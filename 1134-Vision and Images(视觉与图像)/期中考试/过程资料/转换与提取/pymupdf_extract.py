import fitz, os, sys
sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__)) + '/..'
os.chdir(ROOT)

OUT = '期中考试/课件提取MD'
os.makedirs(OUT, exist_ok=True)

LECTURES = {
    'lec00_introduction': 50, 'lec01_filtering': 39, 'lec02_edge': 30,
    'lec03_resample': 38, 'lec04_harris': 49, 'lec05_invariance': 31,
    'lec06_descriptors_matching': 46, 'lec07_transformations': 41,
    'lec13_stereo': 37, 'lec14_mvs': 34, 'lec15_neural_networks': 61,
    'lec16_cnns_transformers': 55,
}

for name, pages in LECTURES.items():
    doc = fitz.open(f'.pdf_convert/{name}.pdf')
    lines = [f'# {name}', '',
             '> PyMuPDF 文本层提取；公式为图形对象无法直接提取，',
             '> 由人工核对幻灯片后以 LaTeX 补全（标注【公式】）。', '']
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        lines.append(f'## Slide {i+1}')
        lines.append('')
        if text:
            # normalize: collapse >2 blank lines
            parts = [p.strip() for p in text.split('\n') if p.strip()]
            lines.append('\n'.join(parts))
        else:
            lines.append('（纯图片页，无文本层）')
        lines.append('')
    with open(f'{OUT}/{name}.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(name, len(doc), 'pages done')
print('ALL DONE')
