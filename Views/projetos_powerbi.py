import streamlit as st
import urllib.parse
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# ══════════════════════════════════════════════
#  DADOS — dashboards organizados por categoria
# ══════════════════════════════════════════════
CATEGORIES = [
    {
        "id": "financeiro",
        "label": "Financeiro",
        "icon": "💹",
        "color": "#10b981",   # emerald
        "desc": "DRE, fluxo de caixa e rentabilidade",
        "projects": [
            {
                "title": "DRE Estratégico — Análise Financeira",
                "tag": "Análise Vertical & Horizontal",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiOWE0ZmU3ZTMtYzAyYi00NDE1LTg3YWItYjcxZTE2ZWI2OWRjIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9&disablecdnExpiration=1766386882",
                "desc": "Acompanhamento do DRE com análise vertical e horizontal integradas. Avalie margens, rentabilidade e tendências — tudo em um único painel para decisões financeiras rápidas e precisas.",
                "kpis": ["Margem Líquida", "EBITDA", "Análise H/V"],
            },
            {
                "title": "Dashboard Financeiro — Beocean Resort",
                "tag": "Hotelaria",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9&pageName=ae6d1828240b25f04e49",
                "desc": "Painel financeiro especializado para hotelaria: fluxo de caixa, receitas por categoria e despesas operacionais. Maximize rentabilidade com dados que chegam antes das decisões.",
                "kpis": ["Fluxo de Caixa", "RevPAR", "Custos Operacionais"],
            },
            {
                "title": "Relatório STONE",
                "tag": "Faturamento B2B",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
                "desc": "Monitoramento de faturamento B2B com KPIs como Margem de Contribuição e Ticket Médio. Análise granular por região e evolução mensal para tomada de decisão assertiva.",
                "kpis": ["Ticket Médio", "Margem Contrib.", "Evolução Mensal"],
            },
        ],
    },
    {
        "id": "operacoes",
        "label": "Operações & Indústria",
        "icon": "⚙️",
        "color": "#f59e0b",   # amber
        "desc": "OEE, produção e logística",
        "projects": [
            {
                "title": "Dashboard OEE — Eficiência Industrial",
                "tag": "Chão de Fábrica",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiM2YxN2NhZmQtMTg4My00YTgwLWJhOGQtZmRkNGZkNTM1ZDM0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
                "desc": "Disponibilidade, desempenho e qualidade da produção em um único painel. Identifique gargalos, reduza perdas e aumente produtividade com dados em tempo real.",
                "kpis": ["Disponibilidade", "Performance", "Qualidade (OEE)"],
            },
            {
                "title": "Dashboard Transporte — Travel Company",
                "tag": "Logística",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiNjY5NThlNjctZWY1Ny00YjA0LTk0MjEtNzhiNjgzZjdjZjA2IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
                "desc": "Indicadores de performance logística para otimizar toda a cadeia de transportes. Reduza lead time, corte custos operacionais e eleve a satisfação dos clientes com dados precisos.",
                "kpis": ["Lead Time", "Custo/KM", "SLA de Entrega"],
            },
            {
                "title": "Controle de Pedidos BNZ",
                "tag": "Estoque & Supply",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiZDZlNzViNzMtODllZS00OTVlLWI4MWQtNzBhZmU5ZTkxY2E0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
                "desc": "Gestão de estoque inteligente com níveis de inventário, giro de produtos e status de pedidos em tempo real. Previna rupturas e otimize a logística de abastecimento.",
                "kpis": ["Giro de Estoque", "Rupturas", "Status Pedidos"],
            },
            {
                "title": "Gestão de Negócios — Relatório Borelli",
                "tag": "Produção Industrial",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiZTY5YmEzZmQtZDVhMS00N2QyLWJhY2QtMDNhMWFmMDRjMjNmIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
                "desc": "Controle completo do ciclo produtivo: produtividade, desperdícios e capacidade. Painel desenvolvido para gestores que precisam reduzir custos operacionais com base em dados.",
                "kpis": ["Ciclo Produtivo", "Desperdícios", "Ocupação"],
            },
        ],
    },
    {
        "id": "vendas",
        "label": "Vendas & Comercial",
        "icon": "📈",
        "color": "#6366f1",   # indigo
        "desc": "Metas, pipeline e performance comercial",
        "projects": [
            {
                "title": "Vendas — Meta vs Realizado",
                "tag": "Performance Comercial",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
                "desc": "Acompanhe o funil de vendas, tempo de fechamento e eficiência por canal. Compare planejado vs realizado e corrija o rumo antes do fim do período.",
                "kpis": ["Funil de Vendas", "% Meta", "Tempo de Fechamento"],
            },
            {
                "title": "Análise de Dados Estratégica",
                "tag": "Alta Gestão",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
                "desc": "Painel de alta gestão com controle rigoroso de metas e performance de vendas. Compare planejado vs realizado e ajuste táticas com agilidade.",
                "kpis": ["KPIs Estratégicos", "Tendências", "Variância"],
            },
        ],
    },
    {
        "id": "rh",
        "label": "RH & People Analytics",
        "icon": "👥",
        "color": "#ec4899",   # pink
        "desc": "Pessoas, contratações e comissões",
        "projects": [
            {
                "title": "People Analytics",
                "tag": "Gestão de Pessoas",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
                "desc": "Automatize o controle de comissões e bonificações. Transparência e precisão nos cálculos, com correlação direta entre desempenho individual e pagamentos realizados.",
                "kpis": ["Turnover", "Headcount", "Comissões"],
            },
            {
                "title": "Monitoramento de Vagas — Bradesco",
                "tag": "Recrutamento & Seleção",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiMjQxN2Q4NGYtNWRmNy00NWVjLWE4YmQtNWMyNWYwNGYyZDUzIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
                "desc": "Visão consolidada de vagas por área, localização e perfil buscado. Identifique tendências de contratação e apoie decisões estratégicas de recrutamento em larga escala.",
                "kpis": ["Vagas Ativas", "Time-to-Hire", "Candidatos/Vaga"],
            },
        ],
    },
    {
        "id": "setor_publico",
        "label": "Setor Público & Regulatório",
        "icon": "🏛️",
        "color": "#14b8a6",   # teal
        "desc": "Transparência, regulação e indicadores governamentais",
        "projects": [
            {
                "title": "Portal da Transparência — Ilhéus",
                "tag": "Gestão Municipal",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiYTM2ZWFlM2QtOTc2NC00NDQ2LTg2ZTctOGY5Nzc4YTk2YWM1IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
                "desc": "Dados públicos de Ilhéus em informação clara e acessível. Acompanhe receitas, despesas e indicadores em tempo real, fortalecendo o controle social e a accountability.",
                "kpis": ["Receitas", "Despesas", "Indicadores Sociais"],
            },
            {
                "title": "ANATEL — Indicadores de Reclamações",
                "tag": "Regulação Telecom",
                "url": "https://app.powerbi.com/view?r=eyJrIjoiZjgwNmViZjMtYTQ3OS00ZjljLWFiZjktOTNlNzJhYWQ2MzZkIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
                "desc": "Monitoramento dos indicadores da ANATEL com análise de tendências e gargalos. Tome decisões mais assertivas para melhorar a qualidade do atendimento ao consumidor.",
                "kpis": ["Volume de Reclamações", "Índice de Resolução", "Tendências"],
            },
        ],
    },
]

# Flatten para busca global
ALL_PROJECTS = []
for cat in CATEGORIES:
    for p in cat["projects"]:
        ALL_PROJECTS.append({**p, "category": cat["label"], "cat_color": cat["color"], "cat_icon": cat["icon"]})

TOTAL = len(ALL_PROJECTS)

# ══════════════════════════════════════════════
#  CSS
# ══════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Bricolage+Grotesque:wght@400;600;700;800&display=swap');
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > section,
.main { background: #07080f !important; }

[data-testid="stHeader"] { background: transparent !important; }

[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(ellipse 70% 45% at 50% 0%, rgba(99,102,241,0.09) 0%, transparent 65%),
        radial-gradient(ellipse 50% 35% at 85% 40%, rgba(16,185,129,0.05) 0%, transparent 55%);
}

.block-container {
    max-width: 1240px !important;
    padding: 0 2.5rem 4rem !important;
    margin: 0 auto !important;
}

[data-testid="stMarkdownContainer"] { width: 100% !important; }

/* ── TIPOGRAFIA GLOBAL ── */
.main *, .main p, .main a, .main li, .main span, .main div {
    font-family: 'Inter', sans-serif !important;
}

/* ── TOP BANNER (urgência silenciosa) ── */
.top-banner {
    background: linear-gradient(90deg, rgba(99,102,241,0.15) 0%, rgba(16,185,129,0.1) 100%);
    border-bottom: 1px solid rgba(99,102,241,0.2);
    text-align: center;
    padding: 10px 20px;
    font-size: 0.82rem;
    color: #a5b4fc;
    letter-spacing: 0.3px;
    width: 100vw;
    margin-left: calc(-50vw + 50%);
}

.top-banner strong { color: #c7d2fe; font-weight: 600; }

/* ── HERO ── */
.hero {
    padding: 80px 0 56px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    position: relative;
}

.hero-eyebrow {
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #818cf8;
    margin-bottom: 22px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.hero-eyebrow::before, .hero-eyebrow::after {
    content: '';
    display: block;
    width: 32px;
    height: 1px;
    background: rgba(129,140,248,0.4);
}

.hero-h1 {
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: clamp(2.6rem, 5.5vw, 4.2rem);
    font-weight: 800;
    line-height: 1.08;
    letter-spacing: -2px;
    color: #eef2ff;
    max-width: 780px;
    margin-bottom: 22px;
}

.hero-h1 em {
    font-style: normal;
    background: linear-gradient(135deg, #818cf8 0%, #a78bfa 50%, #c4b5fd 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    font-size: 1.05rem;
    font-weight: 300;
    color: #64748b;
    max-width: 520px;
    line-height: 1.75;
    margin-bottom: 44px;
}

/* ── STATS ROW ── */
.stats-row {
    display: flex;
    gap: 0;
    border: 1px solid rgba(99,102,241,0.18);
    border-radius: 16px;
    overflow: hidden;
    background: rgba(15,17,30,0.7);
    backdrop-filter: blur(10px);
    margin-bottom: 64px;
}

.stat-cell {
    flex: 1;
    padding: 24px 36px;
    text-align: center;
    border-right: 1px solid rgba(99,102,241,0.12);
}

.stat-cell:last-child { border-right: none; }

.stat-num {
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 2.2rem;
    font-weight: 800;
    color: #818cf8;
    line-height: 1;
    display: block;
}

.stat-lbl {
    font-size: 0.72rem;
    color: #374151;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 6px;
    display: block;
}

/* ── HERO CTA BUTTONS ── */
.hero-ctas {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 56px;
}

.btn-primary {
    background: #6366f1;
    color: #fff !important;
    text-decoration: none !important;
    padding: 13px 28px;
    border-radius: 12px;
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.3px;
    transition: all 0.2s ease;
    border: none;
    cursor: pointer;
    display: inline-block;
}

.btn-primary:hover {
    background: #4f46e5;
    transform: translateY(-1px);
    box-shadow: 0 8px 24px rgba(99,102,241,0.35);
}

.btn-ghost {
    background: transparent;
    color: #6366f1 !important;
    text-decoration: none !important;
    padding: 13px 28px;
    border-radius: 12px;
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-weight: 700;
    font-size: 0.9rem;
    letter-spacing: 0.3px;
    transition: all 0.2s ease;
    border: 1.5px solid rgba(99,102,241,0.4);
    display: inline-block;
}

.btn-ghost:hover {
    border-color: rgba(99,102,241,0.8);
    background: rgba(99,102,241,0.06);
}

/* ── MANIFESTO / SILOGISMO ── */
.manifesto {
    background: rgba(15,17,30,0.6);
    border: 1px solid rgba(99,102,241,0.15);
    border-left: 3px solid #6366f1;
    border-radius: 16px;
    padding: 40px 48px;
    max-width: 860px;
    width: 100%;
    margin: 0 auto 72px;
    text-align: left;
    position: relative;
    overflow: hidden;
}

.manifesto::after {
    content: '"';
    position: absolute;
    right: 32px;
    top: -10px;
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 8rem;
    color: rgba(99,102,241,0.05);
    line-height: 1;
    pointer-events: none;
}

.manifesto-title {
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 1.3rem;
    font-weight: 800;
    color: #eef2ff;
    margin-bottom: 20px;
    letter-spacing: -0.5px;
}

.manifesto-body {
    font-size: 0.95rem;
    color: #64748b;
    line-height: 1.8;
}

.manifesto-body ol {
    padding-left: 22px;
    margin: 16px 0;
}

.manifesto-body li {
    margin-bottom: 12px;
    color: #64748b;
}

.manifesto-body strong { color: #e2e8f0; font-weight: 600; }
.hl { color: #818cf8; font-weight: 600; }

/* ── SEARCH ── */
.search-wrap {
    text-align: center;
    margin-bottom: 12px;
}

.search-hint {
    font-size: 0.8rem;
    color: #374151;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
}

div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.03) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(99,102,241,0.22) !important;
    border-radius: 14px !important;
    padding: 14px 22px !important;
    font-size: 0.95rem !important;
    font-family: 'Inter', sans-serif !important;
    transition: all 0.25s ease !important;
}
div[data-testid="stTextInput"] input::placeholder { color: #1f2937 !important; }
div[data-testid="stTextInput"] input:focus {
    box-shadow: 0 0 0 3px rgba(99,102,241,0.18) !important;
    border-color: rgba(99,102,241,0.55) !important;
    background: rgba(99,102,241,0.04) !important;
    outline: none !important;
}

.result-count {
    text-align: center;
    color: #374151;
    font-size: 0.85rem;
    margin: 12px 0 32px;
}
.result-count span { color: #818cf8; font-weight: 600; }

/* ── CATEGORY HEADER ── */
.cat-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin: 56px 0 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}

.cat-icon-wrap {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
}

.cat-title {
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 1.25rem;
    font-weight: 700;
    color: #eef2ff;
    letter-spacing: -0.5px;
}

.cat-subtitle {
    font-size: 0.8rem;
    color: #374151;
    margin-top: 2px;
}

.cat-count {
    margin-left: auto;
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 4px 12px;
    border-radius: 100px;
}

/* ── PROJECT CARD ── */
.pcard {
    background: rgba(15,17,30,0.7);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 18px;
    padding: 28px;
    height: 100%;
    display: flex;
    flex-direction: column;
    transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
    position: relative;
    overflow: hidden;
}

.pcard::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--accent, #6366f1);
    opacity: 0;
    transition: opacity 0.25s ease;
}

.pcard:hover {
    border-color: rgba(99,102,241,0.25);
    transform: translateY(-3px);
    box-shadow: 0 16px 40px rgba(0,0,0,0.35);
}

.pcard:hover::before { opacity: 1; }

.pcard-tag {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 100px;
    display: inline-block;
    margin-bottom: 14px;
    width: fit-content;
}

.pcard-title {
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 1rem;
    font-weight: 700;
    color: #eef2ff;
    line-height: 1.35;
    margin-bottom: 12px;
    letter-spacing: -0.3px;
}

.pcard-desc {
    font-size: 0.85rem;
    color: #4b5563;
    line-height: 1.65;
    flex: 1;
    margin-bottom: 20px;
}

/* KPIs chips */
.kpis-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 20px;
}

.kpi-chip {
    font-size: 0.7rem;
    font-weight: 500;
    color: #374151;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    padding: 3px 9px;
    border-radius: 6px;
}

/* Card footer */
.pcard-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: auto;
    padding-top: 16px;
    border-top: 1px solid rgba(255,255,255,0.05);
}

.pcard-open {
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 0.8rem;
    font-weight: 700;
    color: #818cf8 !important;
    text-decoration: none !important;
    letter-spacing: 0.3px;
    transition: color 0.2s ease;
    display: flex;
    align-items: center;
    gap: 6px;
}

.pcard-open:hover { color: #c7d2fe !important; }

.pcard-share {
    display: flex;
    gap: 10px;
}

.share-btn {
    color: #1f2937 !important;
    font-size: 1rem;
    text-decoration: none !important;
    transition: color 0.2s ease, transform 0.2s ease;
}
.share-btn:hover { transform: scale(1.2); }
.share-li:hover { color: #93c5fd !important; }
.share-wa:hover { color: #4ade80 !important; }

/* ── EMPTY STATE ── */
.empty {
    text-align: center;
    padding: 80px 20px;
}
.empty-icon { font-size: 2.5rem; margin-bottom: 14px; opacity: 0.3; }
.empty-title {
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 1rem;
    font-weight: 700;
    color: #374151;
    margin-bottom: 6px;
}
.empty-sub { font-size: 0.85rem; color: #1f2937; }

/* ── CTA BOTTOM ── */
.cta-bottom {
    margin: 80px 0 0;
    background: linear-gradient(135deg, rgba(99,102,241,0.08) 0%, rgba(16,185,129,0.06) 100%);
    border: 1px solid rgba(99,102,241,0.18);
    border-radius: 24px;
    padding: 56px 48px;
    text-align: center;
}

.cta-bottom-title {
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: clamp(1.6rem, 3vw, 2.4rem);
    font-weight: 800;
    color: #eef2ff;
    letter-spacing: -1px;
    margin-bottom: 14px;
}

.cta-bottom-sub {
    font-size: 1rem;
    color: #4b5563;
    max-width: 520px;
    margin: 0 auto 36px;
    line-height: 1.7;
}

.cta-badges {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 28px;
}

.cta-badge {
    font-size: 0.75rem;
    color: #374151;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    padding: 5px 14px;
    border-radius: 100px;
}

/* scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #07080f; }
::-webkit-scrollbar-thumb { background: rgba(99,102,241,0.25); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(99,102,241,0.45); }

/* Animations */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

.pcard { animation: fadeUp 0.5s ease forwards; }

</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
""", unsafe_allow_html=True)


# ── TOP BANNER ──
st.markdown("""
<div class="top-banner">
    <strong>Novo projeto disponível:</strong> Dashboard OEE com análise preditiva de paradas. 
    Rolar para conferir ↓
</div>
""", unsafe_allow_html=True)


# ── HERO ──
st.markdown(f"""
<div class="hero">
    <div class="hero-eyebrow">Portfólio Power BI</div>
    <h1 class="hero-h1">
        Dados que <em>convencem</em> quem decide.
    </h1>
    <p class="hero-sub">
        {TOTAL} dashboards construídos com +20 anos de gestão real — não de teoria. 
        Cada painel resolve um problema de negócio específico.
    </p>

    <div class="hero-ctas">
        <a href="#dashboards" class="btn-primary">Ver todos os dashboards →</a>
        <a href="https://wa.me/5500000000000" target="_blank" class="btn-ghost">Falar com Rodrigo</a>
    </div>

    <div class="stats-row">
        <div class="stat-cell">
            <span class="stat-num">{TOTAL}</span>
            <span class="stat-lbl">Dashboards</span>
        </div>
        <div class="stat-cell">
            <span class="stat-num">+20</span>
            <span class="stat-lbl">Anos de Campo</span>
        </div>
        <div class="stat-cell">
            <span class="stat-num">5</span>
            <span class="stat-lbl">Setores</span>
        </div>
        <div class="stat-cell">
            <span class="stat-num">100%</span>
            <span class="stat-lbl">Estratégico</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ── MANIFESTO ──
st.markdown("""
<div class="manifesto">
    <div class="manifesto-title">Decisões de elite exigem experiência real</div>
    <div class="manifesto-body">
        <p><strong>A lógica por trás de cada dashboard:</strong></p>
        <ol>
            <li>Resultados extraordinários só chegam por <span class="hl">metodologias validadas em campo</span> — não em cursos.</li>
            <li>Cada painel aqui sintetiza <span class="hl">+20 anos de gestão aplicada</span> em estratégia visível e acionável.</li>
            <li><strong>Conclusão:</strong> encurtar sua curva de aprendizado comigo não é uma opção — é a <span class="hl">consequência lógica de escolher excelência</span>.</li>
        </ol>
        <p>Não busque apenas visualizações. Busque a inteligência de negócio por trás delas.</p>
    </div>
</div>
""", unsafe_allow_html=True)


# ── SEARCH ──
st.markdown('<div class="search-wrap"><p class="search-hint">🔍 Pesquise por nome, setor ou KPI</p></div>', unsafe_allow_html=True)
col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    query = st.text_input(
        label="Pesquisar",
        placeholder="Ex: financeiro, OEE, ANATEL, RH...",
        key="search_pbi",
        label_visibility="collapsed"
    )

# ── FILTRO ──
if query:
    q = query.lower()
    filtered_cats = []
    for cat in CATEGORIES:
        matched = [
            p for p in cat["projects"]
            if q in p["title"].lower()
            or q in p["desc"].lower()
            or q in cat["label"].lower()
            or any(q in kpi.lower() for kpi in p["kpis"])
        ]
        if matched:
            filtered_cats.append({**cat, "projects": matched})

    total_found = sum(len(c["projects"]) for c in filtered_cats)
    label = "resultado" if total_found == 1 else "resultados"
    st.markdown(
        f"<div class='result-count'>🔎 <span>{total_found}</span> {label} para <span>\"{query}\"</span></div>",
        unsafe_allow_html=True
    )
else:
    filtered_cats = CATEGORIES

# ── EMPTY STATE ──
if not filtered_cats:
    st.markdown("""
    <div class="empty">
        <div class="empty-icon">🔍</div>
        <div class="empty-title">Nenhum dashboard encontrado.</div>
        <div class="empty-sub">Tente outro termo: financeiro, RH, logística, OEE…</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
#  RENDERIZAÇÃO POR CATEGORIA
# ══════════════════════════════════════════════
for cat in filtered_cats:
    count = len(cat["projects"])
    plural = "dashboard" if count == 1 else "dashboards"
    color = cat["color"]
    # Hex color → rgba light for tag backgrounds
    # We'll pass color via inline style on elements

    st.markdown(f"""
    <div class="cat-header">
        <div class="cat-icon-wrap" style="background: {color}18;">
            <span style="font-size:1.1rem;">{cat['icon']}</span>
        </div>
        <div>
            <div class="cat-title">{cat['label']}</div>
            <div class="cat-subtitle">{cat['desc']}</div>
        </div>
        <div class="cat-count" style="background:{color}15; color:{color}; border: 1px solid {color}30;">
            {count} {plural}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Grid de cards — sempre 3 colunas (cards sozinhos ficam na 1ª coluna)
    projects = cat["projects"]
    for row_start in range(0, len(projects), 3):
        row = projects[row_start:row_start + 3]
        cols = st.columns(3)

        for ci, proj in enumerate(row):
            wa_text = f"Olá Rodrigo! Vi o *{proj['title']}* no seu portfólio e quero saber mais.\n\n{proj['desc']}\n\n🔗 {proj['url']}"
            wa_link = f"https://wa.me/?text={urllib.parse.quote(wa_text)}"
            li_link = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(proj['url'])}"

            kpis_html = "".join(f'<span class="kpi-chip">{k}</span>' for k in proj["kpis"])

            with cols[ci]:
                st.markdown(f"""
                <div class="pcard" style="--accent: {color};">
                    <span class="pcard-tag" style="background:{color}15; color:{color}; border:1px solid {color}25;">
                        {proj['tag']}
                    </span>
                    <div class="pcard-title">{proj['title']}</div>
                    <div class="pcard-desc">{proj['desc']}</div>
                    <div class="kpis-row">{kpis_html}</div>
                    <div class="pcard-footer">
                        <a href="{proj['url']}" target="_blank" class="pcard-open">
                            Abrir painel <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:0.72rem;"></i>
                        </a>
                        <div class="pcard-share">
                            <a href="{li_link}" target="_blank" class="share-btn share-li" title="Compartilhar no LinkedIn">
                                <i class="fab fa-linkedin"></i>
                            </a>
                            <a href="{wa_link}" target="_blank" class="share-btn share-wa" title="Compartilhar no WhatsApp">
                                <i class="fab fa-whatsapp"></i>
                            </a>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)


# ── CTA BOTTOM ──
st.markdown("""
<div class="cta-bottom">
    <div class="cta-bottom-title">Seu próximo dashboard começa aqui.</div>
    <p class="cta-bottom-sub">
        +20 anos de experiência em gestão e inteligência de dados. 
        Vamos transformar os seus números em vantagem competitiva real?
    </p>
    <div class="hero-ctas" style="justify-content:center;">
        <a href="https://wa.me/5500000000000" target="_blank" class="btn-primary">
            Solicitar uma consultoria gratuita →
        </a>
        <a href="https://www.linkedin.com/in/rodrigo" target="_blank" class="btn-ghost">
            Conectar no LinkedIn
        </a>
    </div>
    <div class="cta-badges">
        <span class="cta-badge">✓ Resposta em até 24h</span>
        <span class="cta-badge">✓ Primeira reunião sem compromisso</span>
        <span class="cta-badge">✓ Metodologia validada em +20 anos</span>
        <span class="cta-badge">✓ Power BI · Python · SQL</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

exibir_rodape()
