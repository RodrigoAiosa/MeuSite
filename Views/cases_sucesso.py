import streamlit as st
import os
import base64
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Cases de Sucesso")

# --- ESTILO CSS (CARDS EM GRID COM EFEITO HOVER) ---
st.markdown(
    """
    <style>
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 24px;
        margin-top: 20px;
        margin-bottom: 40px;
    }

    .card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 15px;
        border: 2px solid rgba(0, 180, 216, 0.5);
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
        transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }

    .card:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 12px 24px rgba(0, 180, 216, 0.35);
        border-color: rgba(0, 180, 216, 1);
    }

    .card img {
        width: 100%;
        display: block;
        border-radius: 13px 13px 0 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏆 Cases de Sucesso")
st.write("Confira os resultados da nossa Mentoria Estratégica.")

# Imagens do efeito de card: 11, 22, 33, 44, 55, 66, 77, 88, 99
cards = [f"{n}{n}.png" for n in range(1, 10)]


def imagem_para_base64(caminho):
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


cards_html = '<div class="cards-grid">'
faltando = []

for slide in cards:
    caminho_img = os.path.join("assets", slide)
    if os.path.exists(caminho_img):
        img_b64 = imagem_para_base64(caminho_img)
        cards_html += f'<div class="card"><img src="data:image/png;base64,{img_b64}"></div>'
    else:
        faltando.append(slide)

cards_html += '</div>'

st.markdown(cards_html, unsafe_allow_html=True)

for slide in faltando:
    st.warning(f"Imagem não encontrada: {slide}")

exibir_rodape()
