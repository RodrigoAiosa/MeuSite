import streamlit as st
from utils import exibir_rodape, registrar_acesso, conectar_google_sheets
import pandas as pd

# --- REGISTRO DE ACESSO À PÁGINA ---
registrar_acesso("Vitrine de Projetos (Ranking)")

# --- LÓGICA DE CAPTURA DE CLIQUE ---
# Se o usuário clicar no link, a página recarrega com um ID no link. 
# Capturamos isso aqui para registrar na planilha.
query_params = st.query_params
if "clique_em" in query_params:
    projeto_clicado = query_params["clique_em"]
    registrar_acesso(nome_pagina=projeto_clicado, acao="Clique no Link")
    # Limpa o parâmetro da URL para não registrar duplicado no refresh
    st.query_params.clear()

# --- FUNÇÃO PARA OBTER RANKING ---
@st.cache_data(ttl=60)
def obter_ranking_projetos():
    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("Relatorio_Acessos_Site").sheet1
            dados = sheet.get_all_records()
            df = pd.DataFrame(dados)
            if not df.empty and 'acao' in df.columns and 'pagina' in df.columns:
                ranking = df[df['acao'] == "Clique no Link"]['pagina'].value_counts().to_dict()
                return ranking
        return {}
    except:
        return {}

# --- ESTILO CSS (Mantendo sua identidade visual) ---
st.markdown(
    """
    <style>
    .project-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 30px;
        transition: transform 0.3s ease;
        height: 460px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .project-card:hover { transform: translateY(-10px); border: 1px solid #00b4d8; }
    .project-title { color: #ffffff; font-size: 1.1rem; font-weight: bold; min-height: 60px; margin: 15px 0; }
    .project-image-container { width: 100%; height: 200px; overflow: hidden; border-radius: 10px; }
    .project-image { width: 100%; height: 100%; object-fit: cover; }
    
    .views-badge {
        background: rgba(0, 180, 216, 0.1);
        color: #00b4d8;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-bottom: 10px;
        display: inline-block;
    }

    .view-button {
        background-color: transparent;
        color: #00b4d8 !important;
        border: 1px solid #00b4d8;
        padding: 8px 15px;
        border-radius: 8px;
        text-align: center;
        text-decoration: none;
        display: block;
        font-size: 0.9rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    .view-button:hover { background-color: #00b4d8; color: #111827 !important; text-decoration: none; }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; color: white;'>🚀 Portfólio de Projetos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Projetos ordenados dinamicamente pelos mais acessados.</p>", unsafe_allow_html=True)

# --- DADOS DOS PROJETOS ---
projects = [
    {"title": "🎈 Domando a Web: Automatizando a Coleta de Dados", "link": "https://www.linkedin.com/feed/update/urn:li:activity:7396548688942231552", "img": "https://media.licdn.com/dms/image/v2/D5605AQG_O4aWEEr-TA/feedshare-thumbnail_720_1280/B56ZqXRlDZJUA0-/0/1763474559478?e=1771120800&v=beta&t=CcUM7AgRyDg2-fNTDZ9IkforQ6O5Hw3eD2Hf1XkZkKI"},
    {"title": "💡 Chega de Sofrer Enviando Currículo na Mão – Automatize AGORA<<", "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401302855799828480", "img": "https://media.licdn.com/dms/image/v2/D5605AQFOzpwPAE77QQ/videocover-low/B56Zra1qRCHkBQ-/0/1764608093688?e=1771120800&v=beta&t=dvUGvY1ixWmBZtZA3rUTFEfpeVfSyLbmvmeuZBPQEIA"},
    {"title": " 🚀 Por que este script muda a forma de olhar para o mercado de trabalho", "link": "https://www.linkedin.com/feed/update/urn:li:activity:7417316742781399040", "img": "https://media.licdn.com/dms/image/v2/D5605AQGx_Pu_f5S1eQ/feedshare-thumbnail_720_1280/B56Zu.aQJFIsA4-/0/1768426111860?e=1771120800&v=beta&t=7PWQR4yv97hNkBjtscb_lI5QTVvfNdhxbQ8f1hjpgi4"},
    {"title": "🏛️ O Fim da Era Manual: Dashboard Automático", "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425547898580328449", "img": "https://media.licdn.com/dms/image/v2/D5605AQEZjyr3_u48-w/feedshare-thumbnail_720_1280/B56ZwzYaHOK4A4-/0/1770388562694?e=1771030800&v=beta&t=ylHtVPZgzEbyzEqvBv0v9-hHF0x4ZEpn-k8ktPDilXg"},
    {"title": "📊 Análise Pro: Sistemas de Amortização", "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425612242248835073/", "img": "https://media.licdn.com/dms/image/v2/D5622AQF74taisme4XA/feedshare-shrink_480/B56Zw0S_FZHIAs-/0/1770403918426?e=1772064000&v=beta&t=eqFjQKekX8rYQATeRIhy2uruedxVjRL29Oo7Xt97Ogw"},
    {"title": "📍 Ciência por trás da Prospecção de Alta Performance", "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425188593134026752", "img": "https://media.licdn.com/dms/image/v2/D5605AQEYmI4B2ByfGw/feedshare-thumbnail_720_1280/B56ZwuRowKK8A4-/0/1770302901551?e=1771030800&v=beta&t=DxCLIdRDCnXLMcadvJwW6zhWXMXZl6PoIm-PzzZM0fY"},
    {"title": "🚗 Contagem de Veículos em Tempo Real (Visão Computacional)", "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422736985196371969", "img": "https://media.licdn.com/dms/image/v2/D5605AQHKj124qT0VeA/feedshare-thumbnail_720_1280/B56ZwLb66MIUA8-/0/1769718394777?e=1771030800&v=beta&t=Ytd5H0Ctowz9PYkim4wpahKxudojH9-kkiY5HLmd_2s"},
    {"title": "💡 Pedra, Papel e Tesoura com Inteligência Artificial", "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422420309632303104", "img": "https://media.licdn.com/dms/image/v2/D5605AQEnOdzL023RyA/feedshare-thumbnail_720_1280/B56ZwG76crJoA4-/0/1769642895486?e=1771030800&v=beta&t=lA5YIEjUiv)MZFCCnFPOY6CG3Iinb6N6GFD0nXls-UzI"},
    {"title": "❤️ O dia em que a IA me ajudou como PAI", "link": "https://www.linkedin.com/feed/update/urn:li:activity:7420842332155142144", "img": "https://media.licdn.com/dms/image/v2/D5605AQGGIbt2tD1Weg/feedshare-thumbnail_720_1280/B56ZvEub9nHAA4-/0/1768532066431?e=1771030800&v=beta&t=Cr22rY2M1p6TEYvf7fC36OJ-oaRFkCtBXEvcijBX450"}
]

# --- APLICAR ORDENAÇÃO ---
cliques = obter_ranking_projetos()
for p in projects:
    p['views'] = cliques.get(p['title'], 0)

projects_sorted = sorted(projects, key=lambda x: x['views'], reverse=True)

# --- RENDERIZAÇÃO DO GRID ---
for i in range(0, len(projects_sorted), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(projects_sorted):
            p = projects_sorted[i + j]
            with cols[j]:
                # O segredo: o link abre em nova aba E recarrega a página atual com o parâmetro de registro
                # Ao clicar, o navegador abre o LinkedIn imediatamente. O Streamlit detecta o clique no próximo refresh.
                st.markdown(f"""
                <div class="project-card">
                    <div>
                        <div class="project-image-container">
                            <img src="{p['img']}" class="project-image">
                        </div>
                        <h3 class="project-title">{p['title']}</h3>
                        <div class="views-badge">🔥 {p['views']} interessados</div>
                    </div>
                    <a href="{p['link']}" 
                       target="_blank" 
                       class="view-button" 
                       onclick="window.location.href='?clique_em={p['title']}'">
                       Ver Demonstração
                    </a>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
exibir_rodape()
