import streamlit as st

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
        margin-bottom: 10px;
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
    .iframe-container {
        border: 2px solid #31333F;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 60px;
        background-color: #f0f2f6; /* Fundo leve para o app carregar */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🐍 Projetos em Python")
st.write("Interaja com as aplicações diretamente abaixo ou abra em tela cheia.")
st.markdown("---")

# --- FUNÇÃO PARA RENDERIZAR APPS PYTHON ---
def render_python_app(title, url):
    # Botão de acesso rápido
    st.markdown(f'<a href="{url}" target="_blank" class="project-button">{title} ↗️</a>', unsafe_allow_html=True)
    
    # App incorporado (Embed)
    st.markdown(
        f"""
        <div class="iframe-container">
            <iframe 
                src="{url}?embed=true" 
                width="100%" 
                height="700" 
                frameborder="0" 
                allowfullscreen>
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- LISTA DE PROJETOS ---

# Projeto 1: Leilão
render_python_app(
    "⚖️ Calculadora de Viabilidade de Leilão Profissional",
    "https://calculadoraleilao.streamlit.app/"
)

# Projeto 2: Google Maps
render_python_app(
    "📍 Extrator de Dados - Google Maps",
    "https://gerarlead.streamlit.app/"
)

# Projeto 3: Amortização
render_python_app(
    "📊 Análise Pro: Sistemas de Amortização",
    "https://guiadaamortizacao.streamlit.app/"
)

# Projeto 4: Gestão de Custos
render_python_app(
    "☕ Gestão de Custos: Açúcar",
    "https://economiacafe.streamlit.app/"
)

st.info("💡 Nota: Algumas aplicações podem levar instantes para 'acordar' caso não tenham sido usadas recentemente.")