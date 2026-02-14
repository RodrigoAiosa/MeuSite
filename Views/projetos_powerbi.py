import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Rodrigo Aiosa | Business Intelligence", layout="wide")

# --- ESTILO CSS (UX PREMIUM & NEUROMARKETING) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* SEÇÃO DE IMPACTO PSICOLÓGICO RENDERIZADA */
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 60px 40px;
        border-radius: 30px;
        border: 2px solid #00b4d8;
        margin-bottom: 50px;
        box-shadow: 0 25px 50px -12px rgba(0, 180, 216, 0.4);
        text-align: center;
    }

    .neuro-title {
        font-size: 3rem;
        font-weight: 900;
        color: white;
        line-height: 1.1;
        margin-bottom: 25px;
    }

    .comparison-grid {
        display: flex;
        gap: 25px;
        margin: 40px 0;
        text-align: left;
    }

    .comparison-card {
        flex: 1;
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
        transition: 0.3s;
        text-transform: uppercase;
    }

    .btn-call-action:hover {
        transform: translateY(-5px);
        background: white;
    }

    /* GRID SYMMETRY - DISTÂNCIAS IGUAIS */
    [data-testid="column"] { padding: 0 16px !important; }

    .flip-card {
        width: 100%;
        height: 400px;
        perspective: 1000px;
        margin-bottom: 32px; /* Distância vertical igual à horizontal */
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
    .flip-card-back { background: #1e293b; transform: rotateY(180deg); border: 2px solid #00b4d8; }

    @media (max-width: 768px) {
        .comparison-grid { flex-direction: column; }
        .neuro-title { font-size: 2rem; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CABEÇALHO DE CONVENCIMENTO (RENDERIZAÇÃO CORRETA) ---
st.markdown(f"""
<div class="hero-container">
    <div style="color: #00b4d8; font-weight: 700; letter-spacing: 2px; margin-bottom: 10px;">ESTRATÉGIA & PERFORMANCE</div>
    <h1 class="neuro-title">Dados sem inteligência são apenas custos. <br>Eu entrego clareza para lucrar.</h1>
    
    <div class="comparison-grid">
        <div class="comparison-card card-caos">
            <h4 style="color:#ef4444; margin-bottom:10px;">❌ O Custo da Intuição</h4>
            <p style="color:#cbd5e1; font-size:0.95rem;">Decisões baseadas no "achismo" geram desperdício financeiro, perda de tempo e cegueira sobre a saúde real do seu negócio.</p>
        </div>
        <div class="comparison-card card-lucro">
            <h4 style="color:#22c55e; margin-bottom:10px;">✅ A Precisão do BI</h4>
            <p style="color:#cbd5e1; font-size:0.95rem;">Dashboards estratégicos transformam números em lucro, revelando gargalos e oportunidades que seus olhos não conseguem ver.</p>
        </div>
    </div>
    
    <p style="color:white; font-style:italic; margin-bottom:30px;">Se a sua empresa gera dados e você não os usa para decidir, você está deixando dinheiro na mesa.</p>
    <a href="https://api.whatsapp.com/send?phone=5511977019335&text=Olá Rodrigo! 👋 Quero transformar os dados da minha empresa em lucro. Podemos agendar um diagnóstico?" target="_blank" class="btn-call-action">Agendar Diagnóstico Gratuito</a>
</div>
""", unsafe_allow_html=True)

# --- GRID DE PROJETOS ---
pbi_projects = [
    {"title": "💳 Relatório STONE", "icon": "🏛️", "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Monitoramento de KPIs de faturamento B2B e análise de margem regional."},
    {"title": "📊 Vendas vs Realizado", "icon": "📈", "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Controle absoluto de metas comerciais e performance de equipe em tempo real."},
    {"title": "🏝️ Financeiro Beocean", "icon": "🏖️", "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9", "desc": "Gestão hoteleira premium: controle total de fluxo de caixa e lucratividade."},
    {"title": "📦 Controle BNZ", "icon": "📦", "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Inteligência em suprimentos e redução de perdas em estoque operacional."},
    {"title": "🎯 Dashboard OEE", "icon": "🎯", "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Eficiência industrial: monitoramento de disponibilidade e qualidade produtiva."},
    {"title": "👥 Dashboard de RH", "icon": "👥", "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "People Analytics focado em redução de turnover e custos de folha de pagamento."},
    {"title": "🚀 Gestão de Negócios", "icon": "🚀", "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Visão estratégica 360º para suporte imediato à tomada de decisão do CEO."}
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
                
                with cols[j]:
                    st.markdown(f"""
                    <div class="flip-card">
                        <div class="flip-card-inner">
                            <div class="flip-card-front">
                                <div style="font-size:50px; margin-bottom:15px;">{p['icon']}</div>
                                <div style="font-size:1.3rem; font-weight:700; color:white;">{p['title']}</div>
                                <div style="font-size:0.7rem; color:#00b4d8; margin-top:10px;">VER DETALHES ↻</div>
                            </div>
                            <div class="flip-card-back">
                                <p style="font-size:0.85rem; color:#cbd5e1; margin-bottom:20px;">{p['desc']}</p>
                                <a href="{p['url']}" target="_blank" style="background:#00b4d8; color:#111; padding:10px 20px; border-radius:8px; text-decoration:none; font-weight:800; font-size:0.75rem;">ABRIR DASHBOARD</a>
                                <div style="margin-top:20px;">
                                    <a href="{wa_link}" target="_blank" style="color:#25d366; font-size:1.5rem;"><i class="fab fa-whatsapp"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

exibir_rodape()
