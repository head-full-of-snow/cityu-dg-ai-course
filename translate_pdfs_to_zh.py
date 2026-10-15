from __future__ import annotations

import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence

import fitz
import torch
from transformers import MarianMTModel, MarianTokenizer


ROOT = Path(r"c:\Users\admin\Desktop\港城莞AI课程")
FONTFILE = Path(r"C:\Windows\Fonts\simhei.ttf")
MODEL_NAME = "Helsinki-NLP/opus-mt-en-zh"
BATCH_SIZE = 24
MAX_NEW_TOKENS = 256
SKIP_SUFFIXES = ("_zh.pdf", "_zh_preview.pdf")

LATIN_RE = re.compile(r"[A-Za-z]")
SPACE_RE = re.compile(r"\s+")


@dataclass
class LineItem:
    page_index: int
    bbox: fitz.Rect
    text: str
    font_size: float
    color: tuple[float, float, float]


def find_pdfs(root: Path) -> list[Path]:
    pdfs = sorted(root.rglob("*.pdf"))
    return [p for p in pdfs if not p.name.endswith(SKIP_SUFFIXES)]


def normalize_text(text: str) -> str:
    return SPACE_RE.sub(" ", text).strip()


def looks_translatable(text: str) -> bool:
    text = normalize_text(text)
    if len(text) < 2:
        return False
    if not LATIN_RE.search(text):
        return False

    alpha_count = sum(ch.isalpha() for ch in text)
    if alpha_count < 2:
        return False

    # Skip mostly symbolic fragments like formulas or separators.
    symbol_count = sum(not ch.isalnum() and not ch.isspace() for ch in text)
    if symbol_count > len(text) * 0.45:
        return False

    return True


def int_to_rgb(value: int) -> tuple[float, float, float]:
    return (
        ((value >> 16) & 255) / 255.0,
        ((value >> 8) & 255) / 255.0,
        (value & 255) / 255.0,
    )


def collect_line_items(doc: fitz.Document) -> list[LineItem]:
    items: list[LineItem] = []
    for page_index, page in enumerate(doc):
        text_dict = page.get_text("dict")
        for block in text_dict.get("blocks", []):
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                if not spans:
                    continue
                text = normalize_text("".join(span.get("text", "") for span in spans))
                if not looks_translatable(text):
                    continue

                bbox = fitz.Rect(line["bbox"])
                font_size = max(span.get("size", 8.0) for span in spans)
                color = int_to_rgb(spans[0].get("color", 0))
                items.append(
                    LineItem(
                        page_index=page_index,
                        bbox=bbox,
                        text=text,
                        font_size=font_size,
                        color=color,
                    )
                )
    return items


class PdfTranslator:
    def __init__(self) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME, local_files_only=True)
        self.model = MarianMTModel.from_pretrained(MODEL_NAME, local_files_only=True).to(self.device)
        self.model.eval()
        self.cache: Dict[str, str] = {}

    def translate_many(self, texts: Sequence[str]) -> None:
        unseen = [text for text in texts if text not in self.cache]
        if not unseen:
            return

        for start in range(0, len(unseen), BATCH_SIZE):
            batch = unseen[start : start + BATCH_SIZE]
            inputs = self.tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
            ).to(self.device)
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=MAX_NEW_TOKENS,
                    num_beams=4,
                )
            translations = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
            for src, dst in zip(batch, translations):
                dst = normalize_text(dst)
                self.cache[src] = dst or src

    def translate_text(self, text: str) -> str:
        if text not in self.cache:
            self.translate_many([text])
        return self.cache[text]


def fit_textbox(
    page: fitz.Page,
    bbox: fitz.Rect,
    text: str,
    color: tuple[float, float, float],
    base_font_size: float,
) -> None:
    font_size = max(4.0, min(base_font_size * 0.95, bbox.height * 0.92))
    rect = fitz.Rect(bbox)
    rect.x1 += max(0, rect.height * 0.25)
    rect.y1 += max(0, rect.height * 0.15)

    while font_size >= 4.0:
        rc = page.insert_textbox(
            rect,
            text,
            fontname="zhfont",
            fontsize=font_size,
            color=color,
            align=fitz.TEXT_ALIGN_LEFT,
            overlay=True,
        )
        if rc >= 0:
            return

        # Remove failed insertion attempt by repainting the area again.
        page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1), overlay=True)
        font_size -= 0.5

    page.insert_textbox(
        rect,
        text,
        fontname="zhfont",
        fontsize=4.0,
        color=color,
        align=fitz.TEXT_ALIGN_LEFT,
        overlay=True,
    )


def translate_pdf(pdf_path: Path, translator: PdfTranslator) -> tuple[Path, int]:
    doc = fitz.open(pdf_path)
    try:
        line_items = collect_line_items(doc)
        unique_texts = sorted({item.text for item in line_items})
        translator.translate_many(unique_texts)

        grouped: Dict[int, List[LineItem]] = {}
        for item in line_items:
            grouped.setdefault(item.page_index, []).append(item)

        for page_index, items in grouped.items():
            page = doc[page_index]
            for item in items:
                page.add_redact_annot(item.bbox, fill=(1, 1, 1))
            page.apply_redactions()

            page.insert_font(fontname="zhfont", fontfile=str(FONTFILE))
            for item in items:
                translated = translator.translate_text(item.text)
                fit_textbox(page, item.bbox, translated, item.color, item.font_size)

        out_path = pdf_path.with_name(f"{pdf_path.stem}_zh.pdf")
        doc.save(out_path, garbage=3, deflate=True)
        return out_path, len(line_items)
    finally:
        doc.close()


def main() -> None:
    pdfs = find_pdfs(ROOT)
    print(f"Found {len(pdfs)} PDF files.")
    translator = PdfTranslator()

    for index, pdf_path in enumerate(pdfs, start=1):
        print(f"[{index}/{len(pdfs)}] Translating: {pdf_path}")
        try:
            out_path, line_count = translate_pdf(pdf_path, translator)
            print(f"  -> Saved: {out_path} (translated lines: {line_count})")
        except Exception as exc:
            print(f"  !! Failed: {pdf_path}")
            print(f"     {type(exc).__name__}: {exc}")


if __name__ == "__main__":
    main()
