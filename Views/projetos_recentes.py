import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- CONFIG ---
st.set_page_config(page_title="Portfólio", page_icon="🚀", layout="wide")

# --- REGISTRO ---
registrar_acesso("Vitrine de Projetos")

# --- CSS + FONT AWESOME ---
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
    .project-card {
        background: #111827;
        border-radius: 18px;
        padding: 25px;
        border: 1px solid #1f2937;
        margin-bottom: 20px;
        text-align: center;
        transition: 0.3s;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 280px;
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
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .view-button {
        background-color: #00b4d8 !important;
        color: #111827 !important;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none !important;
        font-weight: bold;
        font-size: 0.9rem;
        display: inline-block;
        margin-bottom: 15px;
    }

    .share-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        border-top: 1px solid #1f2937;
        padding-top: 15px;
    }

    .share-icon {
        color: #9ca3af !important;
        font-size: 1.5rem;
        transition: 0.3s;
        text-decoration: none !important;
    }

    .icon-li:hover { color: #0077b5 !important; }
    .icon-wa:hover { color: #25d366 !important; }
</style>
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
cols = st.columns(3)

for idx, p in enumerate(projects):
    # Para o LinkedIn, vamos usar apenas a URL do conteúdo
    li_share_url = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(p['link'])}"
    
    # WhatsApp com mensagem personalizada
    wa_msg = f"Olá Rodrigo! Vi seu projeto '{p['title']}' no seu portfólio e gostaria de conversar sobre ele."
    wa_link = f"https://wa.me/5511977019335?text={urllib.parse.quote(wa_msg)}"
    
    with cols[idx % 3]:
        # Criamos o HTML concatenando strings curtas para forçar o Streamlit a renderizar corretamente
        card_html = "<div class='project-card'>"
        card_html += f"<div class='project-title'>{p['title']}</div>"
        card_html += f"<div><a href='{p['link']}' target='_blank' class='view-button'>Ver Demonstração</a></div>"
        card_html += "<div class='share-container'>"
        card_html += f"<a href='{li_share_url}' target='_blank' class='share-icon icon-li'><i class='fab fa-linkedin'></i></a>"
        card_html += f"<a href='{wa_link}' target='_blank' class='share-icon icon-wa'><i class='fab fa-whatsapp'></i></a>"
        card_html += "</div></div>"
        
        st.markdown(card_html, unsafe_allow_html=True)

# --- RODAPÉ ---
exibir_rodape()
