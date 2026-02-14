import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Rodrigo Aiosa | Business Intelligence", layout="wide")

# --- ESTILO CSS PSICOLÓGICO (NEUROMARKETING) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* SEÇÃO DE IMPACTO PSICOLÓGICO */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 60px 40px;
        border-radius: 30px;
        border: 2px solid #00b4d8;
        margin-bottom: 40px;
        box-shadow: 0 25px 50px -12px rgba(0, 180, 216, 0.5);
    }

    .neuro-title {
        font-size: 3rem;
        font-weight: 900;
        color: white;
        line-height: 1.1;
        margin-bottom: 20px;
    }

    .neuro-subtitle {
        color: #00b4d8;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 40px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .comparison-grid {
        display: flex;
        gap: 30px;
        margin-bottom: 40px;
        flex-wrap: wrap;
    }

    .comparison-card {
        flex: 1;
        min-width: 300px;
        padding: 30px;
        border-radius: 20px;
        background: rgba(255,255,255,0.03);
    }

    .card-caos { border-left: 5px solid #ef4444; }
    .card-lucro { border-left: 5px solid #22c55e; background: rgba(34, 197, 94, 0.05); }

    .btn-call-action {
        background: #00b4d8;
        color: #111827 !important;
        padding: 20px 45px;
        border-radius: 15px;
        font-weight: 900;
        font-size: 1.1rem;
        text-decoration: none;
        display: inline-block;
        transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
        box-shadow: 0 10px 20px rgba(0, 180, 216, 0.3);
    }

    .btn-call-action:hover {
        transform: scale(1.05) translateY(-5px);
        background: white;
        box-shadow: 0 20px 30px rgba(0, 180, 216, 0.4);
    }

    /* GRID SYMMETRY */
    [data-testid="column"] { padding: 0 16px !important; }

    .flip-card {
        width: 100%;
        height: 400px;
        perspective: 1000px;
        margin-bottom: 32px;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        transition: transform 0.6s;
        transform-style: preserve-3d;
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

    .flip-card-front { background: #111827; border: 1px solid rgba(255,255,255,0.1); }
    .flip-card-back { background: #1e293b; transform: rotateY(180deg); border: 1px solid #00b4d8; }

    @media (max-width: 768px) {
        .neuro-title { font-size: 2rem; }
        .comparison-grid { flex-direction: column; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- HEADER PSICOLÓGICO (CONVENCIMENTO) ---
st.markdown(f"""
<div class="hero-container">
    <div class="neuro-subtitle">O Silogismo do Sucesso</div>
    <h1 class="neuro-title">Você não precisa de mais dados. <br>Você precisa de clareza.</h1>
    
    <div class="comparison-grid">
        <div class="comparison-card card-caos">
            <h4 style="color:#ef4444;">❌ O Custo da Intuição</h4>
            <p style="color:#cbd5e1; font-size:0.95rem;">Decisões baseadas no "achismo" geram desperdício financeiro, perda de tempo e cegueira sobre a saúde real do seu negócio.</p>
        </div>
        <div class="comparison-card card-lucro">
            <h4 style="color:#22c55e;">✅ A Precisão do BI</h4>
            <p style="color:#cbd5e1; font-size:0.95rem;">Dashboards estratégicos transformam números em lucro, revelando gargalos e oportunidades que seus olhos não conseguem ver.</p>
        </div>
    </div>
    
    <div style="text-align:center;">
        <p style="color:white; font-style:italic; margin-bottom:20px;">Se a sua empresa gera dados e você não os usa para lucrar, você está deixando dinheiro na mesa.</p>
        <a href="https://api.whatsapp.com/send?phone=5511977019335&text=Olá Rodrigo! 👋 Quero transformar os dados da minha empresa em lucro. Podemos conversar sobre uma consultoria?" target="_blank" class="btn-call-action">Garantir meu Diagnóstico Gratuito</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- DADOS DOS DASHBOARDS ---
pbi_projects = [
    {"title": "💳 Relatório STONE", "icon": "🏛️", "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Monitoramento de KPIs de faturamento B2B e margem de contribuição."},
    {"title": "📊 Vendas vs Realizado", "icon": "📈", "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Controle absoluto de metas comerciais e performance de equipe."},
    {"title": "🏝️ Financeiro Beocean", "icon": "🏖️", "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9", "desc": "Gestão hoteleira premium: do fluxo de caixa à lucratividade líquida."},
    {"title": "📦 Controle BNZ", "icon": "📦", "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Inteligência em suprimentos e redução drástica de perdas em estoque."},
    {"title": "🎯 Dashboard OEE", "icon": "🎯", "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Eficiência industrial de ponta: disponibilidade e qualidade em tempo real."},
    {"title": "👥 Dashboard de RH", "icon": "👥", "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Análise de People Analytics para redução de turnover e custos de folha."},
    {"title": "🚀 Gestão de Negócios", "icon": "🚀", "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Visão 360º para CEOs: todos os KPIs críticos em uma única tela."}
]

# --- RENDERIZAÇÃO DA GRADE ---
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
                                <div style="font-size:50px; margin-bottom:15px;">{p['icon']}</div>
                                <div class="pbi-card-title">{p['title']}</div>
                                <div style="font-size:0.7rem; color:#00b4d8; letter-spacing:1px;">VER DETALHES ↻</div>
                            </div>
                            <div class="flip-card-back">
                                <p style="font-size:0.85rem; color:#cbd5e1; margin-bottom:20px;">{p['desc']}</p>
                                <a href="{p['url']}" target="_blank" style="background:#00b4d8; color:#111; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:800; font-size:0.75rem;">ACESSAR PROJETO</a>
                                <div style="display:flex; gap:15px; margin-top:20px;">
                                    <a href="{li_link}" target="_blank" style="color:#cbd5e1;"><i class="fab fa-linkedin"></i></a>
                                    <a href="{wa_link}" target="_blank" style="color:#cbd5e1;"><i class="fab fa-whatsapp"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

exibir_rodape()
