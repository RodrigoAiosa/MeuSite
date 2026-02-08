import streamlit as st
import os
from utils import exibir_rodape

# --- ESTILO CSS PARA IMAGENS GRANDES ---
st.markdown(
    """
    <style>
    .stImage > img {
        width: 100% !important;
        border-radius: 15px;
        border: 2px solid rgba(0, 180, 216, 0.5);
        margin-bottom: 30px;
    }
    .case-title {
        color: #00b4d8;
        font-size: 2rem;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🏆 Cases de Sucesso")
st.write("Confira os resultados da nossa Mentoria Estratégica em tamanho expandido.")
st.markdown("---")

slides = [
    "Slide6.JPG", "Slide7.JPG", "Slide8.JPG", "Slide9.JPG",
    "Slide10.JPG", "Slide11.JPG", "Slide12.JPG", "Slide13.JPG", "Slide14.JPG"
]

for slide in slides:
    caminho_img = os.path.join("assets", slide)
    st.image(caminho_img, use_container_width=True)
    st.markdown("---")

exibir_rodape()