import streamlit as st
import streamlit.components.v1 as components
import urllib.parse
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- DADOS DOS PROJETOS ---
pbi_projects = [
    {
        "title": "Dashboard Transporte — Travel Company",
        "cat": "operacoes",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiNjY5NThlNjctZWY1Ny00YjA0LTk0MjEtNzhiNjgzZjdjZjA2IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "KPIs logísticos em tempo real — lead time, custos operacionais e satisfação do cliente numa visão única.",
    },
    {
        "title": "ANATEL — Indicadores de Reclamações",
        "cat": "publico",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZjgwNmViZjMtYTQ3OS00ZjljLWFiZjktOTNlNzJhYWQ2MzZkIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Monitoramento de reclamações regulatórias — tendências, gargalos e qualidade do atendimento.",
    },
    {
        "title": "Dashboard OEE",
        "cat": "operacoes",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2YxN2NhZmQtMTg4My00YTgwLWJhOGQtZmRkNGZkNTM1ZDM0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Disponibilidade, desempenho e qualidade industrial em tempo real — identifique gargalos e reduza perdas no chão de fábrica.",
    },
    {
        "title": "Portal da Transparência — Ilhéus",
        "cat": "publico",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTM2ZWFlM2QtOTc2NC00NDQ2LTg2ZTctOGY5Nzc4YTk2YWM1IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Receitas, despesas e indicadores públicos de Ilhéus em linguagem acessível — controle social fortalecido.",
    },
    {
        "title": "DRE Estratégico — Análise Financeira",
        "cat": "financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiOWE0ZmU3ZTMtYzAyYi00NDE1LTg3YWItYjcxZTE2ZWI2OWRjIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9&disablecdnExpiration=1766386882",
        "desc": "Análise vertical e horizontal do DRE — rentabilidade, margens e tendências para decisões financeiras precisas.",
    },
    {
        "title": "Monitoramento de Vagas — Bradesco",
        "cat": "rh",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMjQxN2Q4NGYtNWRmNy00NWVjLWE4YmQtNWMyNWYwNGYyZDUzIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Vagas por área, localização e perfil — tendências de contratação e suporte a decisões estratégicas de recrutamento.",
    },
    {
        "title": "Relatório STONE",
        "cat": "financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Faturamento B2B com Margem de Contribuição e Ticket Médio — análise granular por região e evolução mensal.",
    },
    {
        "title": "Vendas Meta vs Realizado",
        "cat": "rh",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Funil de R&S, tempo de fechamento e eficiência dos canais — gestão de metas com visão preditiva.",
    },
    {
        "title": "Controle de Pedidos BNZ",
        "cat": "varejo",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZDZlNzViNzMtODllZS00OTVlLWI4MWQtNzBhZmU5ZTkxY2E0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Nível de estoque, giro de produtos e status de pedidos — prevenção de rupturas e otimização logística.",
    },
    {
        "title": "Análise Dados Estratégica",
        "cat": "rh",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Controle rigoroso de metas e performance de vendas para alta gestão — planejado vs realizado com ajuste rápido de táticas.",
    },
    {
        "title": "People Analytics (RH)",
        "cat": "rh",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Comissões e bonificações automatizadas — transparência nos cálculos com correlação direta entre desempenho e pagamento.",
    },
    {
        "title": "Gestão de Negócios — Relatório Borelli",
        "cat": "operacoes",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZTY5YmEzZmQtZDVhMS00N2QyLWJhY2QtMDNhMWFmMDRjMjNmIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Ciclo produtivo, produtividade, desperdícios e ocupação de capacidade — redução de custos operacionais baseada em dados.",
    },
    {
        "title": "Dashboard Financeiro — Beocean Resort",
        "cat": "financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9&pageName=ae6d1828240b25f04e49",
        "desc": "Fluxo de caixa, receitas por categoria e despesas operacionais para hotelaria — rentabilidade maximizada com dados em tempo real.",
    },
]

# --- SERIALIZAÇÃO DOS PROJETOS PARA JS ---
def projects_to_js(projects):
    items = []
    for p in projects:
        title = p["title"].replace("'", "\\'")
        desc = p["desc"].replace("'", "\\'")
        url = p["url"].replace("'", "\\'")
        items.append(
            f"{{title:'{title}',cat:'{p['cat']}',url:'{url}',desc:'{desc}'}}"
        )
    return "[" + ",".join(items) + "]"


total_projetos = len(pbi_projects)
projects_json = projects_to_js(pbi_projects)

# --- HTML DO PORTFÓLIO ---
html_content = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,400&display=swap');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
    background: #060912;
    font-family: 'DM Sans', sans-serif;
    color: #e2e8f0;
    min-height: 100vh;
    padding: 0;
}}

/* ── LAYOUT ── */
.page {{
    max-width: 1200px;
    margin: 0 auto;
    padding: 48px 32px 80px;
}}

/* ── HERO ── */
.hero {{
    margin-bottom: 48px;
}}

.hero-top {{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 24px;
    margin-bottom: 28px;
    flex-wrap: wrap;
}}

.hero-badge {{
    display: inline-block;
    font-family: 'Syne', sans-serif;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #00b4d8;
    border: 1px solid rgba(0,180,216,0.3);
    background: rgba(0,180,216,0.07);
    padding: 5px 14px;
    border-radius: 100px;
    margin-bottom: 16px;
    display: block;
    width: fit-content;
}}

.hero-title {{
    font-family: 'Syne', sans-serif;
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -1px;
    color: #f0f4ff;
}}

.hero-title .accent {{
    background: linear-gradient(120deg, #00b4d8, #90e0ef);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}

.hero-subtitle {{
    font-size: 0.95rem;
    color: #4a5568;
    margin-top: 10px;
    line-height: 1.6;
    max-width: 480px;
}}

.hero-stats {{
    display: flex;
    gap: 28px;
    flex-shrink: 0;
    align-items: flex-start;
    padding-top: 4px;
}}

.hero-stat {{ text-align: right; }}

.hero-stat-n {{
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #00b4d8;
    display: block;
    line-height: 1;
}}

.hero-stat-l {{
    font-size: 0.7rem;
    color: #2d3748;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 4px;
    display: block;
}}

/* ── TOOLBAR ── */
.toolbar {{
    display: flex;
    gap: 12px;
    align-items: center;
    flex-wrap: wrap;
    padding: 20px 0;
    border-top: 1px solid rgba(255,255,255,0.04);
    border-bottom: 1px solid rgba(255,255,255,0.04);
    margin-bottom: 28px;
}}

.search-wrap {{
    position: relative;
    flex: 1;
    min-width: 200px;
    max-width: 340px;
}}

.search-wrap i {{
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    color: #2d3748;
    font-size: 0.95rem;
    pointer-events: none;
}}

#pb-search {{
    width: 100%;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    color: #e2e8f0;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    padding: 10px 14px 10px 36px;
    outline: none;
    transition: border-color 0.2s, background 0.2s;
}}

#pb-search::placeholder {{ color: #2d3748; }}

#pb-search:focus {{
    border-color: rgba(0,180,216,0.4);
    background: rgba(0,180,216,0.04);
}}

/* ── FILTROS ── */
.filters {{
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
    flex: 1;
}}

.filter-btn {{
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem;
    font-weight: 500;
    padding: 7px 14px;
    border-radius: 100px;
    border: 1px solid rgba(255,255,255,0.07);
    background: transparent;
    color: #4a5568;
    cursor: pointer;
    transition: all 0.18s;
    display: flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
}}

.filter-btn:hover {{ color: #7b8ba8; border-color: rgba(255,255,255,0.12); }}

.filter-btn.active {{
    background: rgba(0,180,216,0.1);
    color: #00b4d8;
    border-color: rgba(0,180,216,0.35);
}}

.filter-dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    flex-shrink: 0;
}}

/* ── CONTADOR ── */
.result-count {{
    font-size: 0.82rem;
    color: #2d3748;
    margin-bottom: 20px;
}}

.result-count strong {{ color: #4a5568; font-weight: 500; }}

/* ── GRID ── */
.cards-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 14px;
}}

/* ── CARD ── */
.pb-card {{
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 20px 22px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s, background 0.2s;
    animation: fadeUp 0.35s ease both;
}}

@keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}

.pb-card:hover {{
    background: rgba(255,255,255,0.035);
    border-color: rgba(255,255,255,0.1);
}}

.card-accent {{
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 3px;
    border-radius: 16px 0 0 16px;
}}

.card-header {{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 10px;
    padding-left: 12px;
}}

.card-title {{
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #e2e8f0;
    line-height: 1.3;
    flex: 1;
}}

.card-tag {{
    font-size: 0.68rem;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 100px;
    white-space: nowrap;
    flex-shrink: 0;
    letter-spacing: 0.3px;
}}

.card-desc {{
    font-size: 0.85rem;
    color: #4a5568;
    line-height: 1.6;
    padding-left: 12px;
}}

.card-footer {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-left: 12px;
    margin-top: 4px;
}}

.btn-open {{
    font-family: 'Syne', sans-serif;
    font-size: 0.76rem;
    font-weight: 700;
    color: #00b4d8;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 14px;
    border-radius: 8px;
    border: 1px solid rgba(0,180,216,0.25);
    background: rgba(0,180,216,0.07);
    transition: background 0.18s, border-color 0.18s;
    letter-spacing: 0.2px;
    cursor: pointer;
    outline: none;
}}

.btn-open:hover {{
    background: rgba(0,180,216,0.14);
    border-color: rgba(0,180,216,0.5);
}}

.share-row {{ display: flex; gap: 12px; align-items: center; }}

.share-btn {{
    color: #2d3748;
    font-size: 1.05rem;
    text-decoration: none;
    transition: color 0.2s, transform 0.2s;
    display: inline-flex;
    align-items: center;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    outline: none;
    line-height: 1;
}}

.share-btn:hover {{ transform: scale(1.2); }}
.share-btn.li:hover {{ color: #0077b5; }}
.share-btn.wa:hover {{ color: #25d366; }}
.share-btn.cp:hover {{ color: #00b4d8; }}

/* ── TOOLTIP DE CÓPIA ── */
.copy-toast {{
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translateX(-50%) translateY(12px);
    background: rgba(0,180,216,0.15);
    border: 1px solid rgba(0,180,216,0.35);
    color: #00b4d8;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.82rem;
    padding: 8px 18px;
    border-radius: 100px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s, transform 0.2s;
    z-index: 9999;
    white-space: nowrap;
}}

.copy-toast.show {{
    opacity: 1;
    transform: translateX(-50%) translateY(0);
}}

/* ── EMPTY ── */
.empty-state {{
    text-align: center;
    padding: 80px 20px;
    display: none;
}}

.empty-state i {{ font-size: 2.2rem; color: #1a202c; display: block; margin-bottom: 14px; }}
.empty-state p {{ font-size: 0.88rem; color: #1a202c; }}
.empty-state strong {{ color: #2d3748; font-weight: 500; }}

/* ── SCROLLBAR ── */
::-webkit-scrollbar {{ width: 5px; }}
::-webkit-scrollbar-track {{ background: #060912; }}
::-webkit-scrollbar-thumb {{ background: rgba(0,180,216,0.15); border-radius: 3px; }}
</style>
</head>
<body>
<div class="page">

    <!-- HERO -->
    <div class="hero">
        <div class="hero-top">
            <div>
                <span class="hero-badge">📊 Portfólio Power BI</span>
                <h1 class="hero-title">
                    Dashboards que transformam<br>
                    <span class="accent">dados em decisões</span>
                </h1>
                <p class="hero-subtitle">
                    Inteligência de negócios aplicada a gestores que exigem resultado.
                </p>
            </div>
            <div class="hero-stats">
                <div class="hero-stat">
                    <span class="hero-stat-n">{total_projetos}</span>
                    <span class="hero-stat-l">Dashboards</span>
                </div>
                <div class="hero-stat">
                    <span class="hero-stat-n">+20</span>
                    <span class="hero-stat-l">Anos de campo</span>
                </div>
            </div>
        </div>
    </div>

    <!-- TOOLBAR -->
    <div class="toolbar">
        <div class="search-wrap">
            <i class="fa-solid fa-magnifying-glass"></i>
            <input type="text" id="pb-search" placeholder="Buscar por nome ou setor..." oninput="renderCards()">
        </div>
        <div class="filters">
            <button class="filter-btn active" data-cat="all" onclick="setFilter('all')">Todos</button>
            <button class="filter-btn" data-cat="financeiro" onclick="setFilter('financeiro')">
                <span class="filter-dot" style="background:#185FA5"></span> Financeiro
            </button>
            <button class="filter-btn" data-cat="operacoes" onclick="setFilter('operacoes')">
                <span class="filter-dot" style="background:#0F6E56"></span> Operações
            </button>
            <button class="filter-btn" data-cat="rh" onclick="setFilter('rh')">
                <span class="filter-dot" style="background:#993556"></span> RH &amp; Vendas
            </button>
            <button class="filter-btn" data-cat="publico" onclick="setFilter('publico')">
                <span class="filter-dot" style="background:#854F0B"></span> Setor Público
            </button>
            <button class="filter-btn" data-cat="varejo" onclick="setFilter('varejo')">
                <span class="filter-dot" style="background:#534AB7"></span> Varejo
            </button>
        </div>
    </div>

    <!-- CONTAGEM -->
    <p class="result-count" id="result-count"></p>

    <!-- GRID DE CARDS -->
    <div class="cards-grid" id="cards-grid"></div>

    <!-- ESTADO VAZIO -->
    <div class="empty-state" id="empty-state">
        <i class="fa-solid fa-magnifying-glass-minus"></i>
        <p>Nenhum dashboard encontrado.<br><strong>Tente outro termo ou remova o filtro.</strong></p>
    </div>

</div>

<!-- TOAST DE CÓPIA -->
<div class="copy-toast" id="copy-toast">🔗 Link copiado!</div>

<script>
const CATS = {{
    financeiro: {{ label: 'Financeiro', color: '#185FA5', bg: 'rgba(24,95,165,0.12)', text: '#60a5fa' }},
    operacoes:  {{ label: 'Operações',  color: '#0F6E56', bg: 'rgba(15,110,86,0.12)',  text: '#34d399' }},
    rh:         {{ label: 'RH & Vendas',color: '#993556', bg: 'rgba(153,53,86,0.12)',  text: '#f472b6' }},
    publico:    {{ label: 'Público',    color: '#854F0B', bg: 'rgba(133,79,11,0.12)',  text: '#fbbf24' }},
    varejo:     {{ label: 'Varejo',     color: '#534AB7', bg: 'rgba(83,74,183,0.12)',  text: '#a78bfa' }},
}};

const PROJECTS = {projects_json};

let activeFilter = 'all';

/* Abre URL escapando do sandbox do iframe do Streamlit */
function openURL(url) {{
    try {{
        window.top.open(url, '_blank', 'noopener,noreferrer');
    }} catch(e) {{
        window.open(url, '_blank', 'noopener,noreferrer');
    }}
}}

/* Compartilha no LinkedIn */
function shareLinkedIn(url) {{
    const liUrl = 'https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(url);
    openURL(liUrl);
}}

/* Compartilha no WhatsApp */
function shareWhatsApp(title, desc, url) {{
    const text = title + '\\n\\n' + desc + '\\n\\n🔗 ' + url;
    const waUrl = 'https://wa.me/?text=' + encodeURIComponent(text);
    openURL(waUrl);
}}

/* Copia link e exibe toast */
function copyLink(url) {{
    const toast = document.getElementById('copy-toast');
    if (navigator.clipboard && navigator.clipboard.writeText) {{
        navigator.clipboard.writeText(url).then(() => showToast(toast));
    }} else {{
        /* Fallback para contextos sem HTTPS */
        const ta = document.createElement('textarea');
        ta.value = url;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showToast(toast);
    }}
}}

function showToast(el) {{
    el.classList.add('show');
    setTimeout(() => el.classList.remove('show'), 2200);
}}

function setFilter(cat) {{
    activeFilter = cat;
    document.querySelectorAll('.filter-btn').forEach(b => {{
        b.classList.toggle('active', b.dataset.cat === cat);
    }});
    renderCards();
}}

function renderCards() {{
    const q = document.getElementById('pb-search').value.toLowerCase().trim();
    const grid = document.getElementById('cards-grid');
    const empty = document.getElementById('empty-state');
    const countEl = document.getElementById('result-count');

    const filtered = PROJECTS.filter(p => {{
        const matchCat = activeFilter === 'all' || p.cat === activeFilter;
        const matchQ = !q || p.title.toLowerCase().includes(q) || p.desc.toLowerCase().includes(q);
        return matchCat && matchQ;
    }});

    if (filtered.length === 0) {{
        grid.innerHTML = '';
        empty.style.display = 'block';
        countEl.innerHTML = '';
        return;
    }}

    empty.style.display = 'none';
    const word = filtered.length === 1 ? 'dashboard' : 'dashboards';
    countEl.innerHTML = `<strong>${{filtered.length}}</strong> ${{word}} encontrados`;

    grid.innerHTML = filtered.map((p, i) => {{
        const cat  = CATS[p.cat];
        const delay = Math.min(i * 40, 400);
        /* Escapa aspas simples para uso seguro em onclick inline */
        const safeTitle = p.title.replace(/'/g, "\\'");
        const safeDesc  = p.desc.replace(/'/g, "\\'");
        const safeUrl   = p.url.replace(/'/g, "\\'");
        return `
        <div class="pb-card" style="animation-delay:${{delay}}ms">
            <div class="card-accent" style="background:${{cat.color}};"></div>
            <div class="card-header">
                <span class="card-title">${{p.title}}</span>
                <span class="card-tag" style="background:${{cat.bg}}; color:${{cat.text}};">${{cat.label}}</span>
            </div>
            <p class="card-desc">${{p.desc}}</p>
            <div class="card-footer">
                <button class="btn-open" onclick="openURL('${{safeUrl}}')" title="Abrir dashboard no Power BI">
                    Abrir dashboard <i class="fa-solid fa-arrow-up-right-from-square" style="font-size:0.7rem;"></i>
                </button>
                <div class="share-row">
                    <button class="share-btn li" title="Compartilhar no LinkedIn"
                        onclick="shareLinkedIn('${{safeUrl}}')">
                        <i class="fa-brands fa-linkedin"></i>
                    </button>
                    <button class="share-btn wa" title="Compartilhar no WhatsApp"
                        onclick="shareWhatsApp('${{safeTitle}}', '${{safeDesc}}', '${{safeUrl}}')">
                        <i class="fa-brands fa-whatsapp"></i>
                    </button>
                    <button class="share-btn cp" title="Copiar link"
                        onclick="copyLink('${{safeUrl}}')">
                        <i class="fa-regular fa-copy"></i>
                    </button>
                </div>
            </div>
        </div>`;
    }}).join('');
}}

renderCards();
</script>
</body>
</html>
"""

# --- ESTILO GLOBAL DA PÁGINA STREAMLIT ---
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { background-color: #0a0e1a !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

# --- RENDERIZAÇÃO DO COMPONENTE HTML ---
components.html(html_content, height=1600, scrolling=False)

exibir_rodape()
