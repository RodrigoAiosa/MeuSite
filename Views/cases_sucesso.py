import streamlit as st
import os
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
# Registra o acesso na planilha "Relatorio_Acessos_Site" (ID: 1TCx...CVI)
registrar_acesso("Cases de Sucesso")

# --- ESTILO CSS PARA IMAGENS ---
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

# Lista de slides localizados na pasta assets
slides = [
    "Slide6.JPG", "Slide7.JPG", "Slide8.JPG", "Slide9.JPG",
    "Slide10.JPG", "Slide11.JPG", "Slide12.JPG", "Slide13.JPG", "Slide14.JPG"
]

# Loop para exibir as imagens
for slide in slides:
    caminho_img = os.path.join("assets", slide)
    
    # Verifica se o arquivo realmente existe para evitar erros visuais
    if os.path.exists(caminho_img):
        st.image(caminho_img, use_container_width=True)
        st.markdown("---")
    else:
        st.warning(f"Imagem não encontrada: {slide}")

# Exibe o rodapé padrão da SKY DATA SOLUTION
exibir_rodape()
