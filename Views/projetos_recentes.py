import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Portfólio de Projetos",
    page_icon="🚀",
    layout="wide"
)

# --- REGISTRO DE ACESSO ---
registrar_acesso("Vitrine de Projetos")

# --- CSS GLASSMORPHISM ---
st.markdown("""
<style>

/* Fundo com gradiente moderno */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #0b1120);
    color: white;
}

/* Container principal */
.main-project-container {
    padding: 40px 0px;
}

/* Card Glass */
.project-card {
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    padding: 30px 20px;
    margin-bottom: 30px;
    transition: all 0.35s ease;
    min-height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* Hover elegante */
.project-card:hover {
    transform: translateY(-8px);
    border: 1px solid rgba(0, 180, 216, 0.6);
    box-shadow: 0 20px 40px rgba(0, 180, 216, 0.15);
}

/* Título */
.project-title {
    color: #ffffff;
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 20px;
    line-height: 1.5;
}

/* Botão Glass */
.view-button {
    background: rgba(0, 180, 216, 0.1);
    color: #00b4d8;
    border: 1px solid rgba(0, 180, 216, 0.4);
    padding: 10px 15px;
    border-radius: 10px;
    text-align: center;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 600;
    transition: all 0.3s ease;
}

.view-button:hover {
    background: #00b4d8;
    color: #0f172a;
    text-decoration: none;
}

/* Título principal */
.main-title {
    text-align: center;
    font-size: 2.2rem;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 50px;
    font-size: 1rem;
}

</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<div class='main-title'>🚀 Portfólio de Projetos</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Uma seleção das soluções desenvolvidas utilizando Python, BI e Inteligência Artificial.</div>", unsafe_allow_html=True)

# --- PROJETOS ---
projects = [
    {
        "title": "🎈 Domando a Web: Automatizando a Coleta de Dados",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7396548688942231552",
    },
    {
        "title": "💡 Chega de Sofrer Enviando Currículo na Mão – Automatize AGORA",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401302855799828480",
    },
    {
        "title": "🚀 Por que este script muda a forma de olhar para o mercado de trabalho",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7417316742781399040",
    },
    {
        "title": "🏛️ O Fim da Era Manual: Dashboard Automático",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425547898580328449",
    },
    {
        "title": "📊 Análise Pro: Sistemas de Amortização",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425612242248835073/",
    },
    {
        "title": "📍 Ciência por trás da Prospecção de Alta Performance",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425188593134026752",
    },
    {
        "title": "🚗 Contagem de Veículos em Tempo Real (Visão Computacional)",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422736985196371969",
    },
    {
        "title": "💡 Pedra, Papel e Tesoura com Inteligência Artificial",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422420309632303104",
    },
    {
        "title": "❤️ O dia em que a IA me ajudou como PAI",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7420842332155142144",
    }
]

# --- GRID RESPONSIVO ---
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
                        Ver Demonstração
                    </a>
                </div>
                """, unsafe_allow_html=True)

# --- RODAPÉ ---
exibir_rodape()
