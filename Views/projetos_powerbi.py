import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Portfólio de Dashboards | Rodrigo Aiosa", layout="wide")

# --- ESTILO CSS (UI/UX ADVANCED) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main-title {
        background: linear-gradient(90deg, #00b4d8, #0077b5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        margin-bottom: 2rem;
    }

    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 400px;
        perspective: 1000px;
        margin-bottom: 30px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
        transform-style: preserve-3d;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        border-radius: 20px;
    }

    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        border-radius: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 30px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .flip-card-front {
        background: rgba(17, 24, 39, 0.95);
        color: white;
    }

    .flip-card-back {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
        transform: rotateY(180deg);
        border: 2px solid #00b4d8;
    }

    .card-icon { 
        font-size: 70px; 
        margin-bottom: 20px;
        filter: drop-shadow(0 0 10px #00b4d8);
    }
    
    .pbi-card-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 15px;
        letter-spacing: -0.5px;
    }

    .pbi-card-tag {
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        background: #00b4d8;
        color: #111827;
        padding: 5px 15px;
        border-radius: 50px;
    }

    .pbi-description {
        font-size: 0.9rem;
        color: #cbd5e1;
        line-height: 1.6;
        margin-bottom: 25px;
    }

    .btn-acessar {
        background: #00b4d8;
        color: #111827 !important;
        padding: 12px 25px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 800;
        font-size: 0.85rem;
        transition: 0.3s;
        text-transform: uppercase;
    }

    .btn-acessar:hover {
        background: #ffffff;
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(0, 180, 216, 0.3);
    }

    .share-container {
        display: flex;
        gap: 20px;
        margin-top: 20px;
    }
    
    .share-icon {
        color: #94a3b8;
        font-size: 1.5rem;
        transition: 0.3s;
        text-decoration: none;
    }
    
    .share-icon:hover { transform: scale(1.2); }
    .icon-li:hover { color: #0a66c2; }
    .icon-wa:hover { color: #25d366; }
    </style>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='main-title' style='text-align: center; font-size: 3.5rem;'>📊 Dashboards Estratégicos</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; margin-top: -20px;'>Soluções de BI personalizadas para o seu negócio.</p>", unsafe_allow_html=True)

# --- DADOS DOS PROJETOS ---
pbi_projects = [
    {
        "title": "💳 Relatório STONE",
        "icon": "🏛️",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Análise de Faturamento B2B: monitoramento de KPIs, Margem e Ticket Médio por região."
    },
    {
        "title": "📊 Vendas vs Realizado",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Gestão estratégica de metas e funil de Recrutamento & Seleção (RH)."
    },
    {
        "title": "📦 Controle BNZ",
        "icon": "📦",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Otimização de Supply Chain e Gestão de Estoque em tempo real."
    },
    {
        "title": "🎯 Análise Estratégica",
        "icon": "🎯",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmBeItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard focado em performance de vendas e alcance de objetivos comerciais."
    },
    {
        "title": "👥 People Analytics",
        "icon": "👥",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Gestão de talentos e controle automatizado de comissões de vendas."
    },
    {
        "title": "🚀 Gestão de Negócios",
        "icon": "🚀",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Visão 360º da linha de produção e eficiência operacional."
    }
]

# --- RENDERIZAÇÃO ---
for i in range(0, len(pbi_projects), 3):
    cols = st.columns(3)
    for j in range(3):
        idx = i + j
        if idx < len(pbi_projects):
            p = pbi_projects[idx]
            
            # TEXTO WHATSAPP: Agora inclui a descrição do projeto dinamicamente
            wa_msg = (
                f"Olá Rodrigo! 👋\n\n"
                f"Gostaria de falar sobre o projeto: *{p['title']}*\n"
                f"💡 *Descrição:* {p['desc']}\n\n"
                f"🔗 Link do Dashboard: {p['url']}"
            )
            wa_link = f"https://api.whatsapp.com/send?phone=5511977019335&text={urllib.parse.quote(wa_msg)}"
            
            # LinkedIn Link
            li_link = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(p['url'])}"

            with cols[j]:
                st.markdown(f"""
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div class="card-icon">{p['icon']}</div>
                            <div class="pbi-card-title">{p['title']}</div>
                            <div class="pbi-card-tag">Ver Detalhes ↻</div>
                        </div>
                        <div class="flip-card-back">
                            <div style="font-weight: 800; color: #00b4d8; margin-bottom: 10px; font-size: 0.8rem; letter-spacing: 2px;">DETALHES</div>
                            <div class="pbi-description">{p['desc']}</div>
                            <a href="{p['url']}" target="_blank" class="btn-acessar">Abrir Dashboard</a>
                            <div class="share-container">
                                <a href="{li_link}" target="_blank" title="Compartilhar no LinkedIn" class="share-icon icon-li">
                                    <i class="fab fa-linkedin"></i>
                                </a>
                                <a href="{wa_link}" target="_blank" title="Falar com Rodrigo" class="share-icon icon-wa">
                                    <i class="fab fa-whatsapp"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
exibir_rodape()

