import streamlit as st
import pandas as pd
import os
from datetime import datetime
import base64
from io import BytesIO
import requests
from bs4 import BeautifulSoup

# --------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------
st.set_page_config(
    page_title="DataHub — Datasets para Análise",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
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

.main h1, .main h2, .main h3, .main h4,
.main p, .main a, .main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}

.material-symbols-rounded,
.material-icons,
[data-testid*="Collapse"] span,
[data-testid*="collapse"] span {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
}

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

/* ── CATEGORY TABS ── */
.category-tabs {
    display: flex;
    justify-content: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 40px;
    padding: 0 20px;
}

.category-tab {
    padding: 10px 20px;
    border-radius: 12px;
    border: 1px solid rgba(0,180,216,0.25);
    background: rgba(0,180,216,0.05);
    color: #4a5568;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
}

.category-tab.active {
    background: rgba(0,180,216,0.15);
    border-color: rgba(0,180,216,0.5);
    color: #00b4d8;
    font-weight: 600;
}

.category-tab:hover {
    border-color: rgba(0,180,216,0.4);
    background: rgba(0,180,216,0.08);
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

/* ── DATASET CARDS ── */
.dataset-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    padding: 30px 32px;
    border-radius: 20px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,0.05);
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.dataset-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.4), transparent);
    opacity: 0;
    transition: opacity 0.35s ease;
}

.dataset-card:hover {
    transform: translateY(-4px);
    border-color: rgba(0,180,216,0.2);
    box-shadow:
        0 20px 40px rgba(0,0,0,0.4),
        0 0 0 1px rgba(0,180,216,0.1),
        inset 0 1px 0 rgba(0,180,216,0.1);
    background: linear-gradient(145deg, rgba(0,180,216,0.04) 0%, rgba(0,0,0,0.25) 100%);
}

.dataset-card:hover::before {
    opacity: 1;
}

.dataset-card-icon {
    font-size: 2.2rem;
    margin-bottom: 12px;
    display: block;
}

.dataset-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 10px;
    line-height: 1.35;
    letter-spacing: -0.3px;
}

.dataset-description {
    color: #4a5568;
    font-size: 0.9rem;
    font-weight: 300;
    line-height: 1.65;
    margin-bottom: 16px;
}

.dataset-meta {
    display: flex;
    gap: 16px;
    font-size: 0.82rem;
    color: #2d3748;
    margin-bottom: 18px;
    flex-wrap: wrap;
}

.dataset-meta-item {
    display: flex;
    align-items: center;
    gap: 6px;
}

.dataset-buttons {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.dataset-button {
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

.dataset-button:hover {
    background: rgba(0,180,216,0.18);
    border-color: rgba(0,180,216,0.5);
    transform: translateX(3px);
    box-shadow: 0 4px 20px rgba(0,180,216,0.2);
}

.dataset-button .arrow {
    font-size: 1rem;
    transition: transform 0.3s ease;
}

.dataset-button:hover .arrow {
    transform: translateX(3px);
}

.download-info {
    font-size: 0.78rem;
    color: #2d3748;
    margin-top: 4px;
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
# FUNÇÃO PARA EXTRAIR DATASETS DO TABLEAU
# --------------------------------------------------
@st.cache_data(ttl=3600)  # Cache de 1 hora
def get_tableau_datasets():
    try:
        url = "https://public.tableau.com/app/learn/sample-data"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrar todos os assets (recursos)
        assets = soup.find_all('tr', class_='_resourceAsset_atqz8_160')
        
        datasets = []
        
        for asset in assets:
            link = asset.find('a', href=True)
            if link:
                href = link.get('href')
                text = link.get_text(strip=True)
                
                if href and ('/app/sample-data/' in href):
                    # Construir URL completa
                    if href.startswith('/'):
                        full_url = 'https://public.tableau.com' + href
                    else:
                        full_url = href
                    
                    # Extrair nome do arquivo
                    file_name = href.split('/')[-1]
                    
                    # Determinar categoria e ícone baseado no nome
                    if any(word in file_name.lower() for word in ['superstore', 'store']):
                        category = "Vendas"
                        icon = "💰"
                    elif any(word in file_name.lower() for word in ['coffee', 'retail']):
                        category = "Varejo"
                        icon = "☕"
                    elif any(word in file_name.lower() for word in ['world', 'global', 'geography']):
                        category = "Global"
                        icon = "🌍"
                    elif any(word in file_name.lower() for word in ['flight', 'airline']):
                        category = "Transporte"
                        icon = "✈️"
                    elif any(word in file_name.lower() for word in ['gbbo', 'recipe']):
                        category = "Entretenimento"
                        icon = "🎬"
                    else:
                        category = "Diversos"
                        icon = "📊"
                    
                    datasets.append({
                        "category": category,
                        "icon": icon,
                        "title": file_name.replace('_', ' ').replace('.csv', '').replace('.xls', '').replace('.xlsx', '').replace('.zip', ''),
                        "description": f"Dataset {text.lower()} do Tableau Sample Data",
                        "rows": "N/A",
                        "cols": "N/A",
                        "size": "N/A",
                        "url": full_url,
                        "file_name": file_name
                    })
        
        return datasets if datasets else get_default_datasets()
        
    except Exception as e:
        st.warning(f"Não foi possível carregar datasets do Tableau: {str(e)}")
        return get_default_datasets()

def get_default_datasets():
    """Datasets padrão caso o scraping falhe"""
    return [
        {
            "category": "Vendas",
            "icon": "💰",
            "title": "Superstore Sales",
            "description": "Dados de vendas de uma rede de lojas com informações de clientes, produtos e transações.",
            "rows": 9994,
            "cols": 17,
            "size": "2.4 MB",
            "url": "https://public.tableau.com/app/sample-data/sample_-_superstore.xls",
            "file_name": "superstore_sales.xls"
        },
        {
            "category": "Vendas",
            "icon": "📈",
            "title": "World Indicators",
            "description": "Indicadores econômicos mundiais com dados de países e regiões.",
            "rows": 6340,
            "cols": 15,
            "size": "1.2 MB",
            "url": "https://public.tableau.com/app/sample-data/sample_-_world_indicators.xlsx",
            "file_name": "world_indicators.xlsx"
        },
    ]

# Carregar datasets
datasets = get_tableau_datasets()

# --------------------------------------------------
# HERO
# --------------------------------------------------
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-badge">📊 DataHub</div>
    <h1 class="hero-title">
        Datasets para <span class="accent">análise profissional</span>
    </h1>
    <p class="hero-subtitle">
        Acesso a datasets curados para análise de dados, visualizações e business intelligence. Tudo pronto para download.
    </p>
    <div class="hero-stats">
        <div class="hero-stat">
            <span class="hero-stat-number">9</span>
            <span class="hero-stat-label">Datasets</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">5</span>
            <span class="hero-stat-label">Categorias</span>
        </div>
        <div class="hero-stat">
            <span class="hero-stat-number">100%</span>
            <span class="hero-stat-label">Gratuito</span>
        </div>
    </div>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# BARRA DE PESQUISA
# --------------------------------------------------
st.markdown(
    "<p class='search-label'>🔍 Filtre os datasets pelo nome ou descrição</p>",
    unsafe_allow_html=True
)

col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
with col_s2:
    search_query = st.text_input(
        label="Pesquisar dataset",
        placeholder="Ex: Sales, HR, Finance...",
        key="search_datasets",
        label_visibility="collapsed"
    )

st.write("")

# --------------------------------------------------
# FILTRO POR CATEGORIA
# --------------------------------------------------
categories = sorted(list(set([d["category"] for d in datasets])))
categories_with_all = ["Todas"] + categories

col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
with col_s2:
    selected_category = st.selectbox(
        label="Filtrar por categoria",
        options=categories_with_all,
        index=0,
        label_visibility="collapsed",
        key="category_filter"
    )

st.write("")

# --------------------------------------------------
# LÓGICA DE FILTRO
# --------------------------------------------------
filtered_datasets = datasets.copy()

if selected_category != "Todas":
    filtered_datasets = [d for d in filtered_datasets if d["category"] == selected_category]

if search_query:
    filtered_datasets = [
        d for d in filtered_datasets
        if search_query.lower() in d["title"].lower() or search_query.lower() in d["description"].lower()
    ]

# --------------------------------------------------
# CONTAGEM DE RESULTADOS
# --------------------------------------------------
if search_query or selected_category != "Todas":
    total = len(filtered_datasets)
    label = "resultado" if total == 1 else "resultados"
    filter_text = f"Categoria: {selected_category}" if selected_category != "Todas" else ""
    if search_query:
        filter_text += f" • Busca: \"{search_query}\"" if filter_text else f"Busca: \"{search_query}\""
    
    st.markdown(
        f"<div class='search-result-count'>🔎 <span>{total}</span> {label} encontrados • {filter_text}</div>",
        unsafe_allow_html=True
    )

# --------------------------------------------------
# MENSAGEM QUANDO NÃO HÁ RESULTADOS
# --------------------------------------------------
if not filtered_datasets:
    st.markdown(
        """
        <div class="empty-state">
            <div class="empty-state-icon">🔍</div>
            <div class="empty-state-title">Nenhum dataset encontrado.</div>
            <div class="empty-state-sub">Tente outro termo de pesquisa ou categoria.</div>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.write("")
    st.markdown('<div class="section-label">— Datasets Disponíveis —</div>', unsafe_allow_html=True)

# --------------------------------------------------
# RENDERIZAÇÃO DOS CARDS
# --------------------------------------------------
for dataset in filtered_datasets:
    # Criar botões de ação
    col1, col2 = st.columns([2.5, 1])
    
    with col1:
        st.markdown(f"""
        <div class="dataset-card">
            <span class="dataset-card-icon">{dataset['icon']}</span>
            <div class="dataset-title">{dataset['title']}</div>
            <p class="dataset-description">{dataset['description']}</p>
            <div class="dataset-meta">
                <div class="dataset-meta-item">📝 {dataset['rows']:,} linhas</div>
                <div class="dataset-meta-item">📋 {dataset['cols']} colunas</div>
                <div class="dataset-meta-item">💾 {dataset['size']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if st.button(
            "⬇️ Download",
            key=f"download_{dataset['title']}",
            use_container_width=True,
            help=f"Download {dataset['title']}"
        ):
            try:
                import requests
                
                # Headers para simular um navegador
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                # Fazer requisição para o arquivo
                response = requests.get(
                    dataset['url'], 
                    timeout=30, 
                    allow_redirects=True,
                    headers=headers,
                    verify=True
                )
                response.raise_for_status()
                
                st.download_button(
                    label="✓ Pronto",
                    data=response.content,
                    file_name=dataset['file_name'],
                    mime="application/octet-stream",
                    key=f"download_btn_{dataset['title']}"
                )
            except requests.exceptions.Timeout:
                st.error(f"❌ Timeout ao baixar. Tente novamente em alguns segundos.")
            except requests.exceptions.ConnectionError:
                st.error(f"❌ Erro de conexão. Verifique sua internet.")
            except requests.exceptions.HTTPError as e:
                st.error(f"❌ Erro HTTP {e.response.status_code}: Arquivo não encontrado ou acesso negado.")
            except Exception as e:
                st.error(f"❌ Erro ao baixar: {str(e)}")
    
    st.write("")

st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("""
<div style="text-align: center; padding: 40px 20px; color: #2d3748; font-size: 0.85rem; border-top: 1px solid rgba(0,180,216,0.1);">
    <p>📊 DataHub © 2024 | Datasets curados para análise profissional</p>
    <p style="margin-top: 10px; color: #1a202c; font-size: 0.8rem;">
        Acesse dados prontos para exploração. Todos os datasets estão disponíveis para download gratuito.
    </p>
</div>
""", unsafe_allow_html=True)
