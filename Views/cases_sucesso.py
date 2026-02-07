import streamlit as st
import os

# --- ESTILO CSS PARA IMAGENS GRANDES ---
st.markdown(
    """
    <style>
    /* Remove preenchimentos extras e força a imagem a usar 100% da largura do container */
    .stImage > img {
        width: 100% !important;
        border-radius: 15px;
        border: 2px solid rgba(0, 180, 216, 0.5);
        margin-bottom: 30px;
    }
    /* Estilização do container do título para não sumir no fundo */
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

# --- RENDERIZAÇÃO DOS SLIDES EM TAMANHO MÁXIMO ---
# Lista baseada na sua pasta assets
slides = [
    "Slide6.JPG", "Slide7.JPG", "Slide8.JPG", "Slide9.JPG", 
    "Slide10.JPG", "Slide11.JPG", "Slide12.JPG", "Slide13.JPG", "Slide14.JPG"
]

for slide in slides:
    # Caminho relativo correto a partir da raiz do Streamlit
    caminho_img = os.path.join("assets", slide)
    
    # use_container_width=True faz com que a imagem ocupe toda a área central
    st.image(caminho_img, use_container_width=True)
    st.markdown("---") # Linha separadora entre os slides

st.info("💡 Deslize para baixo para visualizar todos os marcos alcançados.")