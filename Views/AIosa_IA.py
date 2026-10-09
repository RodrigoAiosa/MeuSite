import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---

# --- ESTILO CSS ---
st.markdown(
    """
    <style>
    .highlight-blue {
        color: #00b4d8;
    }
    .project-description {
        color: #ffffff;
        font-size: 0.95rem;
        margin-bottom: 15px;
        padding-left: 5px;
        max-width: 800px;
        line-height: 1.4;
    }
    .open-btn {
        display: inline-block;
        background-color: #262730;
        color: #00b4d8 !important;
        font-size: 1rem;
        font-weight: bold;
        padding: 8px 16px;
        margin-bottom: 12px;
        border-radius: 8px;
        text-decoration: none;
        transition: transform 0.2s, box-shadow 0.2s;
        border: 1px solid rgba(0, 180, 216, 0.2);
        cursor: pointer;
    }
    .open-btn:hover {
        transform: scale(1.01);
        box-shadow: 0 4px 12px rgba(0, 180, 216, 0.3);
        border-color: #00b4d8;
    }
    .iframe-wrapper {
        border: 2px solid #31333F;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 60px;
        background-color: #ECE5DD;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- TÍTULO ---
st.markdown('<h1>🦉 <span class="highlight-blue">AI</span>osa Agente de IA</h1>', unsafe_allow_html=True)
st.write("Assistente virtual inteligente desenvolvido por Rodrigo Aiosa.")
st.markdown("---")

st.markdown(
    """
    <div class="iframe-wrapper">
        <iframe
            src="https://aiosaia.streamlit.app/?embed=true"
            width="100%"
            height="720"
            frameborder="0"
            allow="clipboard-read; clipboard-write"
            sandbox="allow-forms allow-modals allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-downloads">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

exibir_rodape()
