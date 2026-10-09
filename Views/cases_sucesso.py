import streamlit as st
import re
from pathlib import Path
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---

# --- ESTILO CSS ---
st.markdown(
    """
    <style>
    .stImage > img {
        width: 100% !important;
        border-radius: 15px;
        border: 2px solid rgba(0, 180, 216, 0.5);
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏆 Cases de Sucesso")
st.write("Confira os resultados da nossa Mentoria Estratégica.")

# Mapeia o diretório base do próprio script
BASE_DIR = Path(__file__).resolve().parent

# Tenta localizar a pasta primeiro no mesmo nível da view e, caso não ache, na raiz do projeto
PASTA_IMAGENS = BASE_DIR / "assets" / "img_cases_suceso"
if not PASTA_IMAGENS.exists():
    PASTA_IMAGENS = BASE_DIR.parent / "assets" / "img_cases_suceso"

EXTENSOES_VALIDAS = (".png", ".jpg", ".jpeg", ".webp")


def chave_ordenacao(caminho: Path):
    """Ordena pelo número contido no nome do arquivo (1, 2, 3... 10),
    e não como texto (1, 10, 2, 3...). Se não houver número, joga pro final."""
    numeros = re.findall(r"\d+", caminho.stem)
    return int(numeros[0]) if numeros else float("inf")


if PASTA_IMAGENS.exists():
    slides = sorted(
        [p for p in PASTA_IMAGENS.iterdir() if p.suffix.lower() in EXTENSOES_VALIDAS],
        key=chave_ordenacao
    )

    if not slides:
        st.info("Nenhuma imagem encontrada na pasta de cases de sucesso.")

    for caminho_img in slides:
        try:
            # Passa o caminho: como os arquivos são JPEG com até 1460 px de largura, o Streamlit
            # entrega os bytes originais, sem redimensionar nem recomprimir a cada execução.
            st.image(str(caminho_img), use_container_width=True)
        except Exception:
            st.error(f"Erro ao carregar a imagem '{caminho_img.name}': O arquivo pode estar corrompido ou em formato inválido.")
else:
    st.warning(f"Pasta de imagens não encontrada: {PASTA_IMAGENS}")

exibir_rodape()
