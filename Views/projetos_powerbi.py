import streamlit as st
from utils import exibir_rodape


# --- ESTILO CSS AJUSTADO (TEXTOS MAIORES) ---
st.markdown(
    """
    <style>
    .pbi-card-link {
        text-decoration: none !important;
        color: inherit;
    }

    .pbi-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 18px;
        padding: 35px 20px; /* Aumentado o padding */
        height: 300px; /* Aumentado para acomodar textos maiores */
        transition: all 0.4s ease;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        cursor: pointer;
    }
    
    .pbi-card:hover {
        transform: translateY(-10px);
        border: 1px solid #00b4d8;
        box-shadow: 0 15px 35px rgba(0, 180, 216, 0.25);
    }

    /* Ícone maior */
    .card-icon { font-size: 60px; margin-bottom: 15px; }

    /* Título do Card maior */
    .pbi-card-title { 
        color: #ffffff; 
        font-size: 1.4rem; /* Aumentado de 1.1 para 1.4 */
        font-weight: bold; 
        line-height: 1.3;
    }

    /* Link "Acessar" maior */
    .pbi-card-tag { 
        margin-top: 20px; 
        font-size: 0.9rem; /* Aumentado */
        color: #00b4d8; 
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    [data-testid="column"] {
        padding: 0 15px !important;
    }

    /* Estilo para a seção de Artigos */
    .article-container {
        margin-bottom: 25px;
        text-decoration: none !important;
        display: block;
    }

    .article-card {
        background-color: #111827;
        padding: 30px;
        border-radius: 15px;
        border-left: 8px solid #00b4d8;
        transition: all 0.3s ease;
    }

    /* Título do Artigo maior */
    .article-title {
        font-size: 1.6rem !important; /* Aumentado */
        color: white !important;
        margin: 0;
        font-weight: bold;
    }

    /* Descrição do Artigo maior */
    .article-desc {
        color: #9ca3af;
        margin-top: 12px;
        font-size: 1.1rem; /* Aumentado */
        line-height: 1.5;
    }

    .article-card:hover {
        background-color: #1a2233;
        transform: translateX(12px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; font-size: 3rem;'>📊 Dashboards Estratégicos</h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 1.2rem;'>Clique nos cards abaixo para interagir com os relatórios em tempo real.</p>", unsafe_allow_html=True)
st.write("")

# --- DADOS DOS PROJETOS ---
pbi_projects = [
    {"title": "💳 Relatório STONE", "icon": "🏛️",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9"},
    {"title": "📊 Vendas Meta vs Realizado", "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9"},
    {"title": "📦 Controle de Pedidos BNZ", "icon": "📦",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9"},
    {"title": "🎯 Análise Dados Estratégica", "icon": "🎯",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9"},
    {"title": "👥 People Analytics (RH)", "icon": "👥",
     "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9"},
    {"title": "🚀 Gestão de Negócios", "icon": "🚀",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9"}
]

# --- RENDERIZAÇÃO DOS CARDS ---
for i in range(0, len(pbi_projects), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(pbi_projects):
            project = pbi_projects[i + j]
            with cols[j]:
                st.markdown(f"""
                <a href="{project['url']}" target="_blank" class="pbi-card-link">
                    <div class="pbi-card">
                        <div class="card-icon">{project['icon']}</div>
                        <div class="pbi-card-title">{project['title']}</div>
                        <div class="pbi-card-tag">ACESSAR DASHBOARD ↗️</div>
                    </div>
                </a>
                """, unsafe_allow_html=True)

    # PULO DE DUAS LINHAS ENTRE FILEIRAS
    if i == 0:
        st.write("")
        st.write("")

st.write("")
st.markdown("---")

# --- CONTEÚDO TÉCNICO & ARTIGOS ---
st.markdown("<h2 style='font-size: 2.2rem;'>💡 Conteúdo Técnico & Artigos</h2>",
            unsafe_allow_html=True)

# Artigo 1: Conexão Banco de Dados
st.markdown("""
    <a href="https://www.linkedin.com/feed/update/urn:li:activity:7406927292955865088" target="_blank" class="article-container">
        <div class="article-card">
            <h4 class="article-title">🚀 Técnicas avançadas em BI: conectando relatórios ao banco de dados com performance</h4>
            <p class="article-desc">Estratégias para otimizar a latência e garantir a integridade dos dados em conexões diretas.</p>
        </div>
    </a>
""", unsafe_allow_html=True)

# Artigo 2: DAX
st.markdown("""
    <a href="https://www.linkedin.com/feed/update/urn:li:activity:7287584764490891266" target="_blank" class="article-container">
        <div class="article-card">
            <h4 class="article-title">☑️ A Revolução das Medidas DAX no Power BI</h4>
            <p class="article-desc">Aprenda como otimizar seus modelos de dados com técnicas avançadas de cálculo.</p>
        </div>
    </a>
""", unsafe_allow_html=True)

exibir_rodape()
