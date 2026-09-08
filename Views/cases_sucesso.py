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

slides = ["1.PNG", "2.PNG", "3.PNG", "4.PNG", "5.PNG", "6.PNG", "7.PNG", "8.PNG"]

for slide in slides:
    caminho_img = os.path.join("assets", slide)
    if os.path.exists(caminho_img):
        st.image(caminho_img, use_container_width=True)
    else:
        st.warning(f"Imagem não encontrada: {slide}")

exibir_rodape()




