#!/bin/bash
cd "C:/Users/admin/Desktop/港城莞AI课程/1134-Vision and Images(视觉与图像)" || exit 1
SKILL="C:/Users/admin/.claude/skills/pdf-ocr/scripts/extract_pdf.py"
PARTS=".pdf_convert/parts2"
TMP=".pdf_convert/tmp_chunk2"
mkdir -p "$PARTS" "$TMP"
# reuse earlier successes (lec00 pages 1-8, 9-16)
cp -n .pdf_convert/parts/lec00_introduction_p1.md "$PARTS/lec00_introduction_c01.md" 2>/dev/null
cp -n .pdf_convert/parts/lec00_introduction_p2.md "$PARTS/lec00_introduction_c02.md" 2>/dev/null

okc=0; failc=""
for pdf in .pdf_convert/chunks/*.pdf; do
  base=$(basename "$pdf" .pdf)           # e.g. lec00_introduction_c03
  name=${base%_c*}                        # lec00_introduction
  part="$PARTS/${base}.md"
  [ -f "$part" ] && { echo "SKIP $base"; continue; }
  ok=0
  for try in 1 2 3 4; do
    rm -f "$TMP/${base}.md"
    if timeout 420 python "$SKILL" "$pdf" -o "$TMP" >/dev/null 2>&1 && [ -f "$TMP/${base}.md" ]; then
      mv "$TMP/${base}.md" "$part"; ok=1; break
    fi
    echo "  retry $base (try $try failed $(date +%H:%M:%S))"
    sleep 120
  done
  if [ $ok -eq 1 ]; then echo "OK $base"; okc=$((okc+1)); else echo "FAIL $base"; failc="$failc $base"; fi
done

echo "=== concat phase ==="
for name in lec00_introduction lec01_filtering lec02_edge lec03_resample lec04_harris lec05_invariance lec06_descriptors_matching lec07_transformations lec13_stereo lec14_mvs lec15_neural_networks lec16_cnns_transformers; do
  total=$(ls .pdf_convert/chunks/${name}_c*.pdf 2>/dev/null | wc -l)
  have=$(ls "$PARTS/${name}_c"*.md 2>/dev/null | wc -l)
  if [ "$have" -eq "$total" ] && [ "$total" -gt 0 ]; then
    ls "$PARTS/${name}_c"*.md | sort -V | xargs cat > "期中考试/课件OCR_MD/${name}.md"
    echo "CONCAT $name"
  else
    echo "INCOMPLETE $name ($have/$total)"
  fi
done
echo "=== PIPELINE DONE: $okc newly OCR'd ==="
[ -n "$failc" ] && echo "failed:$failc"
