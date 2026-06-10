import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- ESTILO MINIMALISTA ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

/* RESET & BASE */
*, *::before, *::after { 
    box-sizing: border-box; 
}

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #0a0c12 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #0a0c12 !important;
    background-image: none !important;
}

[data-testid="stHeader"] { 
    background: transparent !important; 
}

/* TIPOGRAFIA PRINCIPAL */
.main h1, .main h2, .main h3, .main h4,
.main p, .main a, .main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}

/* GARANTE ÍCONES */
.material-symbols-rounded,
.material-icons,
[data-testid*="Collapse"] span,
[data-testid*="collapse"] span {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
}

/* CONTAINER PRINCIPAL */
[data-testid="stMarkdownContainer"] { 
    width: 100% !important; 
}

.block-container {
    max-width: 1200px !important;
    padding: 2rem 2rem 1rem 2rem !important;
    margin: 0 auto !important;
}

/* SCROLLBAR MINIMALISTA */
::-webkit-scrollbar { 
    width: 4px; 
}
::-webkit-scrollbar-track { 
    background: #0a0c12; 
}
::-webkit-scrollbar-thumb { 
    background: rgba(0,180,216,0.15); 
    border-radius: 2px; 
}
::-webkit-scrollbar-thumb:hover { 
    background: rgba(0,180,216,0.3); 
}

/* ── HERO SECTION MINIMAL ── */
.hero-wrapper {
    text-align: center;
    padding: 20px 20px 40px 20px;
    position: relative;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2rem, 4.5vw, 3.5rem);
    font-weight: 700;
    line-height: 1.2;
    letter-spacing: -0.02em;
    color: #e2e8f0;
    margin: 0 auto 16px;
    max-width: 680px;
    text-align: center;
}

.hero-title .accent {
    background: none;
    color: #00b4d8;
}

.hero-subtitle {
    font-size: 1rem;
    font-weight: 400;
    color: #7e8ba3;
    max-width: 560px;
    margin: 0 auto 40px;
    line-height: 1.5;
    text-align: center;
}

/* ── CARD SILOGISMO MINIMAL ── */
.hero-container {
    background: rgba(19,22,31,0.4);
    backdrop-filter: blur(10px);
    padding: 32px 40px;
    border-radius: 16px;
    border-left: 2px solid #00b4d8;
    margin-bottom: 0;
    max-width: 720px;
    width: 100%;
    text-align: left;
}

.hero-container-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.2rem;
    font-weight: 600;
    color: #e2e8f0;
    margin-bottom: 20px;
    letter-spacing: -0.02em;
}

.hero-container-text {
    font-size: 0.9rem;
    color: #7e8ba3;
    line-height: 1.6;
}

.hero-container-text ol {
    padding-left: 20px;
    margin: 12px 0;
}

.hero-container-text li {
    margin-bottom: 8px;
}

.hero-container-text p {
    margin: 8px 0;
}

.hero-highlight {
    color: #00b4d8;
    font-weight: 500;
}

/* ── SEARCH MINIMAL ── */
.search-label {
    text-align: center;
    font-size: 0.8rem;
    color: #4a5568;
    margin-bottom: 12px;
}

div[data-testid="stTextInput"] input {
    background-color: rgba(19,22,31,0.8) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    padding: 12px 18px !important;
    font-size: 0.9rem !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: all 0.2s ease !important;
}

div[data-testid="stTextInput"] input::placeholder { 
    color: #4a5568 !important; 
}

div[data-testid="stTextInput"] input:focus {
    box-shadow: 0 0 0 2px rgba(0,180,216,0.2) !important;
    border-color: rgba(0,180,216,0.4) !important;
    background-color: rgba(19,22,31,0.95) !important;
}

.search-result-count {
    text-align: center;
    color: #4a5568;
    font-size: 0.85rem;
    margin: 16px 0 24px;
}

.search-result-count span {
    color: #00b4d8;
    font-weight: 500;
}

/* ── CARDS MINIMALISTAS (SEM FLIP) ── */
.card {
    background: rgba(19,22,31,0.6);
    backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 24px;
    border: 1px solid rgba(255,255,255,0.05);
    transition: transform 0.2s ease, border-color 0.2s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
}

.card:hover {
    transform: translateY(-4px);
    border-color: rgba(0,180,216,0.3);
}

.card-icon {
    font-size: 40px;
    margin-bottom: 16px;
}

.pbi-card-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.05rem;
    font-weight: 600;
    color: #e2e8f0;
    margin-bottom: 12px;
    line-height: 1.4;
}

.pbi-card-tag {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    background: rgba(0,180,216,0.08);
    color: #00b4d8;
    padding: 4px 12px;
    border-radius: 50px;
    display: inline-block;
    margin-bottom: 16px;
}

.pbi-description {
    font-size: 0.85rem;
    color: #7e8ba3;
    line-height: 1.5;
    margin-bottom: 20px;
    flex-grow: 1;
}

.btn-acessar {
    background: rgba(0,180,216,0.1);
    color: #00b4d8 !important;
    padding: 10px 20px;
    border-radius: 10px;
    text-decoration: none !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600;
    font-size: 0.8rem;
    letter-spacing: 0.3px;
    display: inline-block;
    border: 1px solid rgba(0,180,216,0.15);
    transition: all 0.2s ease;
    text-align: center;
    margin-bottom: 16px;
}

.btn-acessar:hover {
    background: rgba(0,180,216,0.2);
    border-color: rgba(0,180,216,0.4);
}

.share-container {
    display: flex;
    gap: 12px;
    align-items: center;
    justify-content: center;
    padding-top: 12px;
    border-top: 1px solid rgba(255,255,255,0.05);
}

.share-label {
    font-size: 0.7rem;
    color: #4a5568;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.share-icon {
    color: #4a5568;
    font-size: 1.1rem;
    transition: all 0.2s ease;
    text-decoration: none;
}

.share-icon:hover { 
    transform: scale(1.1); 
}

.icon-li:hover { 
    color: #0077b5; 
}

.icon-wa:hover { 
    color: #25d366; 
}

/* ── EMPTY STATE MINIMAL ── */
.empty-state {
    text-align: center;
    padding: 60px 20px;
}

.empty-state-icon { 
    font-size: 2.5rem; 
    margin-bottom: 16px; 
    opacity: 0.3; 
}

.empty-state-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1rem;
    font-weight: 600;
    color: #4a5568;
    margin-bottom: 8px;
}

.empty-state-sub { 
    font-size: 0.85rem; 
    color: #2d3748; 
}

/* ── FOOTER ── */
.footer-spacer { 
    height: 40px; 
}

/* ── RESPONSIVO ── */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem !important;
    }
    
    .hero-container {
        padding: 24px;
    }
    
    .card {
        padding: 20px;
    }
    
    .hero-container-title {
        font-size: 1rem;
    }
}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# --- DADOS DOS PROJETOS ---
pbi_projects = [
    {
        "title": "Dashboard Transporte - Travel Company",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiNjY5NThlNjctZWY1Ny00YjA0LTk0MjEtNzhiNjgzZjdjZjA2IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Transforme dados logísticos em vantagem competitiva. Analise indicadores de performance operacional, identifique pontos de ineficiência e otimize toda a cadeia de transportes."
    },
    {
        "title": "Dashboard ANATEL - Indicadores de Reclamações",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTQ4MGM2MzMtNTU1NS00NjBkLWEyYmItNTI3ZTUyY2NiNjNjIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Transforme dados de reclamações em insights estratégicos. Monitore os indicadores da ANATEL, identifique tendências e gargalos."
    },
    {
        "title": "Dashboard OEE",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2YxN2NhZmQtMTg4My00YTgwLWJhOGQtZmRkNGZkNTM1ZDM0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Transforme dados brutos de eficiência industrial em insights claros. Acompanhe disponibilidade, desempenho e qualidade da produção."
    },
    {
        "title": "Portal da Transparência - Ilheus",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTM2ZWFlM2QtOTc2NC00NDQ2LTg2ZTctOGY5Nzc4YTk2YWM1IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Transforma dados públicos de Ilhéus em informação clara e estratégica. Acompanhe receitas, despesas e indicadores."
    },
    {
        "title": "DRE Estratégico — Análise Financeira",
        "icon": "📊",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiOWE0ZmU3ZTMtYzAyYi00NDE1LTg3YWItYjcxZTE2ZWI2OWRjIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9&disablecdnExpiration=1766386882",
        "desc": "Acompanhamento detalhado do DRE com análises vertical/horizontal. Avalie rentabilidade, margens e tendências."
    },
    {
        "title": "Monitoramento de Vagas — Bradesco",
        "icon": "📋",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMjQxN2Q4NGYtNWRmNy00NWVjLWE4YmQtNWMyNWYwNGYyZDUzIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Visão consolidada de vagas Bradesco por área, localização e perfil. Identifique tendências de contratação."
    },
    {
        "title": "Relatório STONE",
        "icon": "🏛️",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Monitoramento de faturamento B2B com KPIs como Margem de Contribuição e Ticket Médio."
    },
    {
        "title": "Vendas Meta vs Realizado",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Gestão de Recrutamento e Seleção: acompanhe funil, tempo de fechamento e eficiência dos canais."
    },
    {
        "title": "Controle de Pedidos BNZ",
        "icon": "📦",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZDZlNzViNzMtODllZS00OTVlLWI4MWQtNzBhZmU5ZTkxY2E0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Gestão de estoque inteligente: níveis de inventário, giro de produtos e status de pedidos."
    },
    {
        "title": "Análise Dados Estratégica",
        "icon": "🎯",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Alta gestão: controle rigoroso de metas e performance de vendas. Compare planejado vs realizado."
    },
    {
        "title": "People Analytics (RH)",
        "icon": "👥",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Automatize o controle de comissões e bonificações. Transparência e precisão nos cálculos."
    },
    {
        "title": "Gestão de Negócios - Relatório Borelli",
        "icon": "🚀",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZTY5YmEzZmQtZDVhMS00N2QyLWJhY2QtMDNhMWFmMDRjMjNmIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Eficiência fabril e controle de produção: ciclo produtivo, produtividade e desperdícios."
    },
    {
        "title": "Dashboard Financeiro — Beocean Resort",
        "icon": "💰",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9&pageName=ae6d1828240b25f04e49",
        "desc": "Painel financeiro para hotelaria: fluxo de caixa, receitas por categoria e despesas operacionais."
    }
]

# --- CONTAGEM DINÂMICA ---
total_projetos = len(pbi_projects)

# --- HERO SECTION (SEM ELEMENTOS DECORATIVOS) ---
st.markdown(f"""
<div class="hero-wrapper">
    <h1 class="hero-title">
        Dashboards que transformam <span class="accent">dados em decisões</span>
    </h1>
    <p class="hero-subtitle">
        Inteligência de negócios aplicada — visualizações estratégicas para gestores que exigem resultado.
    </p>
    <div class="hero-container">
        <div class="hero-container-title">Decisões de Elite exigem Experiência Real</div>
        <div class="hero-container-text">
            <p><strong style="color:#e2e8f0;">A Lógica do Sucesso:</strong></p>
            <ol>
                <li>Resultados extraordinários só são alcançados através de <span class="hero-highlight">metodologias validadas pelo tempo</span>.</li>
                <li>Minha consultoria e mentoria sintetizam <span class="hero-highlight">+20 anos de campo</span> em estratégias aplicáveis.</li>
                <li><strong style="color:#e2e8f0;">Logo,</strong> acelerar sua curva de aprendizado e seus lucros comigo não é uma opção, é a <span class="hero-highlight">consequência lógica da excelência.</span></li>
            </ol>
            <p>Não busque apenas dashboards. Busque a inteligência por trás deles.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- SEARCH ---
st.markdown(
    "<p class='search-label'>🔍 Filtre os painéis pelo nome ou descrição</p>",
    unsafe_allow_html=True
)

col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
with col_s2:
    search_query = st.text_input(
        label="Pesquisar dashboard",
        placeholder="Ex: financeiro, RH, Stone...",
        key="search_pbi",
        label_visibility="collapsed"
    )

# --- FILTRO DE PESQUISA ---
if search_query:
    filtered_projects = [
        p for p in pbi_projects
        if search_query.lower() in p["title"].lower() or search_query.lower() in p["desc"].lower()
    ]
    total_resultados = len(filtered_projects)
    label = "resultado" if total_resultados == 1 else "resultados"
    st.markdown(
        f"<div class='search-result-count'>🔎 <span>{total_resultados}</span> {label} para <span>\"{search_query}\"</span></div>",
        unsafe_allow_html=True
    )
else:
    filtered_projects = pbi_projects

# --- MENSAGEM QUANDO NÃO HÁ RESULTADOS ---
if not filtered_projects:
    st.markdown(
        """
        <div class="empty-state">
            <div class="empty-state-icon">🔍</div>
            <div class="empty-state-title">Nenhum dashboard encontrado.</div>
            <div class="empty-state-sub">Tente outro termo de pesquisa.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- RENDERIZAÇÃO DOS CARDS (SEM FLIP) ---
if filtered_projects:
    for i in range(0, len(filtered_projects), 3):
        cols = st.columns(3)
        for j in range(3):
            idx = i + j
            if idx < len(filtered_projects):
                p = filtered_projects[idx]
                
                wa_text = f"{p['title']} - que vi no seu portfólio.\n\n💡 {p['desc']}\n\n🔗 Link: {p['url']}"
                wa_link = f"https://wa.me/?text={urllib.parse.quote(wa_text)}"
                li_link = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(p['url'])}"
                
                with cols[j]:
                    st.markdown(f"""
                    <div class="card">
                        <div class="card-icon">{p['icon']}</div>
                        <div class="pbi-card-title">{p['title']}</div>
                        <div class="pbi-card-tag">PROJETO</div>
                        <div class="pbi-description">{p['desc']}</div>
                        <a href="{p['url']}" target="_blank" class="btn-acessar">
                            Abrir Dashboard →
                        </a>
                        <div class="share-container">
                            <span class="share-label">Falar com Rodrigo:</span>
                            <a href="{li_link}" target="_blank" class="share-icon icon-li">
                                <i class="fab fa-linkedin"></i>
                            </a>
                            <a href="{wa_link}" target="_blank" class="share-icon icon-wa">
                                <i class="fab fa-whatsapp"></i>
                            </a>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

exibir_rodape()
