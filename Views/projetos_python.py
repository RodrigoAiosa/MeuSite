import streamlit as st

# --- ESTILO CSS PARA BOTÕES DE TÍTULO COM HOVER ---
st.markdown(
    """
    <style>
    .project-button {
        display: inline-block;
        background-color: #262730;
        color: #00b4d8 !important;
        font-size: 1.5rem;
        font-weight: bold;
        padding: 15px 25px;
        margin-bottom: 20px;
        border-radius: 10px;
        text-decoration: none;
        transition: transform 0.3s, box-shadow 0.3s, border-color 0.3s;
        border: 1px solid rgba(0, 180, 216, 0.2);
        width: auto;
        min-width: 400px; /* Garante um tamanho de botão robusto */
        cursor: pointer;
    }
    
    .project-button:hover {
        transform: scale(1.05); /* Efeito de Zoom */
        box-shadow: 0 10px 20px rgba(0, 180, 216, 0.4); /* Efeito de Sombra */
        border-color: #00b4d8;
        background-color: #31333F;
    }

    .container {
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Alinhamento à esquerda */
        gap: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🐍 Projetos em Python")
st.write("Clique nos títulos abaixo para acessar as aplicações.")
st.markdown("---")

# --- LISTA DE PROJETOS EM FORMATO DE BOTÃO ---
st.markdown('<div class="container">', unsafe_allow_html=True)

# Projeto 1
st.markdown(
    '<a href="https://calculadoraleilao.streamlit.app/" target="_blank" class="project-button">'
    '⚖️ Calculadora de Viabilidade de Leilão Profissional'
    '</a>', 
    unsafe_allow_html=True
)

# Projeto 2
st.markdown(
    '<a href="https://gerarlead.streamlit.app/" target="_blank" class="project-button">'
    '📍 Extrator de Dados - Google Maps'
    '</a>', 
    unsafe_allow_html=True
)

# Projeto 3
st.markdown(
    '<a href="https://guiadaamortizacao.streamlit.app/" target="_blank" class="project-button">'
    '📊 Análise Pro: Sistemas de Amortização'
    '</a>', 
    unsafe_allow_html=True
)

# Projeto 4
st.markdown(
    '<a href="https://economiacafe.streamlit.app/" target="_blank" class="project-button">'
    '☕ Gestão de Custos: Açúcar'
    '</a>', 
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)