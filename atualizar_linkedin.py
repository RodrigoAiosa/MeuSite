#!/usr/bin/env python3
"""
Atualiza data/linkedin_posts.json, que alimenta a aba "Em destaque Linkedin" do site.

O LinkedIn não tem feed público gratuito para perfis pessoais, então há dois caminhos
oficiais (sem scraping) para alimentar o arquivo:

1) Exportação de dados do LinkedIn (recomendado para importar vários posts de uma vez)
   LinkedIn > Configurações e privacidade > Privacidade de dados > "Obter uma cópia dos seus dados"
   > marque "Publicações" (Shares). Baixe o .zip, extraia e rode:

       python atualizar_linkedin.py --csv caminho/para/Shares.csv

2) Adicionar um post por vez (link + texto copiado do post):

       python atualizar_linkedin.py --add "https://www.linkedin.com/feed/update/urn:li:share:123.../" \
           --texto "Texto do post copiado do LinkedIn"

   A data é calculada a partir do ID do post; use --data AAAA-MM-DD para forçar outra.

Em ambos os casos o script faz merge com o que já existe (sem duplicar), ordena do mais
recente para o mais antigo e mantém no máximo --max posts (padrão 100). O site exibe os 70
mais recentes e usa o arquivo inteiro para a pesquisa por palavra-chave.
Depois é só fazer commit e push: a Vercel republica o site sozinha.
"""
import argparse
import csv
import datetime as dt
import json
import re
import sys
from pathlib import Path

ARQUIVO = Path(__file__).parent / "data" / "linkedin_posts.json"
TITULO_MAX = 90


def extrair_urn(link: str):
    """Devolve o URN usado no embed do LinkedIn, ou None se o link não tiver ID."""
    m = re.search(r"urn:li:(share|ugcPost|activity):(\d{10,})", link)
    if m:
        return f"urn:li:{m.group(1)}:{m.group(2)}"
    m = re.search(r"activity-(\d{10,})", link)  # links do tipo /posts/usuario_titulo-activity-123-xxxx
    if m:
        return f"urn:li:activity:{m.group(1)}"
    return None


def data_do_urn(urn: str):
    """IDs do LinkedIn carregam o timestamp (ms) nos bits mais altos."""
    m = re.search(r":(\d{10,})$", urn or "")
    if not m:
        return None
    ms = int(m.group(1)) >> 22
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).strftime("%Y-%m-%d")


def dividir(texto: str):
    """Primeira linha vira título (até TITULO_MAX); o restante vira o texto de apoio."""
    texto = (texto or "").replace("\r\n", "\n").strip()
    if not texto:
        return "", ""
    linhas = texto.split("\n")
    primeira, resto = linhas[0].strip(), "\n".join(linhas[1:]).strip()
    if len(primeira) <= TITULO_MAX:
        return primeira, resto
    corte = primeira[:TITULO_MAX].rsplit(" ", 1)[0].rstrip(",;:- ")
    return corte + "…", texto


def novo_post(link: str, texto: str, data: str | None, imagem: str | None = None,
              curtidas: int | None = None, comentarios: int | None = None):
    """imagem/curtidas/comentarios são opcionais: alimentam a capa, o engajamento e a ordenação do site."""
    urn = extrair_urn(link)
    titulo, corpo = dividir(texto)
    post = {
        "urn": urn,
        "url": link.strip(),
        "date": (data or data_do_urn(urn) or dt.date.today().isoformat())[:10],
        "title": titulo or "Publicação no LinkedIn",
        "text": corpo,
    }
    if imagem is not None:
        post["image"] = imagem or ""
    if curtidas is not None:
        post["likes"] = int(curtidas)
    if comentarios is not None:
        post["comments"] = int(comentarios)
    return post


def chave(p):
    return p.get("urn") or p.get("url")


def carregar():
    if ARQUIVO.exists():
        return json.loads(ARQUIVO.read_text(encoding="utf-8")).get("posts", [])
    return []


def salvar(posts, maximo):
    vistos, unicos = {}, []
    for p in posts:  # a ordem recebida dá prioridade aos registros novos
        k = chave(p)
        if k in vistos:
            # mantém imagem/engajamento do registro antigo quando o novo não trouxe esses campos
            for campo in ("image", "likes", "comments"):
                if campo not in vistos[k] and campo in p:
                    vistos[k][campo] = p[campo]
            continue
        vistos[k] = p
        unicos.append(p)
    unicos = sorted(unicos, key=lambda p: p.get("date", ""), reverse=True)[:maximo]
    ARQUIVO.parent.mkdir(parents=True, exist_ok=True)
    ARQUIVO.write_text(
        json.dumps({"atualizado_em": dt.date.today().isoformat(), "posts": unicos}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return unicos


def ler_csv(caminho: Path):
    posts = []
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        for linha in csv.DictReader(f):
            link = (linha.get("ShareLink") or "").strip()
            if not link:
                continue
            # Em um post existente, o texto do CSV complementa/atualiza o registro
            posts.append(novo_post(link, linha.get("ShareCommentary", ""), (linha.get("Date") or "")[:10] or None))
    return posts


def main():
    ap = argparse.ArgumentParser(description="Atualiza os posts da aba 'Em destaque Linkedin'.")
    ap.add_argument("--csv", type=Path, help="Shares.csv da exportação de dados do LinkedIn")
    ap.add_argument("--add", metavar="URL", help="Link de um post para adicionar")
    ap.add_argument("--texto", default="", help="Texto do post (usado com --add)")
    ap.add_argument("--data", help="Data AAAA-MM-DD (usado com --add; padrão: calculada pelo ID)")
    ap.add_argument("--max", type=int, default=100, help="Máximo de posts guardados no arquivo (padrão 100)")
    args = ap.parse_args()

    if not args.csv and not args.add:
        ap.error("informe --csv Shares.csv ou --add URL")

    novos = []
    if args.csv:
        novos += ler_csv(args.csv)
    if args.add:
        novos.append(novo_post(args.add, args.texto, args.data))

    # Os registros novos entram primeiro: em caso de duplicado, valem o texto e a data mais recentes
    final = salvar(novos + carregar(), args.max)
    print(f"{len(novos)} post(s) lido(s); {len(final)} no arquivo. Mais recente: {final[0]['date']} - {final[0]['title']}")


if __name__ == "__main__":
    sys.exit(main())
