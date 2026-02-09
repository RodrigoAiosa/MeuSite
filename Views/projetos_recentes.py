import streamlit as st
from utils import exibir_rodape, registrar_acesso
import webbrowser

# --- REGISTRO DE ACESSO ---
registrar_acesso("Vitrine de Projetos (Landing Page)")

# --- ESTILO CSS PARA LANDING PAGE ---
st.markdown(
    """
    <style>
    .project-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 30px;
        transition: transform 0.3s ease, border 0.3s ease;
        height: 450px; /* Ajustado para acomodar o botão do Streamlit */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        border: 1px solid #00b4d8;
        box-shadow: 0 10px 30px rgba(0, 180, 216, 0.2);
    }
    
    .project-title {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: bold;
        margin: 15px 0 10px 0;
        min-height: 60px;
    }
    
    .project-image-container {
        width: 100%;
        height: 200px;
        overflow: hidden;
        border-radius: 10px;
    }
    
    .project-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    /* Estilização para o botão do Streamlit parecer o seu anterior */
    div.stButton > button {
        width: 100%;
        background-color: transparent;
        color: #00b4d8 !important;
        border: 1px solid #00b4d8 !important;
        border-radius: 8px;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: #00b4d8 !important;
        color: #111827 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: white;'>🚀 Portfólio de Projetos</h1>", unsafe_allow_html=True)
st.write("")

# --- DADOS DOS PROJETOS ---
projects = [
    {
        "title": "🎈 Domando a Web: Automatizando a Coleta de Dados",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7396548688942231552",
        "img": "https://media.licdn.com/dms/image/v2/D5605AQG_O4aWEEr-TA/feedshare-thumbnail_720_1280/B56ZqXRlDZJUA0-/0/1763474559478?e=1771120800&v=beta&t=CcUM7AgRyDg2-fNTDZ9IkforQ6O5Hw3eD2Hf1XkZkKI"
    },
    {
        "title": "💡 Chega de Sofrer Enviando Currículo na Mão – Automatize AGORA<<",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401302855799828480",
        "img": "https://media.licdn.com/dms/image/v2/D5605AQFOzpwPAE77QQ/videocover-low/B56Zra1qRCHkBQ-/0/1764608093688?e=1771120800&v=beta&t=dvUGvY1ixWmBZtZA3rUTFEfpeVfSyLbmvmeuZBPQEIA"
    },
    {
        "title": " 🚀 Por que este script muda a forma de olhar para o mercado de trabalho",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7417316742781399040",
        "img": "https://media.licdn.com/dms/image/v2/D5605AQGx_Pu_f5S1eQ/feedshare-thumbnail_720_1280/B56Zu.aQJFIsA4-/0/1768426111860?e=1771120800&v=beta&t=7PWQR4yv97hNkBjtscb_lI5QTVvfNdhxbQ8f1hjpgi4"
    },
    {
        "title": "🏛️ O Fim da Era Manual: Dashboard Automático",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425547898580328449",
        "img": "https://media.licdn.com/dms/image/v2/D5605AQEZjyr3_u48-w/feedshare-thumbnail_720_1280/B56ZwzYaHOK4A4-/0/1770388562694?e=1771030800&v=beta&t=ylHtVPZgzEbyzEqvBv0v9-hHF0x4ZEpn-k8ktPDilXg"
    },
    {
        "title": "📊 Análise Pro: Sistemas de Amortização",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425612242248835073/",
        "img": "https://media.licdn.com/dms/image/v2/D5622AQF74taisme4XA/feedshare-shrink_480/B56Zw0S_FZHIAs-/0/1770403918426?e=1772064000&v=beta&t=eqFjQKekX8rYQATeRIhy2uruedxVjRL29Oo7Xt97Ogw"
    },
    {
        "title": "📍 Ciência por trás da Prospecção de Alta Performance",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425188593134026752",
        "img": "https://media.licdn.com/dms/image/v2/D5605AQEYmI4B2ByfGw/feedshare-thumbnail_720_1280/B56ZwuRowKK8A4-/0/1770302901551?e=1771030800&v=beta&t=DxCLIdRDCnXLMcadvJwW6zhWXMXZl6PoIm-PzzZM0fY"
    },
    {
        "title": "🚗 Contagem de Veículos em Tempo Real (Visão Computacional)",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422736985196371969",
        "img": "https://media.licdn.com/dms/image/v2/D5605AQHKj124qT0VeA/feedshare-thumbnail_720_1280/B56ZwLb66MIUA8-/0/1769718394777?e=1771030800&v=beta&t=Ytd5H0Ctowz9PYkim4wpahKxudojH9-kkiY5HLmd_2s"
    },
    {
        "title": "💡 Pedra, Papel e Tesoura com Inteligência Artificial",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422420309632303104",
        "img": "https://media.licdn.com/dms/image/v2/D5605AQEnOdzL023RyA/feedshare-thumbnail_720_1280/B56ZwG76crJoA4-/0/1769642895486?e=1771030800&v=beta&t=lA5YIEjUivMZFCCnFPOY6CG3Iinb6N6GFD0nXls-UzI"
    },
    {
        "title": "❤️ O dia em que a IA me ajudou como PAI",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7420842332155142144",
        "img": "https://media.licdn.com/dms/image/v2/D5605AQGGIbt2tD1Weg/feedshare-thumbnail_720_1280/B56ZvEub9nHAA4-/0/1768532066431?e=1771030800&v=beta&t=Cr22rY2M1p6TEYvf7fC36OJ-oaRFkCtBXEvcijBX450"
    }
]

# --- RENDERIZAÇÃO ---
for i in range(0, len(projects), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(projects):
            project = projects[i + j]
            with cols[j]:
                # Card visual (HTML apenas para imagem e título)
                st.markdown(f"""
                <div class="project-card">
                    <div>
                        <div class="project-image-container">
                            <img src="{project['img']}" class="project-image">
                        </div>
                        <h3 class="project-title">{project['title']}</h3>
                    </div>
                """, unsafe_allow_html=True)
                
                # Botão do Streamlit para capturar o clique
                if st.button("Ver Demonstração", key=f"btn_{i+j}"):
                    # REGISTRA O CLIQUE NA PLANILHA
                    registrar_acesso(nome_pagina=project['title'], acao="Clique no Link")
                    # ABRE O LINK EM NOVA ABA (Via JavaScript)
                    st.markdown(f'<script>window.open("{project["link"]}", "_blank");</script>', unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")
exibir_rodape()
