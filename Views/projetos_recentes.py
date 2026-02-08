import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA (Caso seja rodado sozinho) ---
# st.set_page_config(layout="wide", page_title="Projetos | Rodrigo Aiosa")

# --- ESTILO CSS PARA LANDING PAGE ---
st.markdown(
    """
    <style>
    /* Container dos Cards */
    .main-project-container {
        padding: 20px 0px;
    }
    
    /* Card do Projeto */
    .project-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 30px;
        transition: transform 0.3s ease, border 0.3s ease;
        height: 420px; /* Altura fixa para manter o grid uniforme */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        border: 1px solid #00b4d8;
        box-shadow: 0 10px 30px rgba(0, 180, 216, 0.2);
    }
    
    /* Título do Projeto */
    .project-title {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: bold;
        margin: 15px 0 10px 0;
        line-height: 1.4;
        min-height: 60px; /* Garante que títulos longos não quebrem o layout */
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    
    /* Imagem do Projeto */
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
        transition: transform 0.5s ease;
    }
    
    .project-card:hover .project-image {
        transform: scale(1.1);
    }
    
    /* Botão/Link Estilizado */
    .view-button {
        background-color: transparent;
        color: #00b4d8;
        border: 1px solid #00b4d8;
        padding: 8px 15px;
        border-radius: 8px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 0.9rem;
        font-weight: bold;
        transition: all 0.3s;
        margin-top: 10px;
    }
    
    .view-button:hover {
        background-color: #00b4d8;
        color: #111827;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- TÍTULO DA SEÇÃO ---
st.markdown("<h1 style='text-align: center; color: white;'>🚀 Portfólio de Projetos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Uma seleção das soluções desenvolvidas utilizando Python, BI e Inteligência Artificial.</p>", unsafe_allow_html=True)
st.write("")
st.write("")

# --- DEFINIÇÃO DOS DADOS DOS PROJETOS ---
projects = [
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

# --- RENDERIZAÇÃO DO GRID DE CARDS ---
# Criando linhas com 3 colunas cada
for i in range(0, len(projects), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(projects):
            project = projects[i + j]
            with cols[j]:
                st.markdown(f"""
                <div class="project-card">
                    <div>
                        <div class="project-image-container">
                            <img src="{project['img']}" class="project-image">
                        </div>
                        <h3 class="project-title">{project['title']}</h3>
                    </div>
                    <a href="{project['link']}" target="_blank" class="view-button">Ver Demonstração</a>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #6b7280;'>Rodrigo Aiosa © 2026 | Soluções em Dados</p>", unsafe_allow_html=True)