import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --------------------------------------------------
# REGISTRO DE ACESSO
# --------------------------------------------------
registrar_acesso("Projetos Python")

# --------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------
st.set_page_config(
    page_title="Projetos em Python | Rodrigo Aiosa",
    page_icon="🐍",
    layout="wide"
)

# --------------------------------------------------
# ESTILO LANDING PAGE
# --------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(0,180,216,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(0,100,180,0.07) 0%, transparent 50%);
}

[data-testid="stHeader"] { background: transparent !important; }



/* Aplica fonte customizada apenas no conteúdo principal, nunca na sidebar */
.main h1, .main h2, .main h3, .main h4,
.main p, .main a, .main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}

/* Garante que ícones Material do Streamlit não sejam afetados */
.material-symbols-rounded,
.material-icons,
[data-testid*="Collapse"] span,
[data-testid*="collapse"] span {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
}

/* ── FORÇA CENTRALIZAÇÃO NO CONTAINER DO STREAMLIT ── */
[data-testid="stMarkdownContainer"] {
    width: 100% !important;
}

.block-container {
    max-width: 100% !important;
    padding-left: 4rem !important;
    padding-right: 4rem !important;
}

/* ── HERO ── */
.hero-wrapper {
    text-align: center;
    padding: 80px 20px 50px;
    position: relative;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.hero-badge {
    display: inline-block;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00b4d8;
    border: 1px solid rgba(0,180,216,0.35);
    background: rgba(0,180,216,0.07);
    padding: 6px 18px;
    border-radius: 100px;
    margin-bottom: 28px;
}

.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2.4rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -1.5px;
    color: #f0f4ff;
    margin: 0 auto 20px;
    max-width: 720px;
    text-align: center;
}

.hero-title .accent {
    background: linear-gradient(135deg, #00b4d8 0%, #48cae4 50%, #90e0ef 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 1.05rem;
    font-weight: 300;
    color: #7b8ba8;
    max-width: 560px;
    margin: 0 auto 48px;
    line-height: 1.7;
    text-align: center;
}

.hero-stats {
    display: flex;
    justify-content: center;
    gap: 48px;
    flex-wrap: wrap;
    margin-bottom: 60px;
}

.hero-stat {
    text-align: center;
}

.hero-stat-number {
    font-family: 'Syne', sans-serif !important;
    font-size: 2rem;
    font-weight: 800;
    color: #00b4d8;
    display: block;
    line-height: 1;
}

.hero-stat-label {
    font-size: 0.78rem;
    color: #4a5568;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 6px;
    display: block;
}

.hero-divider {
    width: 100%;
    max-width: 900px;
    margin: 0 auto 60px;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.3), transparent);
}

/* ── SEARCH ── */
.search-label {
    text-align: center;
    font-size: 0.85rem;
    color: #4a5568;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
}

div[data-testid="stTextInput"] input {
    background-color: rgba(255,255,255,0.03) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(0,180,216,0.25) !important;
    border-radius: 14px !important;
    padding: 14px 22px !important;
    font-size: 0.95rem !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stTextInput"] input::placeholder {
    color: #2d3748 !important;
}
div[data-testid="stTextInput"] input:focus {
    box-shadow: 0 0 0 3px rgba(0,180,216,0.15) !important;
    border-color: rgba(0,180,216,0.6) !important;
    background-color: rgba(0,180,216,0.04) !important;
}

.search-result-count {
    text-align: center;
    color: #4a5568;
    font-size: 0.88rem;
    margin: 14px 0 28px;
}
.search-result-count span {
    color: #00b4d8;
    font-weight: 600;
}

/* ── SECTION LABEL ── */
.section-label {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #2d3748;
    margin-bottom: 32px;
    text-align: center;
}

/* ── PROJECT CARDS ── */
.project-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    padding: 30px 32px;
    border-radius: 20px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.05);
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.4), transparent);
    opacity: 0;
    transition: opacity 0.35s ease;
}

.project-card:hover {
    transform: translateY(-4px);
    border-color: rgba(0,180,216,0.2);
    box-shadow:
        0 20px 40px rgba(0,0,0,0.4),
        0 0 0 1px rgba(0,180,216,0.1),
        inset 0 1px 0 rgba(0,180,216,0.1);
    background: linear-gradient(145deg, rgba(0,180,216,0.04) 0%, rgba(0,0,0,0.25) 100%);
}

.project-card:hover::before {
    opacity: 1;
}

.project-card-inner {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 24px;
}

.project-card-content {
    flex: 1;
}

.project-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 10px;
    line-height: 1.35;
    letter-spacing: -0.3px;
}

.project-description {
    color: #4a5568;
    font-size: 0.9rem;
    font-weight: 300;
    line-height: 1.65;
    margin: 0;
}

.project-btn-wrap {
    flex-shrink: 0;
    display: flex;
    align-items: center;
}

.project-button {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(0,180,216,0.1);
    color: #00b4d8 !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700;
    font-size: 0.82rem;
    letter-spacing: 0.5px;
    padding: 11px 20px;
    border-radius: 12px;
    text-decoration: none !important;
    border: 1px solid rgba(0,180,216,0.25);
    white-space: nowrap;
    transition: all 0.3s ease;
}

.project-button:hover {
    background: rgba(0,180,216,0.18);
    border-color: rgba(0,180,216,0.5);
    transform: translateX(3px);
    box-shadow: 0 4px 20px rgba(0,180,216,0.2);
}

.project-button .arrow {
    font-size: 1rem;
    transition: transform 0.3s ease;
}

.project-button:hover .arrow {
    transform: translateX(3px);
}

/* ── EMPTY STATE ── */
.empty-state {
    text-align: center;
    padding: 80px 20px;
    color: #2d3748;
}
.empty-state-icon {
    font-size: 3rem;
    margin-bottom: 16px;
    opacity: 0.5;
}
.empty-state-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem;
    font-weight: 700;
    color: #2d3748;
    margin-bottom: 8px;
}
.empty-state-sub {
    font-size: 0.88rem;
    color: #1a202c;
}

/* ── FOOTER SPACER ── */
.footer-spacer {
    height: 60px;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #060912; }
::-webkit-scrollbar-thumb { background: rgba(0,180,216,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0,180,216,0.4); }

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HERO
# --------------------------------------------------
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-badge">⚡ Portfólio Python</div>
    <h1 class="hero-title">
        Aplicações que <span class="accent">resolvem problemas</span><br>reais com código
    </h1>
    <p class="hero-subtitle">
        Automação, análise financeira e Business Intelligence — ferramentas construídas para impactar.
    </p>
    <div class="hero-stats">
        <div class="hero-stat">
            <span class="hero-stat-number">11</span>
            <span class="hero-stat-label">Projetos</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">100%</span>
            <span class="hero-stat-label">Open Access</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">∞</span>
            <span class="hero-stat-label">Impacto</span>
        </div>
    </div>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# BARRA DE PESQUISA
# --------------------------------------------------
st.markdown(
    "<p class='search-label'>🔍 Filtre os projetos pelo nome ou descrição</p>",
    unsafe_allow_html=True
)

col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
with col_s2:
    search_query = st.text_input(
        label="Pesquisar projeto",
        placeholder="Ex: ENEM, ROI, mapas...",
        key="search_python",
        label_visibility="collapsed"
    )

st.write("")

# --------------------------------------------------
# LISTA DE PROJETOS
# --------------------------------------------------
python_projects = [

    {
        "title": "📍 População Municipal",
        "desc": "Dados oficiais do IBGE | Tabela SIDRA 6579",
        "url": "https://popualcaoibge.streamlit.app/"
    },
    {
        "title": "💰 Renda por Município - São Paulo",
        "desc": "Dados oficiais do IBGE | PIB per capita e estimativas de renda familiar",
        "url": "https://renda-cidades-sp-ibge.streamlit.app/"
    },
    {
        "title": "🎓 O cursinho que o Brasil não pode pagar — eu construí de graça",
        "desc": "Construí um simulador do ENEM gratuito com Python + Streamlit. E quero te contar por que isso importa",
        "url": "https://enem-simulador.streamlit.app/"
    },
    {
        "title": "🎓 Simulador FUVEST",
        "desc": "Construí um simulador da FUVEST gratuito com Python + Streamlit. E quero te contar por que isso importa.",
        "url": "https://simulador-fuvest.streamlit.app/"
    },
    {
        "title": "✈️ Criei um simulado GRATUITO do ITA com questões reais de 2021 a 2025",
        "desc": "Questões reais, gabarito comentado, cronômetro. Sem cadastro. Sem pagar nada, porque o sonho não pode depender do bolso",
        "url": "https://simulador-ita.streamlit.app/"
    },
    {
        "title": "🚀 BI Data Generator PRO",
        "desc": "Construí uma ferramenta que analisa seu desempenho no ENEM por área, explica cada resposta e aponta onde focar. Open source, gratuito, acessível a qualquer estudante com internet.",
        "url": "https://ai-bidatagenerator.streamlit.app/"
    },
    {
        "title": "🗺️ CrimeMap BR — Segurança Pública",
        "desc": "Dashboard interativo com dados abertos oficiais do Rio de Janeiro. Explore ocorrências criminais por município, tipo e período.",
        "url": "https://rodrigoaiosa-crimemap.hf.space"
    },
    {
        "title": "🦉 Calculadora ROI de Automação",
        "desc": "Ferramenta estratégica para estimar o Retorno sobre Investimento (ROI) de projetos de automação empresarial.",
        "url": "https://roiautomacao.streamlit.app/"
    },
    {
        "title": "💼 APP S.O.S. MULHER",
        "desc": "Aplicação voltada à conscientização e análise de dados relacionados à violência contra a mulher no Brasil.",
        "url": "https://rodrigoaiosa-help-mulher.hf.space"
    },
    {
        "title": "💼 Precificador Profissional para MEI",
        "desc": "Calculadora inteligente de precificação para microempreendedores baseada em custos reais e margem desejada.",
        "url": "https://rodrigoaiosa-precificador-profissional-mei.hf.space"
    },
    {
        "title": "📍 Extrator de Dados - Google Maps",
        "desc": "Ferramenta para extração estruturada de dados públicos do Google Maps para geração de leads.",
        "url": "https://extrator-de-dados-gm.streamlit.app/"
    },
]

# --------------------------------------------------
# FILTRO DE PESQUISA
# --------------------------------------------------
if search_query:
    filtered_projects = [
        p for p in python_projects
        if search_query.lower() in p["title"].lower() or search_query.lower() in p["desc"].lower()
    ]
    total = len(filtered_projects)
    label = "resultado" if total == 1 else "resultados"
    st.markdown(
        f"<div class='search-result-count'>🔎 <span>{total}</span> {label} para <span>\"{search_query}\"</span></div>",
        unsafe_allow_html=True
    )
else:
    filtered_projects = python_projects

# --------------------------------------------------
# MENSAGEM QUANDO NÃO HÁ RESULTADOS
# --------------------------------------------------
if not filtered_projects:
    st.markdown(
        """
        <div class="empty-state">
            <div class="empty-state-icon">🔍</div>
            <div class="empty-state-title">Nenhum projeto encontrado.</div>
            <div class="empty-state-sub">Tente outro termo de pesquisa.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# SECTION LABEL
# --------------------------------------------------
if filtered_projects:
    st.markdown('<div class="section-label">— Projetos em destaque —</div>', unsafe_allow_html=True)

# --------------------------------------------------
# RENDERIZAÇÃO DOS CARDS
# --------------------------------------------------
for p in filtered_projects:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-card-inner">
            <div class="project-card-content">
                <div class="project-title">{p['title']}</div>
                <p class="project-description">{p['desc']}</p>
            </div>
            <div class="project-btn-wrap">
                <a href="{p['url']}" target="_blank" class="project-button">
                    Abrir <span class="arrow">→</span>
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

exibir_rodape()
