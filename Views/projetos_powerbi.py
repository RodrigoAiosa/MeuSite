import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- ESTILO CSS ---
st.markdown(
    """
    <style>
    .hero-container {
        background: linear-gradient(135deg, #111827 0%, #0f172a 100%);
        padding: 40px;
        border-radius: 20px;
        border-left: 5px solid #00b4d8;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 15px;
    }
    .hero-text {
        font-size: 1.1rem;
        color: #9ca3af;
        line-height: 1.6;
    }
    .hero-highlight {
        color: #00b4d8;
        font-weight: bold;
    }
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 420px;
        perspective: 1000px;
        margin-bottom: 20px;
        animation: fadeInUp 0.8s ease-out forwards;
        opacity: 0;
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
    }
    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }
    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        border-radius: 18px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 25px;
    }
    .flip-card-front {
        background-color: #111827;
        color: white;
        border: 1px solid #1f2937;
    }
    .flip-card-back {
        background-color: #0f172a;
        color: white;
        transform: rotateY(180deg);
        border: 2px solid #00b4d8;
    }
    .card-icon { font-size: 60px; margin-bottom: 15px; }
    
    .pbi-card-title {
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .pbi-card-tag {
        font-size: 0.8rem;
        font-weight: 900;
        background: rgba(255, 255, 255, 0.2);
        padding: 4px 12px;
        border-radius: 20px;
    }
    .pbi-description {
        font-size: 0.95rem;
        color: #9ca3af;
        line-height: 1.4;
        margin-bottom: 15px;
    }
    .btn-acessar {
        background-color: #00b4d8;
        color: #111827 !important;
        padding: 8px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
        display: inline-block;
    }
    .share-container {
        display: flex;
        gap: 15px;
        margin-top: 10px;
        align-items: center;
    }
    
    .share-icon {
        color: #9ca3af;
        font-size: 1.4rem;
        transition: 0.3s;
        text-decoration: none;
    }
    
    .share-icon:hover { transform: scale(1.2); }
    .icon-li:hover { color: #0077b5; }
    .icon-wa:hover { color: #25d366; }
    </style>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """,
    unsafe_allow_html=True
)

# --- SEÇÃO ESTRATÉGICA (SILOGISMO) ---
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">Decisões de Elite exigem Experiência Real</div>
        <div class="hero-text">
            <p><strong>A Lógica do Sucesso:</strong></p>
            <ol>
                <li>Resultados extraordinários só são alcançados através de <span class="hero-highlight">metodologias validadas pelo tempo</span>.</li>
                <li>Minha consultoria e mentoria sintetizam <span class="hero-highlight">+20 anos de campo</span> em estratégias aplicáveis.</li>
                <li><strong>Logo,</strong> acelerar sua curva de aprendizado e seus lucros comigo não é uma opção, é a <span class="hero-highlight">consequência lógica da excelência.</span></li>
            </ol>
            <p>Não busque apenas dashboards. Busque a inteligência por trás deles.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; font-size: 3rem;'>📊 Dashboards Estratégicos</h1>", unsafe_allow_html=True)
st.write("")

# --- DADOS DOS PROJETOS ---
pbi_projects = [
    {
        "title": "💳 Relatório STONE",
        "icon": "🏛️",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard interativo de Faturamento B2B: monitora KPIs (Faturamento, Margem, Ticket Médio), evolução mensal e filtros regionais."
    },
    {
        "title": "📊 Vendas Meta vs Realizado",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard de Recrutamento e Seleção."
    },
    {
        "title": "📦 Controle de Pedidos BNZ",
        "icon": "📦",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard de Gestão de Estoque."
    },
    {
        "title": "🎯 Análise Dados Estratégica",
        "icon": "🎯",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Controle de metas e vendas."
    },
    {
        "title": "👥 People Analytics (RH)",
        "icon": "👥",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Controle de comissões."
    },
    {
        "title": "🚀 Gestão de Negócios - Relatório Borelli",
        "icon": "🚀",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Controle de produção."
    },
     {
        "title": "🏖️ Dashboard Financeiro — Beocean Resort",
        "icon": "💰",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9&pageName=ae6d1828240b25f04e49",
        "desc": "Painel de gerenciamento financeiro do Beocean Resort, acompanhando receitas, despesas, fluxo de caixa e indicadores operacionais para suporte à tomada de decisão estratégica."
    }
]

# --- RENDERIZAÇÃO ---
for i in range(0, len(pbi_projects), 3):
    cols = st.columns(3)
    for j in range(3):
        idx = i + j
        if idx < len(pbi_projects):
            p = pbi_projects[idx]
            
            # Texto para WhatsApp (com descrição + link personalizado conforme as instruções salvas)
            wa_text = f"Olá Rodrigo! Gostaria de falar sobre o projeto 🚀 *{p['title']}* que vi no seu portfólio.\n\n💡 {p['desc']}\n\n🔗 Link: {p['url']}"
            wa_link = f"https://api.whatsapp.com/send?phone=5511977019335&text={urllib.parse.quote(wa_text)}"
            
            # LinkedIn: SOMENTE A URL
            li_link = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(p['url'])}"

            with cols[j]:
                st.markdown(f"""
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div class="card-icon">{p['icon']}</div>
                            <div class="pbi-card-title">{p['title']}</div>
                            <div class="pbi-card-tag">PASSE O MOUSE ↻</div>
                        </div>
                        <div class="flip-card-back">
                            <div style="font-weight: bold; color: #00b4d8; font-size: 1.2rem; margin-bottom: 20px;">PROJETO</div>
                            <a href="{p['url']}" target="_blank" class="btn-acessar">
                                Abrir Dashboard ↗️
                            </a>
                            <div style="font-size: 0.8rem; color: #9ca3af; margin-top: 12px;">Falar com Rodrigo:</div>
                            <div class="share-container">
                                <a href="{li_link}" target="_blank" class="share-icon icon-li">
                                    <i class="fab fa-linkedin"></i>
                                </a>
                                <a href="{wa_link}" target="_blank" class="share-icon icon-wa">
                                    <i class="fab fa-whatsapp"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
exibir_rodape()

