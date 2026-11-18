"""Baixa para o repositório as imagens dos posts de data/linkedin_posts.json.

Os links de imagem do LinkedIn (media.licdn.com / dms.licdn.com) expiram em poucas
semanas. Este script salva cada imagem em assets/linkedin/<id do post>.jpg e troca o
link no JSON pelo caminho local, para o card do site não perder a imagem.

Roda sozinho pelo GitHub Actions (.github/workflows/linkedin-imagens.yml) sempre que
o JSON muda. Um link que já expirou é ignorado (o card mostra o ícone padrão).
"""
import io, json, os, re, sys, urllib.request
from PIL import Image

ARQ = "data/linkedin_posts.json"
PASTA = "assets/linkedin"
LARGURA_MAX = 800

def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site rodrigoaiosa.vercel.app)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

def main():
    with open(ARQ, encoding="utf-8") as f:
        dados = json.load(f)
    os.makedirs(PASTA, exist_ok=True)
    salvas = falhas = 0
    for p in dados.get("posts", []):
        img = p.get("image") or ""
        if not img.startswith("http"):
            continue
        m = re.search(r"(\d{10,})", p.get("urn", ""))
        if not m:
            continue
        destino = f"{PASTA}/{m.group(1)}.jpg"
        try:
            bruto = baixar(img)
            im = Image.open(io.BytesIO(bruto)).convert("RGB")
            if im.width > LARGURA_MAX:
                im = im.resize((LARGURA_MAX, round(im.height * LARGURA_MAX / im.width)), Image.LANCZOS)
            im.save(destino, "JPEG", quality=85, optimize=True, progressive=True)
            p["image"] = destino
            salvas += 1
            print(f"ok    {destino}  ({p.get('title', '')[:50]})")
        except Exception as e:  # link expirado ou fora do ar: mantém como está
            falhas += 1
            print(f"falha {p.get('urn')}: {e}", file=sys.stderr)
    if salvas:
        with open(ARQ, "w", encoding="utf-8") as f:
            f.write(json.dumps(dados, ensure_ascii=False, indent=2) + "\n")
    print(f"{salvas} imagem(ns) salva(s), {falhas} link(s) indisponível(is).")

if __name__ == "__main__":
    main()
