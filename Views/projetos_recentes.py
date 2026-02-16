import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Projetos Recentes",
    page_icon="🚀",
    layout="wide"
)

# --- REGISTRO DE ACESSO ---
registrar_acesso("Vitrine de Projetos")

# --- CSS ---
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #0b1120);
    color: white;
}

.project-card {
    backdrop-filter: blur(14px);
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    padding: 30px 20px;
    margin-bottom: 30px;
    transition: all 0.35s ease;
    min-height: 210px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.project-card:hover {
    transform: translateY(-8px);
    border: 1px solid rgba(0, 180, 216, 0.6);
    box-shadow: 0 20px 40px rgba(0, 180, 216, 0.15);
}

.project-title {
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 20px;
}

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
    display: block;
    margin-bottom: 12px;
}

.view-button:hover {
    background: #00b4d8;
    color: #0f172a;
}

.share-container {
    display: flex;
    gap: 12px;
    justify-content: center;
}

.share-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    border-radius: 10px;
    background: rgba(255,255,255,0.05);
}

.main-title {
    text-align: center;
    font-size: 2.2rem;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 50px;
}

</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<div class='main-title'>🚀 Portfólio de Projetos</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Projetos de Python, BI e IA</div>", unsafe_allow_html=True)

# --- PROJETOS ---
projects = [
    {
        "title": "📊 Automatizei o cálculo de custo de funcionários",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7429183442157989888",
    },
    {
        "title": "🚀 Automação gerando mil arquivos em segundos",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7250105059819040768",
    },
    {
        "title": "🎮 Tetris com IA em Python",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401703226657406976",
    },
]

# --- GRID ---
for i in range(0, len(projects), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(projects):
            project = projects[i + j]

            link_encoded = urllib.parse.quote(project["link"])
            text_encoded = urllib.parse.quote(project["title"] + " " + project["link"])

            linkedin_share = f"https://www.linkedin.com/sharing/share-offsite/?url={link_encoded}"
            whatsapp_share = f"https://wa.me/?text={text_encoded}"

            with cols[j]:
                st.markdown(f"""
                <div class="project-card">
                    <div class="project-title">{project['title']}</div>

                    <a href="{project['link']}" target="_blank" class="view-button">
                        Ver Demonstração
                    </a>

                    <div class="share-container">

                        <a href="{linkedin_share}" target="_blank" class="share-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#0A66C2" viewBox="0 0 24 24">
                                <path d="M4.98 3.5C4.98 4.88 3.86 6 2.48 6S0 4.88 0 3.5 1.12 1 2.5 1 5 2.12 5 3.5zM0 8h5v16H0V8zm7.5 0h4.7v2.2h.1c.7-1.2 2.3-2.4 4.7-2.4 5 0 6 3.3 6 7.6V24h-5v-7.3c0-1.7 0-3.9-2.4-3.9s-2.8 1.9-2.8 3.8V24h-5V8z"/>
                            </svg>
                        </a>

                        <a href="{whatsapp_share}" target="_blank" class="share-icon">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#25D366" viewBox="0 0 24 24">
                                <path d="M20.52 3.48A11.83 11.83 0 0 0 12.06 0C5.4 0 .01 5.39.01 12.04c0 2.12.55 4.19 1.6 6.02L0 24l6.13-1.6a11.96 11.96 0 0 0 5.93 1.51h.01c6.65 0 12.05-5.39 12.05-12.04a11.9 11.9 0 0 0-3.6-8.39z"/>
                            </svg>
                        </a>

                    </div>
                </div>
                """, unsafe_allow_html=True)

# --- RODAPÉ ---
exibir_rodape()
