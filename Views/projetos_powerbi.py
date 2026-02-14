import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Consultoria & Dashboards | Rodrigo Aiosa", layout="wide")

# --- ESTILO CSS (UI/UX ADVANCED) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* SEÇÃO DE VENDAS (SILOGISMO) */
    .sales-section {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 50px 30px;
        border-radius: 24px;
        border: 1px solid rgba(0, 180, 216, 0.3);
        margin-bottom: 50px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    }

    .syllogism-box {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        gap: 20px;
        margin-top: 30px;
    }

    .syllogism-item {
        flex: 1;
        min-width: 250px;
        background: rgba(255,255,255,0.03);
        padding: 25px;
        border-radius: 15px;
        border-left: 4px solid #00b4d8;
    }

    .syllogism-item h4 { color: #00b4d8; margin-bottom: 10px; font-weight: 800; }
    .syllogism-item p { color: #cbd5e1; font-size: 0.95rem; line-height: 1.5; }

    /* GRID SYMMETRY CONTROL */
    [data-testid="column"] {
        padding: 0 16px !important;
    }

    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 400px;
        perspective: 1000px;
        margin-bottom: 32px;
        box-sizing: border-box;
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

    .flip-card:hover .flip-card-inner { transform: rotateY(180deg); }

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
    }

    .flip-card-front { background: rgba(17, 24, 39, 0.95); color: white; }
    .flip-card-back {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: white;
        transform: rotateY(180deg);
        border: 2px solid #00b4d8;
    }

    .card-icon { font-size: 60px; margin-bottom: 15px; filter: drop-shadow(0 0 10px #00b4d8); }
    .pbi-card-title { font-size: 1.3rem; font-weight: 700; margin-bottom: 10px; }
    .pbi-description { font-size: 0.85rem; color: #cbd5e1; margin-bottom: 20px; }

    .btn-cta {
        background: #00b4d8;
        color: #111827 !important;
        padding: 15px 35px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 900;
        display: inline-block;
        margin-top: 25px;
        transition: 0.3s;
        text-transform: uppercase;
    }
    .btn-cta:hover { transform: scale(1.05); background: #fff; }

    @media only screen and (max-width: 768px) {
        .flip-card { height: 380px; }
        .syllogism-item { min-width: 100%; }
    }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """,
    unsafe_allow_html=True
)

# --- SEÇÃO DE VENDAS (SILOGISMO) ---
st.markdown(f"""
<div class="sales-section">
    <h2 style="color: white; font-weight: 900; font-size: 2.5rem; margin-bottom: 10px;">Transforme Dados em Lucro Real</h2>
    <p style="color: #00b4d8; font-size: 1.1rem; font-weight: 600;">Consultoria e Treinamentos Especializados em Power BI</p>
    
    <div class="syllogism-box">
        <div class="syllogism-item">
            <h4>💡 A Premissa</h4>
            <p>Empresas que dominam seus dados crescem 3x mais rápido e reduzem custos operacionais em até 25%.</p>
        </div>
        <div class="syllogism-item">
            <h4>📊 A Solução</h4>
            <p>Minha metodologia de BI elimina a "cegueira gerencial", entregando painéis de alto impacto para decisões imediatas.</p>
        </div>
        <div class="syllogism-item">
            <h4>🚀 O Resultado</h4>
            <p>Ao unir sua expertise de negócio com minha engenharia de dados, sua empresa atinge um novo patamar de previsibilidade.</p>
        </div>
    </div>
    <a href="https://api.whatsapp.com/send?phone=5511977019335&text=Olá Rodrigo! Vi seu portfólio e gostaria de agendar uma consultoria." target="_blank" class="btn-cta">Agendar Consultoria Estratégica</a>
</div>
""", unsafe_allow_html=True)

# --- GRID DE PROJETOS ---
pbi_projects = [
    {"title": "💳 Relatório STONE", "icon": "🏛️", "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Análise de Faturamento B2B: monitoramento de KPIs, Margem e Ticket Médio por região."},
    {"title": "📊 Vendas vs Realizado", "icon": "📈", "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Controle de metas vs realizado para acompanhamento comercial preciso e dinâmico."},
    {"title": "🏝️ Gestão Financeira Beocean", "icon": "🏖️", "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9", "desc": "Dashboard premium hoteleiro: integração total de receitas, despesas e lucratividade líquida."},
    {"title": "📦 Controle BNZ", "icon": "📦", "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Otimização de Supply Chain e Gestão de Estoque em tempo real para alta performance."},
    {"title": "🎯 Dashboard OEE", "icon": "🎯", "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Eficiência Global Industrial: foco em Disponibilidade, Performance e Qualidade."},
    {"title": "👥 Dashboard de RH", "icon": "👥", "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Capital humano estratégico: controle de turnover, absenteísmo e evolução da folha."},
    {"title": "🚀 Gestão de Negócios", "icon": "🚀", "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Inteligência empresarial 360º para monitoramento de KPIs e suporte à decisão."}
]

with st.container():
    for i in range(0, len(pbi_projects), 3):
        cols = st.columns(3) 
        for j in range(3):
            idx = i + j
            if idx < len(pbi_projects):
                p = pbi_projects[idx]
                wa_msg = f"Olá Rodrigo! 👋\n\nGostaria de falar sobre o projeto: *{p['title']}*"
                wa_link = f"https://api.whatsapp.com/send?phone=5511977019335&text={urllib.parse.quote(wa_msg)}"
                li_link = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(p['url'])}"

                with cols[j]:
                    st.markdown(f"""
                    <div class="flip-card">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">
                                <div class="card-icon">{p['icon']}</div>
                                <div class="pbi-card-title">{p['title']}</div>
                                <div class="pbi-card-tag" style="font-size: 0.7rem; background:#00b4d8; padding:3px 10px; border-radius:50px; color:#111;">Ver Detalhes ↻</div>
                            </div>
                            <div class="flip-card-back">
                                <div class="pbi-description">{p['desc']}</div>
                                <a href="{p['url']}" target="_blank" style="background:#00b4d8; color:#111; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:800; font-size:0.8rem;">ABRIR DASHBOARD</a>
                                <div style="display:flex; gap:15px; margin-top:15px;">
                                    <a href="{li_link}" target="_blank" style="color:#cbd5e1; font-size:1.2rem;"><i class="fab fa-linkedin"></i></a>
                                    <a href="{wa_link}" target="_blank" style="color:#cbd5e1; font-size:1.2rem;"><i class="fab fa-whatsapp"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

exibir_rodape()
