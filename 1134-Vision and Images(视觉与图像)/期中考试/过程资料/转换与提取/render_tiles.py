import fitz, os, sys
from PIL import Image
sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__)) + '/..'
os.chdir(ROOT)

TILES = {
    'tile01_lec01_32_lec02_6_7_11': [('lec01_filtering', 32), ('lec02_edge', 6), ('lec02_edge', 7), ('lec02_edge', 11)],
    'tile02_lec02_12_13_14_15':    [('lec02_edge', 12), ('lec02_edge', 13), ('lec02_edge', 14), ('lec02_edge', 15)],
    'tile03_lec03_26_28_30':       [('lec03_resample', 26), ('lec03_resample', 28), ('lec03_resample', 30)],
    'tile04_lec04_23_24_26_30':    [('lec04_harris', 23), ('lec04_harris', 24), ('lec04_harris', 26), ('lec04_harris', 30)],
    'tile05_lec04_31_38_39_46':    [('lec04_harris', 31), ('lec04_harris', 38), ('lec04_harris', 39), ('lec04_harris', 46)],
    'tile06_lec05_10_21_23':       [('lec05_invariance', 10), ('lec05_invariance', 21), ('lec05_invariance', 23)],
    'tile07_lec06_13_15_16_27':    [('lec06_descriptors_matching', 13), ('lec06_descriptors_matching', 15), ('lec06_descriptors_matching', 16), ('lec06_descriptors_matching', 27)],
    'tile08_lec07_11_12_19_20':    [('lec07_transformations', 11), ('lec07_transformations', 12), ('lec07_transformations', 19), ('lec07_transformations', 20)],
    'tile09_lec07_21_25_26_33':    [('lec07_transformations', 21), ('lec07_transformations', 25), ('lec07_transformations', 26), ('lec07_transformations', 33)],
    'tile10_lec13_6_10_16_24':     [('lec13_stereo', 6), ('lec13_stereo', 10), ('lec13_stereo', 16), ('lec13_stereo', 24)],
    'tile11_lec14_23_lec15_26_39': [('lec14_mvs', 23), ('lec15_neural_networks', 26), ('lec15_neural_networks', 39), ('lec15_neural_networks', 41)],
    'tile12_lec15_48_50_lec16_23_44': [('lec15_neural_networks', 48), ('lec15_neural_networks', 50), ('lec16_cnns_transformers', 23), ('lec16_cnns_transformers', 44)],
}

os.makedirs('.pdf_convert/tiles', exist_ok=True)
for tname, pages in TILES.items():
    imgs = []
    for pdf, pno in pages:
        doc = fitz.open(f'.pdf_convert/{pdf}.pdf')
        pix = doc[pno-1].get_pixmap(matrix=fitz.Matrix(1.6, 1.6))
        p = f'.pdf_convert/tiles/_tmp_{pdf}_{pno}.png'
        pix.save(p)
        imgs.append((p, pdf, pno))
        doc.close()
    ims = [Image.open(p) for p, _, _ in imgs]
    W = max(im.width for im in ims)
    gap = 26
    H = sum(im.height for im in ims) + gap * (len(ims) - 1)
    canvas = Image.new('RGB', (W, H), 'white')
    y = 0
    for im in ims:
        canvas.paste(im, (0, y))
        y += im.height + gap
    outp = f'.pdf_convert/tiles/{tname}.png'
    canvas.save(outp)
    for p, _, _ in imgs:
        os.remove(p)
    print(tname, canvas.size, 'from', [(pdf.split("_")[0], pno) for _, pdf, pno in imgs])
print('TILES DONE')
