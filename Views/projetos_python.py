import streamlit as st
import urllib.parse
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
# ESTILO GLOBAL DA LANDING PAGE
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

.main h1, .main h2, .main h3, .main h4, .main p, .main a, .main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}

.block-container {
    max-width: 1200px !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* ── HERO ── */
.hero-wrapper {
    text-align: center;
    padding: 80px 20px 30px;
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
    margin-bottom: 40px;
}

.hero-stat {
    text-align: center;
    background: rgba(255,255,255,0.02);
    padding: 10px 24px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.05);
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
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 6px;
    display: block;
}

.hero-divider {
    width: 100%;
    max-width: 900px;
    margin: 40px auto 40px;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.3), transparent);
}

/* ── SEARCH ── */
.search-label {
    text-align: center;
    font-size: 0.85rem;
    color: #64748b;
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

div[data-testid="stTextInput"] input:focus {
    box-shadow: 0 0 0 3px rgba(0,180,216,0.15) !important;
    border-color: rgba(0,180,216,0.6) !important;
    background-color: rgba(0,180,216,0.04) !important;
}

.search-result-count {
    text-align: center;
    color: #64748b;
    font-size: 0.88rem;
    margin: 14px 0 28px;
}
.search-result-count span {
    color: #00b4d8;
    font-weight: 600;
}

/* ── FILTROS POR CATEGORIA (BOTÕES STREAMLIT) ── */
div[data-testid="stHorizontalBlock"] div[data-testid="element-container"] button {
    background-color: rgba(255, 255, 255, 0.02) !important;
    color: #94a3b8 !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 10px !important;
    padding: 6px 16px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.85rem !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
}

div[data-testid="stHorizontalBlock"] div[data-testid="element-container"] button:hover {
    border-color: rgba(0, 180, 216, 0.4) !important;
    color: #00b4d8 !important;
    background-color: rgba(0, 180, 216, 0.03) !important;
}

.section-label {
    font-family: 'Syne', sans-serif !important;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #f0f4ff;
    margin-top: 35px;
    margin-bottom: 32px;
    text-align: center;
}

/* ── FORÇA COLUNAS STREAMLIT MESMA ALTURA (rolagem nativa da página) ── */
[data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
}

[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] {
    display: flex !important;
    flex-direction: column !important;
    height: auto !important;
}

[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] > div {
    height: 100% !important;
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
}

[data-testid="stColumn"] [data-testid="stVerticalBlock"] {
    height: 100% !important;
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
}

[data-testid="stColumn"] [data-testid="stVerticalBlockBorderWrapper"] {
    height: 100% !important;
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
}

[data-testid="stColumn"] [data-testid="element-container"],
[data-testid="stColumn"] [data-testid="stElementContainer"] {
    height: 100% !important;
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
}

[data-testid="stColumn"] [data-testid="stMarkdownContainer"] {
    height: 100% !important;
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
}

[data-testid="stColumn"] [data-testid="stMarkdown"] {
    height: 100% !important;
    flex: 1 !important;
    display: flex !important;
    flex-direction: column !important;
}

/* ── CARDS EM GRID NATIVO (mesmo estilo do Power BI) ── */
.ux-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.3) 100%);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 24px;
    height: 360px !important;
    min-height: 360px !important;
    max-height: 360px !important;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.4s ease, box-shadow 0.4s ease;
    margin-bottom: 24px;
    overflow: hidden;
}

.ux-card:hover {
    transform: translateY(-6px);
    border-color: rgba(0,180,216,0.4);
    box-shadow: 0 12px 30px rgba(0,180,216,0.1);
}

.card-badge {
    display: inline-block;
    font-family: 'Syne', sans-serif !important;
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: rgba(0, 180, 216, 0.85);
    background: rgba(0, 180, 216, 0.05);
    border: 1px solid rgba(0, 180, 216, 0.2);
    padding: 4px 10px;
    border-radius: 6px;
    margin-bottom: 14px;
    align-self: flex-start;
}

.ux-card-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem;
    font-weight: 700;
    color: #f0f4ff;
    margin-bottom: 10px;
    line-height: 1.35;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    min-height: calc(1.35em * 2);
}

.ux-card-desc {
    font-size: 0.85rem;
    color: #94a3b8;
    font-weight: 300;
    line-height: 1.6;
    margin-bottom: 20px;
    flex-grow: 1;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

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
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DATA SOURCING (LISTA DE PROJETOS COM CATEGORIAS)
# --------------------------------------------------
python_projects = [
    {
      "title": "🎮 DAX 2048",
      "desc": "Um jogo educativo inspirado no clássico 2048, onde cada peça representa uma função DAX do Power BI. Ao combinar duas peças iguais, você evolui para funções cada vez mais avançadas, transformando o aprendizado de DAX em uma experiência divertida, interativa e progressiva.",
      "url": "https://jogo2048dax.streamlit.app/",
      "category": "Educação"
    },
    {
        "title": "🤖 Automação GNX Group",
        "desc": "Automação inteligente para preenchimento de formulários no site da GNX Group. Sistema com suporte a múltiplas execuções, geração de logs em CSV com separador ponto e vírgula, e interface intuitiva para automação de processos de captação de leads e contatos comerciais.",
        "url": "https://rpagnxgroup.streamlit.app/",
        "category": "Automação & BI"
    },
    
    {
    "title": "💰Salário Médio por Estado — Brasil",
    "desc": "Explore o salário médio dos trabalhadores em todos os estados brasileiros com dados oficiais. Compare remunerações por unidade da federação, visualize rankings, mapas e gráficos interativos para analisar as diferenças salariais entre as regiões do país.",
    "url": "https://salariomediobrasil.streamlit.app/",
    "category": "Dados & IBGE"
    },
    
    {
    "title": "🚌 Olho Vivo Dashboard",
    "desc": "Acompanhe o transporte público de São Paulo em tempo real com dados da API Olho Vivo (SPTrans). Consulte linhas, paradas e corredores, veja a posição ao vivo de toda a frota e a previsão de chegada por parada ou linha, com mapa interativo e atualização automática.",
    "url": "https://appsptrans.streamlit.app/",
    "category": "Automação & BI"
    },
    {
    "title": "📊 Processador Inteligente de CEPs",
    "desc": "Automatize a consulta de endereços com dados do Via CEP. Realize buscas individuais com mapa interativo ou processe lotes de planilhas (CSV/XLSX) para obter dados completos como DDD e IBGE. Explore ainda bairros por faixa de CEP com consultas por amostragem.",
    "url": "https://consultacep.streamlit.app/",
    "category": "Dados & IBGE"
    },
    {
        "title": "📍 População Brasil",
        "desc": "Dashboard interativo com dados populacionais oficiais do IBGE. Explore estimativas demográficas por região, estado e município com visualizações dinâmicas e mapas interativos.",
        "url": "https://populacaobrasil.streamlit.app/",
        "category": "Dados & IBGE"
    },
    {
        "title": "📍 População Municipal",
        "desc": "Consulta detalhada de população por município brasileiro usando dados oficiais da tabela SIDRA 6579 do IBGE. Visualize rankings, compare regiões e acompanhe tendências demográficas.",
        "url": "https://popualcaoibge.streamlit.app/",
        "category": "Dados & IBGE"
    },
    {
        "title": "💰 Renda por Município - São Paulo",
        "desc": "Análise aprofundada da distribuição de renda nos municípios paulistas com dados oficiais do IBGE. Explore PIB per capita, estimativas de renda familiar e desigualdades regionais em dashboards interativos.",
        "url": "https://renda-cidades-sp-ibge.streamlit.app/",
        "category": "Dados & IBGE"
    },
    {
        "title": "🎓 O cursinho que o Brasil não pode pagar — eu construí de graça",
        "desc": "Simulador ENEM gratuito com questões reais, correção automática, estatísticas de desempenho e plano de estudos personalizado. Democratizando o acesso à preparação para o vestibular.",
        "url": "https://enem-simulador.streamlit.app/",
        "category": "Educação"
    },
    {
        "title": "🎓 Simulador FUVEST",
        "desc": "Treine para a FUVEST com questões de provas anteriores, correção instantânea, análise de desempenho por área e recomendações personalizadas de estudo. 100% gratuito e sem cadastro.",
        "url": "https://simulador-fuvest.streamlit.app/",
        "category": "Educação"
    },
    {
        "title": "✈️ Simulador ITA — 2021 a 2025",
        "desc": "Prepare-se para o vestibular mais concorrido do Brasil com questões reais do ITA dos últimos 5 anos. Gabarito comentado, cronômetro integrado, estatísticas de desempenho e análise por disciplina.",
        "url": "https://simulador-ita.streamlit.app/",
        "category": "Educação"
    },
    {
        "title": "🚀 BI Data Generator PRO",
        "desc": "Ferramenta inteligente que analisa seu desempenho no ENEM por área do conhecimento, explica cada resposta detalhadamente e identifica pontos críticos para otimizar seus estudos. Com IA integrada.",
        "url": "https://ai-bidatagenerator.streamlit.app/",
        "category": "Automação & BI"
    },
    {
        "title": "🗺️ CrimeMap BR — Segurança Pública",
        "desc": "Dashboard interativo com dados oficiais de criminalidade do Rio de Janeiro. Analise padrões de ocorrências por município, tipo de crime e período, com visualizações georreferenciadas e filtros dinâmicos.",
        "url": "https://rodrigoaiosa-crimemap.hf.space",
        "category": "Impacto Social"
    },
    {
        "title": "🦉 Calculadora ROI de Automação",
        "desc": "Ferramenta estratégica para calcular o Retorno sobre Investimento (ROI) de projetos de automação. Compare cenários, projete resultados financeiros e tome decisões baseadas em dados.",
        "url": "https://roiautomacao.streamlit.app/",
        "category": "Automação & BI"
    },
    {
        "title": "💼 APP S.O.S. MULHER",
        "desc": "Plataforma de conscientização e análise de dados sobre violência contra a mulher no Brasil. Visualize estatísticas, tendências regionais e tenha acesso a recursos e informações de apoio.",
        "url": "https://rodrigoaiosa-help-mulher.hf.space",
        "category": "Impacto Social"
    },
]

total_projetos = len(python_projects)

# --------------------------------------------------
# RENDER HERO
# --------------------------------------------------
st.markdown(f"""
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
            <span class="hero-stat-number">{total_projetos}</span>
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
# RENDER FILTRO DE BUSCA
# --------------------------------------------------
st.markdown("<p class='search-label'>🔍 Filtre os projetos pelo nome ou descrição</p>", unsafe_allow_html=True)

_, col_s2, _ = st.columns([1, 2, 1])
with col_s2:
    search_query = st.text_input(
        label="Pesquisar projeto",
        placeholder="Ex: ENEM, ROI, mapas, IBGE...",
        key="search_python",
        label_visibility="collapsed"
    )

# --------------------------------------------------
# COMPONENTE DE FILTRO INTERATIVO POR CATEGORIA
# --------------------------------------------------
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Todos"

categorias = ["Todos", "Dados & IBGE", "Educação", "Automação & BI", "Impacto Social"]

col_cat = st.columns(len(categorias))
for i, cat in enumerate(categorias):
    with col_cat[i]:
        label_btn = f"✓ {cat}" if st.session_state.selected_category == cat else cat
        if st.button(label_btn, key=f"btn_cat_{cat}"):
            st.session_state.selected_category = cat
            st.rerun()

# --------------------------------------------------
# MECANISMO DE FILTRAGEM (TEXTO + CATEGORIA)
# --------------------------------------------------
filtered_projects = python_projects

if st.session_state.selected_category != "Todos":
    filtered_projects = [p for p in filtered_projects if p["category"] == st.session_state.selected_category]

if search_query:
    search_terms = search_query.lower().split()
    filtered_projects = [
        p for p in filtered_projects
        if all(term in f"{p['title']} {p['desc']}".lower() for term in search_terms)
    ]
    total_resultados = len(filtered_projects)
    label = "resultado" if total_resultados == 1 else "resultados"
    st.markdown(
        f"<div class='search-result-count'>🔎 <span>{total_resultados}</span> {label} encontrados</div>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# RENDERIZADOR DE CARD INDIVIDUAL (mesmo padrão do Power BI)
# --------------------------------------------------
def renderizar_card(p):
    mensagem_whatsapp = (
        f"Olá! Veja esse projeto em Python:\n\n"
        f"📌 *{p['title']}*\n"
        f"ℹ️ {p['desc']}\n\n"
        f"🔗 Acesse a aplicação aqui: {p['url']}"
    )
    wa_link = f"https://wa.me/?text={urllib.parse.quote(mensagem_whatsapp)}"

    li_base = "https://www.linkedin.com/shareArticle?mini=true"
    li_title = urllib.parse.quote(p['title'])
    li_summary = urllib.parse.quote(f"Projeto Python: {p['desc']}")
    li_url = urllib.parse.quote(p['url'])
    li_link = f"{li_base}&url={li_url}&title={li_title}&summary={li_summary}"

    st.markdown(f"""
    <div class="ux-card">
        <div style="display:flex; flex-direction:column; flex-grow:1;">
            <div class="card-badge">{p['category']}</div>
            <div class="ux-card-title">{p['title']}</div>
            <div class="ux-card-desc">{p['desc']}</div>
        </div>
        <div class="card-actions">
            <a href="{p['url']}" target="_blank" class="btn-direct">Acessar Aplicação →</a>
            <div class="share-row">
                <span class="share-txt">Compartilhar:</span>
                <div class="share-links">
                    <a href="{wa_link}" target="_blank" class="share-btn-item wa">
                        WhatsApp
                    </a>
                    <a href="{li_link}" target="_blank" class="share-btn-item li">
                        LinkedIn
                    </a>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# EXIBIÇÃO EM GRID NATIVO STREAMLIT (rolagem da própria página)
# --------------------------------------------------
if filtered_projects:
    label_secao = f"Aplicações Ativas — {st.session_state.selected_category}" if st.session_state.selected_category != "Todos" else "Todas as Aplicações"
    st.markdown(f'<div class="section-label">{label_secao}</div>', unsafe_allow_html=True)

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
            <h3>Nenhum projeto encontrado nesta categoria.</h3>
            <p>Tente mudar a categoria selecionada ou limpe os termos pesquisados.</p>
        </div>
    """, unsafe_allow_html=True)

st.write("")
exibir_rodape()
