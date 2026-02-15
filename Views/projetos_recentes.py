import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --- CONFIGURAÇÃO ---
st.set_page_config(
    page_title="Portfólio de Projetos",
    page_icon="🚀",
    layout="wide"
)

registrar_acesso("Vitrine de Projetos (Landing Page)")

# --- CSS APPLE STYLE ---
st.markdown("""
<style>

/* Fundo minimalista estilo Apple */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom, #0c0c0c, #111111);
    color: #f5f5f7;
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", sans-serif;
}

/* Título principal */
.main-title {
    text-align: center;
    font-size: 2.8rem;
    font-weight: 600;
    letter-spacing: -0.5px;
    margin-top: 40px;
}

.subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: #86868b;
    margin-top: 10px;
    margin-bottom: 70px;
}

/* Card estilo Apple */
.project-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 22px;
    padding: 35px 25px;
    margin-bottom: 35px;
    transition: all 0.4s cubic-bezier(.28,.11,.32,1);
    min-height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    /* Animação inicial */
    opacity: 0;
    transform: translateY(40px);
    animation: fadeUp 0.9s ease forwards;
}

/* Delay progressivo automático */
.project-card:nth-child(1) { animation-delay: 0.1s; }
.project-card:nth-child(2) { animation-delay: 0.2s; }
.project-card:nth-child(3) { animation-delay: 0.3s; }
.project-card:nth-child(4) { animation-delay: 0.4s; }
.project-card:nth-child(5) { animation-delay: 0.5s; }
.project-card:nth-child(6) { animation-delay: 0.6s; }
.project-card:nth-child(7) { animation-delay: 0.7s; }
.project-card:nth-child(8) { animation-delay: 0.8s; }
.project-card:nth-child(9) { animation-delay: 0.9s; }

/* Keyframe Fade-In */
@keyframes fadeUp {
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* Hover refinado */
.project-card:hover {
    transform: scale(1.03);
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(255, 255, 255, 0.18);
}

/* Título do projeto */
.project-title {
    font-size: 1.15rem;
    font-weight: 500;
    line-height: 1.6;
    margin-bottom: 25px;
}

/* Botão minimalista */
.view-button {
    background: #f5f5f7;
    color: #000;
    border-radius: 12px;
    padding: 10px 18px;
    text-align: center;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    transition: all 0.3s ease;
}

.view-button:hover {
    background: #d2d2d7;
    text-decoration: none;
}

</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<div class='main-title'>Portfólio de Projetos</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Soluções desenvolvidas com Python, BI e Inteligência Artificial.</div>", unsafe_allow_html=True)

# --- PROJETOS ---
projects = [
    {"title": "🎈 Domando a Web: Automatizando a Coleta de Dados",
     "link": "https://www.linkedin.com/feed/update/urn:li:activity:7396548688942231552"},

    {"title": "💡 Chega de Sofrer Enviando Currículo na Mão – Automatize AGORA",
     "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401302855799828480"},

    {"title": "🚀 Por que este script muda a forma de olhar para o mercado de trabalho",
     "link": "https://www.linkedin.com/feed/update/urn:li:activity:7417316742781399040"},

    {"title": "🏛️ O Fim da Era Manual: Dashboard Automático",
     "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425547898580328449"},

    {"title": "📊 Análise Pro: Sistemas de Amortização",
     "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425612242248835073/"},

    {"title": "📍 Ciência por trás da Prospecção de Alta Performance",
     "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425188593134026752"},

    {"title": "🚗 Contagem de Veículos em Tempo Real (Visão Computacional)",
     "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422736985196371969"},

    {"title": "💡 Pedra, Papel e Tesoura com Inteligência Artificial",
     "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422420309632303104"},

    {"title": "❤️ O dia em que a IA me ajudou como PAI",
     "link": "https://www.linkedin.com/feed/update/urn:li:activity:7420842332155142144"},
]

# --- GRID ---
for i in range(0, len(projects), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(projects):
            project = projects[i + j]
            with cols[j]:
                st.markdown(f"""
                <div class="project-card">
                    <div class="project-title">{project['title']}</div>
                    <a href="{project['link']}" target="_blank" class="view-button">
                        Ver Projeto
                    </a>
                </div>
                """, unsafe_allow_html=True)

exibir_rodape()
