import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- CONFIG ---
st.set_page_config(page_title="Portfólio", page_icon="🚀", layout="wide")

# --- REGISTRO ---
registrar_acesso("Vitrine de Projetos")

# --- CSS + FONT AWESOME ---
st.markdown("""
<style>

.project-card {
    background: #111827;
    border-radius: 18px;
    padding: 25px;
    border: 1px solid #1f2937;
    margin-bottom: 20px;
    text-align: center;
    transition: 0.3s;
}

.project-card:hover {
    transform: translateY(-6px);
    border: 1px solid #00b4d8;
}

.project-title {
    font-size: 1.1rem;
    font-weight: bold;
    color: white;
    margin-bottom: 20px;
}

.view-button {
    background-color: #00b4d8;
    color: #111827 !important;
    padding: 8px 20px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: bold;
    font-size: 0.9rem;
    display: inline-block;
    margin-bottom: 12px;
}

.share-container {
    display: flex;
    gap: 15px;
    justify-content: center;
}

.share-icon {
    color: #9ca3af;
    font-size: 1.4rem;
    transition: 0.3s;
    text-decoration: none;
}

.icon-li:hover { color: #0077b5; }
.icon-wa:hover { color: #25d366; }

</style>

<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<h1 style='text-align:center'>🚀 Portfólio de Projetos</h1>", unsafe_allow_html=True)
st.write("")

# --- PROJETOS ---
projects = [
    {
        "title": "📊 Automatizei o cálculo de custo de funcionários",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7429183442157989888",
    },
    {
        "title": "🚀 Gerando mil arquivos em segundos com Python",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7250105059819040768",
    },
    {
        "title": "🎮 Tetris com IA em Python",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401703226657406976",
    }
]

# --- GRID ---
for i in range(0, len(projects), 3):
    cols = st.columns(3)
    for j in range(3):
        idx = i + j
        if idx < len(projects):
            p = projects[idx]

            wa_text = f"Olha esse projeto:\n{p['title']}\n{p['link']}"
            wa_link = f"https://wa.me/?text={urllib.parse.quote(wa_text)}"

            li_link = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(p['link'])}"

            with cols[j]:
                st.markdown(f"""
                <div class="project-card">

                    <div class="project-title">
                        {p['title']}
                    </div>

                    <a href="{p['link']}" target="_blank" class="view-button">
                        Ver Demonstração
                    </a>

                    <div class="share-container">
                        <a href="{li_link}" target="_blank" class="share-icon icon-li">
                            <i class="fab fa-linkedin"></i>
                        </a>

                        <a href="{wa_link}" target="_blank" class="share-icon icon-wa">
                            <i class="fab fa-whatsapp"></i>
                        </a>
                    </div>

                </div>
                """, unsafe_allow_html=True)

# --- RODAPÉ ---
exibir_rodape()
