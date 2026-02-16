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

# --- CSS GLASSMORPHISM ---
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #0b1120);
    color: white;
}

.main-project-container {
    padding: 40px 0px;
}

.project-card {
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    padding: 30px 20px;
    margin-bottom: 30px;
    transition: all 0.35s ease;
    min-height: 200px;
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
    color: #ffffff;
    font-size: 1.15rem;
    font-weight: 600;
    margin-bottom: 20px;
    line-height: 1.5;
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
    transition: all 0.3s ease;
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
    margin-top: 8px;
}

.share-icon {
    font-size: 20px;
    text-decoration: none;
    transition: transform 0.2s ease;
}

.share-icon:hover {
    transform: scale(1.2);
}

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
        "title": "📊 Automatizei o cálculo de custo de funcionários e o resultado é impressionante!",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7429183442157989888",
    },
    {
        "title": "🚀 Automação em Alta Velocidade: Gerando Mil Arquivos em 30 Segundos com Python ⚡",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7250105059819040768",
    },
    {
        "title": "🎈Criando o clássico jogo TETRIS com python e usando I.A. para jogar",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401703226657406976",
    },
]

# --- GRID RESPONSIVO ---
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
                        <a href="{linkedin_share}" target="_blank" class="share-icon">💼</a>
                        <a href="{whatsapp_share}" target="_blank" class="share-icon">🟢</a>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# --- RODAPÉ ---
exibir_rodape()
