import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("🦉 AIosa Agente de IA")

# --- ESTILO CSS ---
st.markdown(
    """
    <style>
    .project-button {
        display: inline-block;
        background-color: #262730;
        color: #00b4d8 !important;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 12px 20px;
        margin-bottom: 5px;
        border-radius: 10px;
        text-decoration: none;
        transition: transform 0.3s, box-shadow 0.3s;
        border: 1px solid rgba(0, 180, 216, 0.2);
        width: 100%;
        max-width: 800px;
        cursor: pointer;
        text-align: left;
    }
    .project-button:hover {
        transform: scale(1.01);
        box-shadow: 0 8px 16px rgba(0, 180, 216, 0.3);
        border-color: #00b4d8;
    }
    .project-description {
        color: #ffffff;
        font-size: 0.95rem;
        margin-bottom: 15px;
        padding-left: 5px;
        max-width: 800px;
        line-height: 1.4;
    }
    .highlight-blue {
        color: #00b4d8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- TÍTULO ---
st.markdown('<h1>🦉 <span class="highlight-blue">AI</span>osa Agente de IA</h1>', unsafe_allow_html=True)
st.write("Aplicações web completas desenvolvidas para automação de processos e análise financeira.")
st.markdown("---")

# --- BOTÃO QUE ABRE EM NOVA ABA ---
st.markdown(
    """
    <a href="https://aiosaia.streamlit.app/" target="_blank" class="project-button">
        🦉<span style="color:#00b4d8;">AI</span>OSA — Assistente Virtual Inteligente ↗️
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="project-description">Assistente virtual desenvolvido por Rodrigo Aiosa. Clique para abrir o chat.</div>',
    unsafe_allow_html=True
)

exibir_rodape()
