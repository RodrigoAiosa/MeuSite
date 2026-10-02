import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- ESTILO LANDING PAGE PREMIUM (FOCO EM RETENÇÃO & UX) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;700&display=swap');
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

*, *::before, *::after { box-sizing: border-box; }

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
}

[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(0,180,216,0.15) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(0,100,180,0.08) 0%, transparent 50%);
}

[data-testid="stHeader"] { background: transparent !important; }

.main h1, .main h2, .main h3, .main h4, .main p, .main a, .main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}

.block-container {
    max-width: 1200px !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* ── HERO OPTIMIZED ── */
.hero-wrapper {
    text-align: center;
    padding: 60px 20px 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.hero-badge {
    display: inline-block;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #00b4d8;
    border: 1px solid rgba(0,180,216,0.3);
    background: rgba(0,180,216,0.08);
    padding: 6px 16px;
    border-radius: 100px;
    margin-bottom: 20px;
}

.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2.2rem, 4.5vw, 3.8rem);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -1px;
    color: #f0f4ff;
    margin-bottom: 20px;
    max-width: 800px;
}

.hero-title .accent {
    background: linear-gradient(135deg, #00b4d8 0%, #48cae4 60%, #90e0ef 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 1.1rem;
    font-weight: 300;
    color: #7b8ba8;
    max-width: 600px;
    margin-bottom: 40px;
    line-height: 1.6;
}

.hero-stats {
    display: flex;
    justify-content: center;
    gap: 40px;
    flex-wrap: wrap;
    margin-bottom: 40px;
}

.hero-stat { text-align: center; background: rgba(255,255,255,0.02); padding: 10px 24px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); }
.hero-stat-number { font-family: 'Syne', sans-serif !important; font-size: 1.8rem; font-weight: 800; color: #00b4d8; }
.hero-stat-label { font-size: 0.75rem; color: #64748b; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }

/* ── TITULOS DE CATEGORIA ── */
.category-header {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.4rem;
    font-weight: 700;
    color: #f0f4ff;
    margin: 45px 0 20px 0;
    padding-left: 12px;
    border-left: 3px solid #00b4d8;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* ── FORÇA COLUNAS STREAMLIT MESMA ALTURA ── */
[data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
}

[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    display: flex !important;
    flex-direction: column !important;
}

[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] > [data-testid="stVerticalBlockBorderWrapper"],
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] > div {
    height: 100% !important;
    flex: 1 !important;
}

/* ── CARDS EM GRID INTERATIVO ── */
.ux-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.3) 100%);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 24px;
    height: 100%;
    min-height: 320px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease, box-shadow 0.4s ease;
    margin-bottom: 24px;
}

.ux-card:hover {
    transform: translateY(-6px);
    border-color: rgba(0,180,216,0.4);
    box-shadow: 0 12px 30px rgba(0,180,216,0.1);
}

.card-top { display: flex; gap: 16px; align-items: flex-start; margin-bottom: 16px; }
.card-icon-box { font-size: 32px; background: rgba(0,180,216,0.06); padding: 10px; border-radius: 12px; border: 1px solid rgba(0,180,216,0.1); line-height: 1; flex-shrink: 0; }
.ux-card-title { font-family: 'Syne', sans-serif !important; font-size: 1.15rem; font-weight: 700; color: #f0f4ff; line-height: 1.3; }

.ux-card-desc { font-size: 0.88rem; color: #94a3b8; line-height: 1.6; margin-bottom: 20px; flex-grow: 1; }

.card-actions { display: flex; flex-direction: column; gap: 12px; margin-top: auto; }
.btn-direct {
    background: linear-gradient(135deg, #00b4d8 0%, #0077b6 100%);
    color: #ffffff !important;
    padding: 12px;
    border-radius: 10px;
    text-align: center;
    text-decoration: none !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 0.5px;
    transition: opacity 0.3s ease;
    display: block;
}
.btn-direct:hover { opacity: 0.9; }

/* COMPARTILHAMENTO */
.share-row { display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.05); padding-top: 12px; }
.share-txt { font-size: 0.75rem; color: #64748b; font-weight: 500; }
.share-links { display: flex; gap: 8px; }

.share-btn-item {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 10px;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 600;
    text-decoration: none !important;
    transition: background-color 0.2s;
}
.share-btn-item.wa {
    background-color: rgba(37, 211, 102, 0.1);
    color: #25D366 !important;
    border: 1px solid rgba(37, 211, 102, 0.2);
}
.share-btn-item.wa:hover {
    background-color: rgba(37, 211, 102, 0.2);
}
.share-btn-item.li {
    background-color: rgba(10, 102, 194, 0.1);
    color: #0A66C2 !important;
    border: 1px solid rgba(10, 102, 194, 0.2);
}
.share-btn-item.li:hover {
    background-color: rgba(10, 102, 194, 0.2);
}

/* SEARCH BAR */
div[data-testid="stTextInput"] input {
    background-color: rgba(255,255,255,0.02) !important;
    color: #e2e8f0 !important;
    border: 1px solid rgba(0,180,216,0.2) !important;
    border-radius: 12px !important;
    padding: 12px 20px !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: rgba(0,180,216,0.6) !important;
    background-color: rgba(0,180,216,0.02) !important;
}
</style>
""", unsafe_allow_html=True)

# --- BASE DE DADOS DOS PROJETOS CATEGORIZADOS ---
pbi_projects = [
    {
    "title": "Panorama Macroeconômico Brasil",
    "icon": "📈",
    "category": "Setor Público & Geral",
    "url": "https://app.powerbi.com/view?r=eyJrIjoiZjAxMTdhODAtMjE2OC00ZTQ5LTllOTQtMmRiZjVmYWViMzFiIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9&pageName=c0a1b2c3d4e5f6a7b8c9",
    "desc": "Selic, IPCA, dólar e desemprego atualizados diariamente via API pública do Banco Central. Acompanhe juro real, inflação frente à meta e a evolução do câmbio e do emprego em um só painel."
    },
    {
        "title": "Transporte - Travel Company",
        "icon": "🚛",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiNjY5NThlNjctZWY1Ny00YjA0LTk0MjEtNzhiNjgzZjdjZjA2IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Transforme dados logísticos em vantagem competitiva. Analise indicadores de performance operacional, identifique ineficiências e otimize custos."
    },
    {
        "title": "Dashboard ANATEL - Reclamações",
        "icon": "📞",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/reportEmbed?reportId=a416b3a1-5446-422b-9d1c-9ac5c3089fd7&autoAuth=true&ctid=3606e3a2-62f5-40ac-ad22-0d6c80989030",
        "desc": "Monitoramento de reclamações gerais da ANATEL. Perfeito para identificar gargalos de atendimento, tendências e disparadores de insatisfação."
    },
    {
        "title": "Dashboard OEE - Eficiência Industrial",
        "icon": "🏭",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2YxN2NhZmQtMTg4My00YTgwLWJhOGQtZmRkNGZkNTM1ZDM0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Acompanhe disponibilidade, desempenho e qualidade de produção industrial em tempo real, mitigando as perdas ocultas do chão de fábrica."
    },
    {
        "title": "Portal da Transparência - Ilhéus",
        "icon": "🏛️",
        "category": "Setor Público & Geral",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTM2ZWFlM2QtOTc2NC00NDQ2LTg2ZTctOGY5Nzc4YTk2YWM1IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Auditoria de dados públicos municipais simplificada. Transparência visual clara de receitas, despesas empenhadas e investimentos de Ilhéus."
    },
    {
        "title": "💹 DRE Estratégico — Finanças",
        "icon": "💰",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiOWE0ZmU3ZTMtYzAyYi00NDE1LTg3YWItYjcxZTE2ZWI2OWRjIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Demonstrativo de Resultados estruturado com análises vertical e horizontal automáticas. Avalie margens de contribuição e lucratividade real."
    },
    {
        "title": "🏦 Monitoramento de Vagas — Bradesco",
        "icon": "👔",
        "category": "RH & People Analytics",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMjQxN2Q4NGYtNWRmNy00NWVjLWE4YmQtNWMyNWYwNGYyZDUzIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Visão consolidada do fluxo interno de contratações do banco. Mapeamento por praças regionais, perfis técnicos de entrada e status de posições."
    },
    {
        "title": "💳 Relatório STONE - Faturamento B2B",
        "icon": "💳",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Acompanhamento granular de performance de adquirência de cartões. Métricas de Ticket Médio, faturamento bruto e fatias de mercado."
    },
    {
        "title": "📊 Vendas Meta vs Realizado",
        "icon": "🎯",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Gestão comercial cirúrgica. Identifique rapidamente quais filiais ou vendedores estão performando abaixo da linha de corte esperada."
    },
    {
        "title": "📦 Controle de Pedidos BNZ",
        "icon": "📦",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZDZlNzViNzMtODllZS00OTVlLWI4MWQtNzBhZmU5ZTkxY2E0IiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Níveis de estoque e giro de produtos atualizados. Ideal para evitar rupturas de prateleira e excessos de capital imobilizado."
    },
    {
        "title": "🎯 Análise Dados Estratégica",
        "icon": "📈",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Visão unificada para C-Level. Consolidação ágil de múltiplos vetores de crescimento e gaps de eficiência organizacional interna."
    },
    {
        "title": "👥 People Analytics (RH)",
        "icon": "👥",
        "category": "RH & People Analytics",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Inteligência de departamento pessoal: Funil de R&S, turnover, custos associados a comissões e bonificações integradas por performance."
    },
    {
        "title": "🚀 Relatório Borelli",
        "icon": "🚀",
        "category": "Operações & Logística",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiZTY5YmEzZmQtZDVhMS00N2QyLWJhY2QtMDNhMWFmMDRjMjNmIiwidCI6IjM2MDZlM2EyLTYyZjUtNDBhYy1hZDIyLTBkNmM4MDk4OTAzMCJ9",
        "desc": "Mapeamento minucioso do ciclo de produção industrial. Identificação ágil de gargalos e taxas de ociosidade de maquinário."
    },
    {
        "title": "🏖️ Financeiro — Beocean Resort",
        "icon": "🏖️",
        "category": "Estratégico & Financeiro",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiY2VkZmU1MDMtNTgwZS00NTJmLWFhOTktYzM0YzMwZDE3OTE4IiwidCI6IjdjNTYzNjMxLTcyZGMtNDY1Ny05MTRkLWIyM2M5ZTI5OGVlMSJ9",
        "desc": "Fluxo de caixa corporativo adaptado para redes de hotelaria. Gestão centralizada de canais de receita direta e custos operacionais fixos."
    }
]

# --- HERO AREA ---
total_projetos = len(pbi_projects)
st.markdown(f"""
<div class="hero-wrapper">
    <div class="hero-badge">📊 Portfólio de Alta Performance</div>
    <h1 class="hero-title">Dashboards que transformam <span class="accent">Dados em Lucro</span></h1>
    <p class="hero-subtitle">Arquitetura de BI de nível corporativo. Role para baixo e conheça todas as soluções segmentadas por verticais de negócio.</p>
    <div class="hero-stats">
        <div class="hero-stat"><span class="hero-stat-number">{total_projetos}</span><span class="hero-stat-label"> Painéis Ativos</span></div>
        <div class="hero-stat"><span class="hero-stat-number">+20 Anos</span><span class="hero-stat-label"> De Projetos REAIS</span></div>
        <div class="hero-stat"><span class="hero-stat-number">100%</span><span class="hero-stat-label"> Foco em Decisão</span></div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- SISTEMA DE BUSCA CENTRALIZADO ---
col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
with col_s2:
    search_query = st.text_input(
        label="Pesquisa Inteligente",
        placeholder="Digite termos como: RH, Financeiro, Logística...",
        key="search_pbi",
        label_visibility="collapsed"
    )

st.write("")

# --- RENDERIZADOR DE CARD INDIVIDUAL ---
def renderizar_card(p):
    mensagem_whatsapp = (
        f"Olá! Veja que excelente dashboard de Power BI:\n\n"
        f"📊 *{p['title']}*\n"
        f"ℹ️ {p['desc']}\n\n"
        f"🔗 Aceda ao painel completo aqui: {p['url']}"
    )
    wa_link = f"https://wa.me/?text={urllib.parse.quote(mensagem_whatsapp)}"

    li_base = "https://www.linkedin.com/shareArticle?mini=true"
    li_title = urllib.parse.quote(p['title'])
    li_summary = urllib.parse.quote(f"Solução de BI: {p['desc']}")
    li_url = urllib.parse.quote(p['url'])
    li_link = f"{li_base}&url={li_url}&title={li_title}&summary={li_summary}"

    st.markdown(f"""
    <div class="ux-card">
        <div style="display:flex; flex-direction:column; flex-grow:1;">
            <div class="card-top">
                <div class="card-icon-box">{p['icon']}</div>
                <div class="ux-card-title">{p['title']}</div>
            </div>
            <div class="ux-card-desc">{p['desc']}</div>
        </div>
        <div class="card-actions">
            <a href="{p['url']}" target="_blank" class="btn-direct">Abrir Dashboard →</a>
            <div class="share-row">
                <span class="share-txt">Compartilhar:</span>
                <div class="share-links">
                    <a href="{wa_link}" target="_blank" class="share-btn-item wa">
                        <i class="fab fa-whatsapp"></i> WhatsApp
                    </a>
                    <a href="{li_link}" target="_blank" class="share-btn-item li">
                        <i class="fab fa-linkedin"></i> LinkedIn
                    </a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- FLUXO DINÂMICO DE FILTRO VS GERAL ---
if search_query:
    # 🌟 PESQUISA ULTRA INTELIGENTE: Quebra os termos digitados e valida de forma ampla
    search_terms = search_query.lower().split()
    filtered_projects = []

    for p in pbi_projects:
        # Texto consolidado do painel para checar contra os termos pesquisados
        texto_painel = f"{p['title']} {p['desc']} {p['category']} {p['icon']}".lower()

        # O painel precisa conter TODOS os termos digitados (independente da ordem ou posição)
        if all(term in texto_painel for term in search_terms):
            filtered_projects.append(p)

    if filtered_projects:
        st.markdown(f"<p style='color:#64748b; text-align:center;'>Exibindo {len(filtered_projects)} resultado(s) para sua busca</p>", unsafe_allow_html=True)
        for i in range(0, len(filtered_projects), 3):
            cols = st.columns(3)
            for j in range(3):
                idx = i + j
                if idx < len(filtered_projects):
                    with cols[j]:
                        renderizar_card(filtered_projects[idx])
    else:
        st.markdown("""
        <div style="text-align:center; padding: 40px; color: #64748b;">
            <p style="font-size:2rem;">🔍</p>
            <h3>Nenhum painel atende a esse termo.</h3>
            <p>Tente buscar por palavras mais amplas ou termos contidos nas descrições.</p>
        </div>
        """, unsafe_allow_html=True)

else:
    # --- VISUALIZAÇÃO GERAL ---
    categorias = ["Estratégico & Financeiro", "Operações & Logística", "RH & People Analytics", "Setor Público & Geral"]

    for cat_name in categorias:
        cat_projects = [p for p in pbi_projects if p["category"] == cat_name]

        if cat_projects:
            st.markdown(f'<div class="category-header"><span></span> {cat_name}</div>', unsafe_allow_html=True)

            for i in range(0, len(cat_projects), 3):
                cols = st.columns(3)
                for j in range(3):
                    idx_proj = i + j
                    if idx_proj < len(cat_projects):
                        with cols[j]:
                            renderizar_card(cat_projects[idx_proj])

st.markdown('<div style="height: 60px;"></div>', unsafe_allow_html=True)
exibir_rodape()
