import streamlit as st
import os
from pathlib import Path
from PIL import Image, UnidentifiedImageError
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Cases de Sucesso")

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

slides = ["1.png", "2.png", "3.png", "4.png", "5.png", "7.png", "8.png", "9.png","10.png"]

for slide in slides:
    # Tenta localizar primeiro no mesmo nível/pasta da view e, caso não ache, na raiz do projeto
    caminho_img = BASE_DIR / "assets" / slide
    if not caminho_img.exists():
        caminho_img = BASE_DIR.parent / "assets" / slide

    if caminho_img.exists():
        try:
            # Valida a abertura da imagem antes de enviar ao st.image
            img = Image.open(caminho_img)
            st.image(img, use_container_width=True)
        except (UnidentifiedImageError, Exception) as e:
            st.error(f"Erro ao carregar a imagem '{slide}': O arquivo pode estar corrompido ou em formato inválido.")
    else:
        st.warning(f"Imagem não encontrada: {slide} (Caminho procurado: {caminho_img})")

exibir_rodape()
