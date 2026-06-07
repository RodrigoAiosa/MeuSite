import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- ESTILO LANDING PAGE ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

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

/* Centralização do container */
[data-testid="stMarkdownContainer"] { width: 100% !important; }
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

.hero-stat { text-align: center; }

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

/* ── SILOGISMO / HERO CARD ── */
.hero-container {
    background: linear-gradient(135deg, rgba(17,24,39,0.8) 0%, rgba(15,23,42,0.9) 100%);
    padding: 40px 48px;
    border-radius: 20px;
    border-left: 3px solid #00b4d8;
    margin-bottom: 60px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.4), inset 0 1px 0 rgba(0,180,216,0.1);
    max-width: 860px;
    width: 100%;
    text-align: left;
}

.hero-container-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.4rem;
    font-weight: 800;
    color: #f0f4ff;
    margin-bottom: 20px;
    letter-spacing: -0.3px;
}

.hero-container-text {
    font-size: 0.95rem;
    color: #7b8ba8;
    line-height: 1.75;
}

.hero-container-text ol {
    padding-left: 20px;
    margin: 12px 0;
}

.hero-container-text li {
    margin-bottom: 10px;
}

.hero-container-text p {
    margin: 8px 0;
}

.hero-highlight {
    color: #00b4d8;
    font-weight: 600;
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
div[data-testid="stTextInput"] input::placeholder { color: #2d3748 !important; }
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

/* ── FLIP CARDS ── */
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
    to   { opacity: 1; transform: translateY(0); }
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
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 28px;
}

.flip-card-front {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.25) 100%);
    border: 1px solid rgba(255,255,255,0.05);
    color: #f0f4ff;
}

.flip-card-back {
    background: linear-gradient(145deg, rgba(0,180,216,0.06) 0%, rgba(6,9,18,0.95) 100%);
    border: 1px solid rgba(0,180,216,0.3);
    color: #f0f4ff;
    transform: rotateY(180deg);
    overflow: hidden;
    box-shadow: 0 0 30px rgba(0,180,216,0.1);
}

.pbi-description {
    font-size: 0.88rem;
    color: #7b8ba8;
    line-height: 1.55;
    margin-bottom: 18px;
    opacity: 0;
    transform: translateY(20px);
    transition: all 0.5s ease-in-out;
    transition-delay: 0.3s;
}
.flip-card:hover .pbi-description {
    opacity: 1;
    transform: translateY(0);
}

.card-icon { font-size: 56px; margin-bottom: 18px; }

.pbi-card-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.15rem;
    font-weight: 700;
    color: #f0f4ff;
    margin-bottom: 16px;
    letter-spacing: -0.3px;
    line-height: 1.3;
}

.pbi-card-tag {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    background: rgba(0,180,216,0.1);
    color: #00b4d8;
    padding: 5px 14px;
    border-radius: 100px;
    border: 1px solid rgba(0,180,216,0.2);
}

.btn-acessar {
    background: rgba(0,180,216,0.12);
    color: #00b4d8 !important;
    padding: 10px 22px;
    border-radius: 12px;
    text-decoration: none !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700;
    font-size: 0.82rem;
    letter-spacing: 0.5px;
    display: inline-block;
    border: 1px solid rgba(0,180,216,0.3);
    opacity: 0;
    transition: all 0.4s ease;
    transition-delay: 0.45s;
}
.flip-card:hover .btn-acessar {
    opacity: 1;
}
.btn-acessar:hover {
    background: rgba(0,180,216,0.22);
    border-color: rgba(0,180,216,0.6);
}

.share-container {
    display: flex;
    gap: 16px;
    margin-top: 12px;
    align-items: center;
    justify-content: center;
}

.share-label {
    font-size: 0.75rem;
    color: #4a5568;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 14px;
}

.share-icon {
    color: #4a5568;
    font-size: 1.3rem;
    transition: all 0.3s ease;
    text-decoration: none;
}
.share-icon:hover { transform: scale(1.2); }
.icon-li:hover { color: #0077b5; }
.icon-wa:hover { color: #25d366; }

/* ── EMPTY STATE ── */
.empty-state {
    text-align: center;
    padding: 80px 20px;
}
.empty-state-icon { font-size: 3rem; margin-bottom: 16px; opacity: 0.4; }
.empty-state-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem;
    font-weight: 700;
    color: #2d3748;
    margin-bottom: 8px;
}
.empty-state-sub { font-size: 0.88rem; color: #1a202c; }

.footer-spacer { height: 60px; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #060912; }
::-webkit-scrollbar-thumb { background: rgba(0,180,216,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0,180,216,0.4); }

</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# ── HERO ──
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-badge">📊 Portfólio Power BI</div>
    <h1 class="hero-title">
        Dashboards que transformam <span class="accent">dados em decisões</span>
    </h1>
    <p class="hero-subtitle">
        Inteligência de negócios aplicada — visualizações estratégicas para gestores que exigem resultado.
    </p>
    <div class="hero-stats">
        <div class="hero-stat">
            <span class="hero-stat-number">11</span>
            <span class="hero-stat-label">Dashboards</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">+20</span>
            <span class="hero-stat-label">Anos de Campo</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">100%</span>
            <span class="hero-stat-label">Estratégico</span>
        </div>
    </div>
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
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# ── SEARCH ──
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

st.write("")

# --- DADOS DOS PROJETOS ---
pbi_projects = [
     {
        "title": "Dashboard OEE",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2YxN2NhZmQtMTg4My00YTgwLWJhOGQtZmRkNGZkNTM1ZDM0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Transforme dados brutos de eficiência industrial em insights claros e estratégicos. Acompanhe a disponibilidade, o desempenho e a qualidade da produção em tempo real, identificando gargalos, reduzindo perdas e aumentando a produtividade do seu chão de fábrica."
    },
    {
        "title": "Portal da Transparência - Ilheus",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTM2ZWFlM2QtOTc2NC00NDQ2LTg2ZTctOGY5Nzc4YTk2YWM1IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Transforma dados públicos de Ilhéus em informação clara e estratégica. Acompanhe receitas, despesas e indicadores em tempo real, fortalecendo o controle social."
    },
    {
        "title": "💹 DRE Estratégico — Análise Financeira",
        "icon": "📊",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiOWE0ZmU3ZTMtYzAyYi00NDE1LTg3YWItYjcxZTE2ZWI2OWRjIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9&disablecdnExpiration=1766386882",
        "desc": "Acompanhamento detalhado do DRE com análises vertical/horizontal. Avalie rentabilidade, margens e tendências para decisões financeiras mais precisas."
    },
    {
        "title": "🏦 Monitoramento de Vagas — Bradesco",
        "icon": "📋",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMjQxN2Q4NGYtNWRmNy00NWVjLWE4YmQtNWMyNWYwNGYyZDUzIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Visão consolidada de vagas Bradesco por área, localização e perfil. Identifique tendências de contratação e apoie decisões estratégicas de recrutamento."
    },
    {
        "title": "💳 Relatório STONE",
        "icon": "🏛️",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Monitoramento de faturamento B2B com KPIs como Margem de Contribuição e Ticket Médio. Análise granular por região e evolução mensal."
    },
    {
        "title": "📊 Vendas Meta vs Realizado",
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Gestão de Recrutamento e Seleção: acompanhe funil, tempo de fechamento e eficiência dos canais. RH preditivo para alcance de metas."
    },
    {
        "title": "📦 Controle de Pedidos BNZ",
        "icon": "📦",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZDZlNzViNzMtODllZS00OTVlLWI4MWQtNzBhZmU5ZTkxY2E0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Gestão de estoque inteligente: níveis de inventário, giro de produtos e status de pedidos em tempo real. Prevenção de rupturas e otimização logística."
    },
    {
        "title": "🎯 Análise Dados Estratégica",
        "icon": "🎯",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Alta gestão: controle rigoroso de metas e performance de vendas. Compare planejado vs realizado e ajuste táticas rapidamente."
    },
    {
        "title": "👥 People Analytics (RH)",
        "icon": "👥",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Automatize o controle de comissões e bonificações. Transparência e precisão nos cálculos, correlacionando desempenho com pagamentos efetuados."
    },
    {
        "title": "🚀 Gestão de Negócios - Relatório Borelli",
        "icon": "🚀",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZTY5YmEzZmQtZDVhMS00N2QyLWJhY2QtMDNhMWFmMDRjMjNmIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Eficiência fabril e controle de produção: ciclo produtivo, produtividade, desperdícios e ocupação de capacidade. Reduza custos operacionais."
    },
    {
        "title": "🏖️ Dashboard Financeiro — Beocean Resort",
        "icon": "💰",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9&pageName=ae6d1828240b25f04e49",
        "desc": "Painel financeiro para hotelaria: fluxo de caixa, receitas por categoria e despesas operacionais. Decisões baseadas em dados para maximizar rentabilidade."
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
        <div class="empty-state">
            <div class="empty-state-icon">🔍</div>
            <div class="empty-state-title">Nenhum dashboard encontrado.</div>
            <div class="empty-state-sub">Tente outro termo de pesquisa.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ── SECTION LABEL ──
if filtered_projects:
    st.markdown('<div class="section-label">— Dashboards em destaque —</div>', unsafe_allow_html=True)

# --- RENDERIZAÇÃO DOS FLIP CARDS ---
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
                            <div style="font-family:'Syne',sans-serif; font-weight:700; font-size:0.7rem; letter-spacing:2px; text-transform:uppercase; color:#00b4d8; margin-bottom:8px;">PROJETO</div>
                            <div class="pbi-description">{p['desc']}</div>
                            <a href="{p['url']}" target="_blank" class="btn-acessar">
                                Abrir Dashboard →
                            </a>
                            <div class="share-label">Falar com Rodrigo:</div>
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

st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

exibir_rodape()
