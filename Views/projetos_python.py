import streamlit as st
import streamlit.components.v1 as components
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Python")

# --- CONFIG PÁGINA ---
st.set_page_config(layout="wide")

# --- ESTILO CSS ---
st.markdown("""
<style>
.project-card {
    background-color: #1E1F25;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
    border: 1px solid rgba(0, 180, 216, 0.15);
}

.project-title {
    font-size: 1.4rem;
    font-weight: bold;
    color: #00b4d8;
    margin-bottom: 8px;
}

.project-description {
    font-size: 0.95rem;
    margin-bottom: 15px;
    line-height: 1.5;
}

.project-button {
    display: inline-block;
    background-color: #262730;
    color: #00b4d8 !important;
    font-weight: bold;
    padding: 10px 18px;
    border-radius: 8px;
    text-decoration: none;
    transition: 0.3s;
    border: 1px solid rgba(0, 180, 216, 0.3);
}

.project-button:hover {
    background-color: #00b4d8;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

st.title("🐍 Projetos em Python")
st.write("Aplicações web completas desenvolvidas para automação, análise de dados e soluções inteligentes.")

# --- LISTA DE PROJETOS (ESTRUTURA ESCALÁVEL) ---
projects = [
    {
        "title": "🔍 Onde no mundo está o hacker das queries?",
        "description": "Inspirado em Carmen Sandiego, um jogo investigativo para treinar SQL de forma gamificada.",
        "url": "https://jogo-sql-sandiego.streamlit.app",
        "embed": False  # 🚨 Streamlit Cloud não permite iframe
    },
    {
        "title": "🗺️ CrimeMap BR — Segurança Pública",
        "description": "Dashboard interativo de criminalidade com dados abertos oficiais do RJ.",
        "url": "https://rodrigoaiosa-crimemap.hf.space",
        "embed": True
    },
    {
        "title": "🦉 Calculadora ROI de Automação",
        "description": "Calculadora que estima o Retorno sobre Investimento (ROI) de projetos de automação.",
        "url": "https://rodrigoaiosa-roi-automacao.hf.space",
        "embed": True
    },
    {
        "title": "💼 APP S.O.S. MULHER",
        "description": "Aplicação voltada à conscientização e apoio.",
        "url": "https://rodrigoaiosa-help-mulher.hf.space",
        "embed": True
    },
    {
        "title": "💼 Precificador Profissional para MEI",
        "description": "Calculadora inteligente de precificação baseada em custos.",
        "url": "https://rodrigoaiosa-precificador-profissional-mei.hf.space",
        "embed": True
    },
    {
        "title": "📍 Extrator de Dados - Google Maps",
        "description": "Extrai informações públicas para geração de leads.",
        "url": "https://rodrigoaiosa-extrair-dados-googlemaps.hf.space",
        "embed": True
    },
    {
        "title": "☕ Gestão de Custos: Açúcar",
        "description": "Aplicação voltada para eliminação de desperdícios e redução de custos.",
        "url": "https://rodrigoaiosa-calcular-custo-acucar.hf.space",
        "embed": True
    }
]

# --- FUNÇÃO DE RENDERIZAÇÃO ---
def render_project(project):
    st.markdown('<div class="project-card">', unsafe_allow_html=True)

    st.markdown(f'<div class="project-title">{project["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="project-description">{project["description"]}</div>', unsafe_allow_html=True)

    st.markdown(
        f'<a href="{project["url"]}" target="_blank" class="project-button">Abrir Aplicação ↗</a>',
        unsafe_allow_html=True
    )

    if project["embed"]:
        components.html(
            f"""
            <iframe
                src="{project["url"]}"
                width="100%"
                height="650"
                style="margin-top:20px; border-radius: 12px; border: 1px solid #31333F;"
            ></iframe>
            """,
            height=680,
        )

    st.markdown('</div>', unsafe_allow_html=True)


# --- RENDERIZA TODOS ---
for project in projects:
    render_project(project)

exibir_rodape()
