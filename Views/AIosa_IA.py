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
    .iframe-container {
        border: 2px solid #31333F;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 60px;
        background-color: #f0f2f6;
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

# --- FUNÇÃO PARA RENDERIZAR APPS COM DESCRIÇÃO ---
def render_python_app(title, description, url):
    st.markdown(f'<a href="{url}" target="_blank" class="project-button">{title} ↗️</a>', unsafe_allow_html=True)
    st.markdown(f'<div class="project-description">{description}</div>', unsafe_allow_html=True)

    clean_url = url.split('#')[0]
    embed_url = f"{clean_url}?embed=true"

    st.markdown(
        f"""
        <div class="iframe-container">
            <iframe 
                src="{embed_url}" 
                width="100%" 
                height="700" 
                frameborder="0" 
                allowfullscreen
                sandbox="allow-forms allow-modals allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-downloads">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- PROJETO ---
render_python_app(
    "🦉<span class='highlight-blue'>AI</span>OSA — Assistente Virtual Inteligente",
    "Assistente virtual desenvolvido por Rodrigo Aiosa.",
    "https://aiosaia.streamlit.app"  # ✅ URL atualizada
)

exibir_rodape()
