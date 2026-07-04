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

.main h1, .main h2, .main h3, .main h4, .main p, .main a, .main li {
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

div[data-testid="stHorizontalBlock"] div[data-testid="element-container"] button p:contains("✓") {
    color: #00b4d8 !important;
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
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DATA SOURCING (LISTA DE PROJETOS COM CATEGORIAS)
# --------------------------------------------------
python_projects = [
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
# INJEÇÃO DO COMPONENTE ISOLADO EM CSS GRID IFRAME
# --------------------------------------------------
if filtered_projects:
    label_secao = f"Aplicações Ativas — {st.session_state.selected_category}" if st.session_state.selected_category != "Todos" else "Todas as Aplicações"
    st.markdown(f'<div class="section-label">{label_secao}</div>', unsafe_allow_html=True)
    
    # Geração das strings de cada card interno do Grid com links de compartilhamento dinâmicos
    cards_html = ""
    for p in filtered_projects:
        # Codificação de URLs para os links de compartilhamento
        texto_share = f"Confira o projeto '{p['title']}' no portfólio do Rodrigo Aiosa: {p['url']}"
        url_encoded_text = urllib.parse.quote(texto_share)
        url_encoded_link = urllib.parse.quote(p['url'])
        
        share_whatsapp = f"https://api.whatsapp.com/send?text={url_encoded_text}"
        share_linkedin = f"https://www.linkedin.com/sharing/share-offsite/?url={url_encoded_link}"
        
        cards_html += f"""
        <div class="project-card">
            <div class="project-content">
                <div class="card-badge">{p['category']}</div>
                <div class="project-title">{p['title']}</div>
                <div class="project-description">{p['desc']}</div>
            </div>
            <div class="project-footer">
                <a href="{p['url']}" target="_blank" class="project-button">
                    Acessar Aplicação →
                </a>
                <div class="share-group">
                    <a href="{share_whatsapp}" target="_blank" class="share-btn whatsapp" title="Compartilhar no WhatsApp">
                        <svg viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.4.01 12.008.01c3.202.001 6.212 1.246 8.477 3.516 2.266 2.27 3.51 5.284 3.508 8.492-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.502-5.713-1.455L0 24zm6.79-4.367l.388.23c1.53.91 3.29 1.391 5.108 1.392 5.584 0 10.126-4.544 10.129-10.13.001-2.705-1.052-5.247-2.966-7.161C17.59 1.95 15.05 .893 12.012.893c-5.59 0-10.134 4.545-10.138 10.13-.001 1.93.501 3.81 1.456 5.516l.25.445-.999 3.648 3.733-.981zm11.374-6.758c-.3-.15-1.774-.875-2.046-.975-.27-.1-.466-.15-.66.15-.194.3-.75.945-.919 1.144-.169.2-.338.225-.638.075-.3-.15-1.265-.467-2.41-1.487-.893-.797-1.495-1.783-1.67-2.083-.174-.3-.019-.462.131-.61.135-.134.3-.349.449-.523.149-.174.199-.3.299-.5.1-.2.05-.375-.025-.525-.075-.15-.66-1.59-.905-2.179-.239-.574-.481-.497-.66-.505-.169-.008-.363-.009-.557-.009-.194 0-.51.073-.777.362-.267.289-1.02 1.01-1.02 2.461 0 1.451 1.056 2.853 1.203 3.052.148.2 2.077 3.173 5.032 4.45 1.704.733 2.336.856 3.17.733.512-.075 1.775-.726 2.026-1.427.25-.7 2.5-3.3 2.1-3.4-.25-.1-.725-.35-1.025-.5z"/></svg>
                    </a>
                    <a href="{share_linkedin}" target="_blank" class="share-btn linkedin" title="Compartilhar no LinkedIn">
                        <svg viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                    </a>
                </div>
            </div>
        </div>
        """

    # Montagem do HTML isolado com tratamento robusto de alturas e botões extras
    component_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            background-color: transparent;
            font-family: 'DM Sans', sans-serif;
            overflow: hidden;
            padding: 15px 0 25px 0; 
        }}
        
        .projects-grid-container {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 32px;
            width: 100%;
        }}
        
        @media (max-width: 900px) {{
            .projects-grid-container {{ grid-template-columns: repeat(2, 1fr); }}
        }}
        @media (max-width: 600px) {{
            .projects-grid-container {{ grid-template-columns: 1fr; }}
        }}
        
        .project-card {{
            background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.3) 100%);
            padding: 28px;
            border-radius: 16px;
            border: 1px solid rgba(255,255,255,0.06);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
            transition: transform 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
        }}
        
        .project-card:hover {{
            transform: translateY(-5px);
            border-color: rgba(0,180,216,0.4);
            box-shadow: 0 12px 30px rgba(0,180,216,0.1);
        }}
        
        .card-badge {{
            display: inline-block;
            font-family: 'Syne', sans-serif;
            font-size: 0.65rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: rgba(0, 180, 216, 0.85);
            background: rgba(0, 180, 216, 0.05);
            border: 1px solid rgba(0, 180, 216, 0.2);
            padding: 4px 10px;
            border-radius: 6px;
            margin-bottom: 16px;
        }}
        
        .project-title {{
            font-family: 'Syne', sans-serif;
            font-size: 1.15rem;
            font-weight: 700;
            color: #f0f4ff;
            margin-bottom: 12px;
            line-height: 1.35;
        }}
        
        .project-description {{
            color: #94a3b8;
            font-size: 0.88rem;
            font-weight: 300;
            line-height: 1.6;
            margin-bottom: 28px;
        }}
        
        /* Rodapé unificado para o Botão e os Compartilhamentos */
        .project-footer {{
            margin-top: auto;
            display: flex;
            align-items: center;
            gap: 12px;
            width: 100%;
        }}
        
        .project-button {{
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #00b4d8 0%, #0077b6 100%);
            color: #ffffff;
            font-family: 'Syne', sans-serif;
            font-weight: 700;
            font-size: 0.85rem;
            letter-spacing: 0.5px;
            padding: 12px;
            border-radius: 10px;
            text-decoration: none;
            transition: opacity 0.3s ease;
            white-space: nowrap;
        }}
        
        .project-button:hover {{
            opacity: 0.9;
        }}
        
        .share-group {{
            display: flex;
            gap: 8px;
        }}
        
        .share-btn {{
            display: flex;
            align-items: center;
            justify-content: center;
            width: 38px;
            height: 38px;
            border-radius: 10px;
            border: 1px solid rgba(255,255,255,0.08);
            background: rgba(255,255,255,0.02);
            transition: all 0.3s ease;
            text-decoration: none;
        }}
        
        .share-btn svg {{
            width: 16px;
            height: 16px;
            fill: #94a3b8;
            transition: fill 0.3s ease;
        }}
        
        .share-btn:hover {{
            border-color: rgba(0,180,216,0.3);
            background: rgba(0,180,216,0.05);
        }}
        
        .share-btn.whatsapp:hover svg {{
            fill: #25D366;
        }}
        
        .share-btn.linkedin:hover svg {{
            fill: #0077B5;
        }}
        </style>
    </head>
    <body>
        <div class="projects-grid-container">
            {cards_html}
        </div>
    </body>
    </html>
    """
    
    # Cálculo dinâmico reajustado para evitar QUALQUER tipo de corte nos cards inferiores
    linhas = (len(filtered_projects) + 2) // 3
    # Aumentado o multiplicador de linha para 365 para acomodar com segurança o novo rodapé de ações
    altura_calculada = (linhas * 365) + 40 
    
    st.components.v1.html(component_code, height=altura_calculada, scrolling=False)

else:
    st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon" style="text-align:center; font-size:2.5rem; margin-top:30px;">🔍</div>
            <div class="empty-state-title" style="text-align:center; color:#f0f4ff; font-weight:600; margin-top:10px;">Nenhum projeto encontrado nesta categoria.</div>
            <div class="empty-state-sub" style="text-align:center; color:#64748b; font-size:0.88rem; margin-top:5px;">Tente mudar a categoria selecionada ou limpe os termos pesquisados.</div>
        </div>
    """, unsafe_allow_html=True)

st.write("")
exibir_rodape()
