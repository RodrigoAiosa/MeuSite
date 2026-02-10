import streamlit as st
import os
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
st.markdown("---")

slides = ["Slide6.JPG", "Slide7.JPG", "Slide8.JPG", "Slide9.JPG", "Slide10.JPG", "Slide11.JPG", "Slide12.JPG", "Slide13.JPG", "Slide14.JPG"]

for slide in slides:
    caminho_img = os.path.join("assets", slide)
    if os.path.exists(caminho_img):
        st.image(caminho_img, use_container_width=True)
        st.markdown("***")
    else:
        st.warning(f"Imagem não encontrada: {slide}")

exibir_rodape()

