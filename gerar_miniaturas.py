"""Gera miniaturas leves (WebP, 720 px) das imagens de assets/img_cases_suceso/ para a grade de cases.

Cada miniatura leva no nome um pedaço do hash da imagem original (ex.: 1-a1b2c3d4.webp). Assim o
navegador pode guardar as miniaturas por 1 ano: se um case mudar, o nome muda e o site busca a nova.
O mapa "imagem original -> miniatura" fica em data/miniaturas.js, lido pelo index.html.
Miniaturas de imagens que não existem mais são apagadas. Roda sozinho pelo GitHub Actions
(.github/workflows/miniaturas-cases.yml); também pode ser rodado à mão: python gerar_miniaturas.py
"""
import glob, hashlib, json, os
from PIL import Image

SRC, OUT, MAPA = "assets/img_cases_suceso", "assets/cases_thumb", "data/miniaturas.js"
LARGURA, QUALIDADE = 720, 78

os.makedirs(OUT, exist_ok=True)
mapa = {}
for f in sorted(glob.glob(f"{SRC}/*.jpg"), key=lambda s: int(os.path.basename(s)[:-4])):
    nome = os.path.basename(f)
    h = hashlib.md5(open(f, "rb").read()).hexdigest()[:8]
    destino = f"{OUT}/{nome[:-4]}-{h}.webp"
    if not os.path.exists(destino):
        im = Image.open(f).convert("RGB")
        if im.width > LARGURA:
            im = im.resize((LARGURA, round(im.height * LARGURA / im.width)), Image.LANCZOS)
        im.save(destino, "WEBP", quality=QUALIDADE, method=6)
        print("gerada", destino, round(os.path.getsize(destino) / 1024), "KB")
    mapa[nome] = destino

for velha in set(glob.glob(f"{OUT}/*.webp")) - set(mapa.values()):
    os.remove(velha); print("removida", velha)

with open(MAPA, "w", encoding="utf-8") as fp:
    fp.write("// Gerado por gerar_miniaturas.py: imagem do case -> miniatura usada na grade do site.\n")
    fp.write("window.MINIATURAS = " + json.dumps(mapa, ensure_ascii=False, indent=1) + ";\n")
print(len(mapa), "miniaturas no mapa")
