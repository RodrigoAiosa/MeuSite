import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- ESTILO CSS ATUALIZADO ---
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
    
    /* Efeito do Card */
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
        overflow: hidden;
    }
    
    /* Efeito de revelação da descrição no Back do Card */
    .pbi-description {
        font-size: 0.95rem;
        color: #9ca3af;
        line-height: 1.4;
        margin-bottom: 15px;
        opacity: 0;
        transform: translateY(20px);
        transition: all 0.5s ease-in-out;
        transition-delay: 0.3s;
    }
    .flip-card:hover .pbi-description {
        opacity: 1;
        transform: translateY(0);
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
    .btn-acessar {
        background-color: #00b4d8;
        color: #111827 !important;
        padding: 8px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
        display: inline-block;
        opacity: 0;
        transition: 0.5s;
        transition-delay: 0.5s;
    }
    .flip-card:hover .btn-acessar {
        opacity: 1;
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

    /* Estilo da barra de pesquisa */
    div[data-testid="stTextInput"] input {
        background-color: #111827 !important;
        color: #ffffff !important;
        border: 1px solid #00b4d8 !important;
        border-radius: 12px !important;
        padding: 12px 20px !important;
        font-size: 1rem !important;
    }
    div[data-testid="stTextInput"] input::placeholder {
        color: #6b7280 !important;
    }
    div[data-testid="stTextInput"] input:focus {
        box-shadow: 0 0 0 2px rgba(0, 180, 216, 0.3) !important;
        border-color: #00b4d8 !important;
    }
    .search-result-count {
        text-align: center;
        color: #6b7280;
        font-size: 0.9rem;
        margin-bottom: 20px;
    }
    .search-result-count span {
        color: #00b4d8;
        font-weight: bold;
    }
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

# --- BARRA DE PESQUISA ---
col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
with col_s2:
    search_query = st.text_input(
        label="",
        placeholder="🔍  Pesquisar dashboard...",
        key="search_pbi"
    )

st.write("")

# --- DADOS DOS PROJETOS ---
pbi_projects = [
    {
        "title": "Portal da Transparência - Ilheus",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTM2ZWFlM2QtOTc2NC00NDQ2LTg2ZTctOGY5Nzc4YTk2YWM1IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9&pageName=6a9e62a06ecb8db6c215",
        "desc": "Meu dashboard em Power BI do Portal da Transparência de Ilhéus transforma dados públicos em informação clara e estratégica. Com visualizações interativas, é possível acompanhar receitas, despesas e indicadores em tempo real, fortalecendo o controle social e apoiando decisões mais conscientes e transparentes."
    },
    {
        "title": "💹 DRE Estratégico — Análise Financeira",
        "icon": "📊",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiOWE0ZmU3ZTMtYzAyYi00NDE1LTg3YWItYjcxZTE2ZWI2OWRjIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9&disablecdnExpiration=1766386882",
        "desc": "Dashboard financeiro focado no acompanhamento detalhado do DRE, com análises vertical e horizontal que permitem avaliar a composição de receitas, custos e despesas ao longo do tempo. A solução oferece insights estratégicos sobre rentabilidade, margens e tendências financeiras, apoiando gestores na tomada de decisões mais precisas e alinhadas aos objetivos corporativos."
    },
    {
        "title": "🏦 Monitoramento de Vagas — Bradesco",
        "icon": "📋",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMjQxN2Q4NGYtNWRmNy00NWVjLWE4YmQtNWMyNWYwNGYyZDUzIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Dashboard estratégico para acompanhamento de vagas abertas no site oficial do Bradesco, oferecendo visão consolidada por área, localização, tipo de vaga e volume de oportunidades ativas. A solução permite identificar tendências de contratação, mapear demandas por perfil profissional e apoiar decisões estratégicas de recrutamento com base em dados atualizados do mercado bancário."
    },
    {
        "title": "💳 Relatório STONE",
        "icon": "🏛️",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Solução avançada para monitoramento de faturamento B2B, consolidando KPIs essenciais como Margem de Contribuição e Ticket Médio. O dashboard permite uma análise granular da evolução mensal e performance por filtros regionais, facilitando a identificação de gargalos operacionais e oportunidades de expansão no setor financeiro."
    },
    {
        "title": "📊 Vendas Meta vs Realizado",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Focado na gestão de Recrutamento e Seleção, este painel transforma dados brutos em inteligência estratégica. Acompanhe o funil de contratação, tempo médio de fechamento de vagas e eficiência dos canais de recrutamento, permitindo que o RH atue de forma preditiva na composição das equipes e no alcance das metas corporativas."
    },
    {
        "title": "📦 Controle de Pedidos BNZ",
        "icon": "📦",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Sistema de gestão de estoque inteligente que oferece visibilidade total sobre o fluxo de mercadorias. O dashboard monitora níveis de inventário, giro de produtos e status de pedidos em tempo real, auxiliando na prevenção de rupturas e no otimização logística para garantir que o suprimento atenda à demanda com precisão."
    },
    {
        "title": "🎯 Análise Dados Estratégica",
        "icon": "🎯",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Painel voltado para a alta gestão, focado no controle rigoroso de metas e performance de vendas. Através de visualizações dinâmicas, é possível confrontar o planejado vs. realizado, analisar tendências de mercado e ajustar táticas comerciais rapidamente para garantir o atingimento dos objetivos estratégicos da organização."
    },
    {
        "title": "👥 People Analytics (RH)",
        "icon": "👥",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Especializado na gestão de remuneração variável, este dashboard automatiza o controle de comissões e bonificações. A ferramenta garante transparência e precisão nos cálculos, correlacionando o desempenho individual com os pagamentos efetuados, reduzindo erros operacionais e aumentando a motivação da força de vendas."
    },
    {
        "title": "🚀 Gestão de Negócios - Relatório Borelli",
        "icon": "🚀",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard focado na eficiência fabril e controle de produção. Monitora o ciclo produtivo completo, desde a entrada de insumos até o produto final, destacando índices de produtividade, desperdícios e ocupação de capacidade. Ideal para gestores que buscam otimizar processos e reduzir custos operacionais na indústria."
    },
    {
        "title": "🏖️ Dashboard Financeiro — Beocean Resort",
        "icon": "💰",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9&pageName=ae6d1828240b25f04e49",
        "desc": "Painel de controle financeiro integral para o setor de hotelaria. Oferece uma visão clara do fluxo de caixa, receitas por categoria e despesas operacionais. Com indicadores de saúde financeira atualizados, permite uma gestão de tesouraria mais segura e decisões baseadas em dados para maximizar a rentabilidade do resort."
    }
]

# --- FILTRO DE PESQUISA ---
if search_query:
    filtered_projects = [
        p for p in pbi_projects
        if search_query.lower() in p["title"].lower() or search_query.lower() in p["desc"].lower()
    ]
    total = len(filtered_projects)
    label = "resultado" if total == 1 else "resultados"
    st.markdown(
        f"<div class='search-result-count'>🔎 <span>{total}</span> {label} para <span>\"{search_query}\"</span></div>",
        unsafe_allow_html=True
    )
else:
    filtered_projects = pbi_projects

# --- MENSAGEM QUANDO NÃO HÁ RESULTADOS ---
if not filtered_projects:
    st.markdown(
        """
        <div style='text-align:center; padding: 60px 20px; color: #6b7280;'>
            <div style='font-size: 3rem;'>🔍</div>
            <div style='font-size: 1.2rem; margin-top: 10px;'>Nenhum dashboard encontrado.</div>
            <div style='font-size: 0.95rem; margin-top: 5px;'>Tente outro termo de pesquisa.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- RENDERIZAÇÃO ---
for i in range(0, len(filtered_projects), 3):
    cols = st.columns(3)
    for j in range(3):
        idx = i + j
        if idx < len(filtered_projects):
            p = filtered_projects[idx]
            
            wa_text = f"{p['title']}* que vi no seu portfólio.\n\n💡 {p['desc']}\n\n🔗 Link: {p['url']}"
            wa_link = f"https://wa.me/?text={urllib.parse.quote(wa_text)}"
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
                            <div style="font-weight: bold; color: #00b4d8; margin-bottom: 5px;">PROJETO</div>
                            <div class="pbi-description">{p['desc']}</div>
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
