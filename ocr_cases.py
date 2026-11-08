"""Extrai por OCR o texto das imagens de assets/img_cases_suceso/ e grava em
data/cases_texto.json, usado pela pesquisa da seção Cases de Sucesso do site.

Rodar sempre que um case for adicionado ou trocado:  python ocr_cases.py
Requer o Tesseract com os idiomas por e eng.
"""
import glob, json, re, subprocess, os, tempfile
from PIL import Image, ImageOps
from concurrent.futures import ThreadPoolExecutor
SRC = "assets/img_cases_suceso"; OUT = "data/cases_texto.json"; TMP = tempfile.mkdtemp()
def ocr(f):
    im = Image.open(f).convert('L')
    if im.width < 2500: im = im.resize((im.width*2, im.height*2), Image.LANCZOS)
    textos = []
    # passa normal e invertida (muitos cases têm texto claro em fundo escuro)
    for k, img in enumerate([im, ImageOps.invert(im)]):
        p = f"{TMP}/{os.path.basename(f)}_{k}.png"; img.save(p)
        r = subprocess.run(['tesseract', p, '-', '-l', 'por+eng', '--psm', '11'], capture_output=True, text=True)
        textos.append(r.stdout); os.remove(p)
    palavras, vistos = [], set()
    for t in textos:
        for w in re.findall(r"[0-9A-Za-zÀ-ÿ$%°ª][0-9A-Za-zÀ-ÿ$%°ª.,/+\-]*", t):
            w = w.strip('.,-/')
            # descarta lixo de OCR: tokens curtos sem vogal ou com mistura estranha
            if len(w) < 2 and not w.isdigit(): continue
            if not re.search(r"[aeiouáéíóúâêôãõàAEIOUÁÉÍÓÚÂÊÔÃÕ0-9]", w): continue
            k = w.lower()
            if k not in vistos: vistos.add(k); palavras.append(w)
    return os.path.basename(f), " ".join(palavras)
files = sorted(glob.glob(f"{SRC}/*.jpg"), key=lambda s: int(os.path.basename(s)[:-4]))
with ThreadPoolExecutor(4) as ex: res = dict(ex.map(ocr, files))
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{len(res)} imagens indexadas em {OUT}")
