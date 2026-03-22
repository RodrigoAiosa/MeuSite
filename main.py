import streamlit as st
from utils import registrar_acesso, exibir_rodape

# 1. Configuração da página
st.set_page_config(
    page_title="Portfólio Rodrigo Aiosa",
    page_icon="🦉",
    layout="wide"
)

# --- ESTILO CSS MODERNO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Space+Grotesk:wght@400;500;600&display=swap');

    /* ── Fundo e base da Sidebar ── */
    [data-testid="stSidebar"],
    [data-testid="stSidebarNav"] {
        background-color: #0d0d14 !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* ── Scrollbar fina na sidebar ── */
    [data-testid="stSidebar"]::-webkit-scrollbar { width: 3px; }
    [data-testid="stSidebar"]::-webkit-scrollbar-track { background: transparent; }
    [data-testid="stSidebar"]::-webkit-scrollbar-thumb { background: rgba(0, 180, 216, 0.3); border-radius: 10px; }

    /* ── Títulos de seção (categorias do menu) ── */
    [data-testid="stSidebarNavSeparator"] + div span,
    [data-testid="stSidebarNavItems"] > div > div > span {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.68rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.12em !important;
        text-transform: uppercase !important;
        color: rgba(0, 180, 216, 0.55) !important;
        padding: 18px 20px 6px !important;
        display: block !important;
    }

    /* ── Itens de navegação ── */
    [data-testid="stSidebarNav"] ul {
        padding: 0 10px !important;
        gap: 2px !important;
        display: flex;
        flex-direction: column;
    }

    [data-testid="stSidebarNav"] ul li a {
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.875rem !important;
        font-weight: 400 !important;
        color: rgba(210, 220, 240, 0.75) !important;
        background-color: transparent !important;
        border-radius: 8px !important;
        margin: 1px 0 !important;
        padding: 9px 14px !important;
        border: none !important;
        transition: background 0.2s ease, color 0.2s ease, padding-left 0.2s ease !important;
        text-decoration: none !important;
        display: flex !important;
        align-items: center !important;
        gap: 10px !important;
        position: relative !important;
        letter-spacing: 0.01em !important;
    }

    /* Ícones dos itens */
    [data-testid="stSidebarNav"] ul li a span {
        font-size: 1rem !important;
        color: rgba(180, 200, 230, 0.5) !important;
        transition: color 0.2s ease !important;
        flex-shrink: 0 !important;
    }

    /* ── Hover ── */
    [data-testid="stSidebarNav"] ul li a:hover {
        background-color: rgba(0, 180, 216, 0.07) !important;
        color: rgba(220, 235, 255, 0.95) !important;
        padding-left: 18px !important;
    }

    [data-testid="stSidebarNav"] ul li a:hover span {
        color: rgba(0, 180, 216, 0.8) !important;
    }

    /* ── Página ativa ── */
    [data-testid="stSidebarNav"] ul li a[aria-current="page"] {
        background: linear-gradient(
            105deg,
            rgba(0, 180, 216, 0.15) 0%,
            rgba(0, 119, 182, 0.08) 100%
        ) !important;
        color: #e8f4ff !important;
        font-weight: 500 !important;
        border: none !important;
        padding-left: 18px !important;
        box-shadow: inset 3px 0 0 #00b4d8 !important;
    }

    [data-testid="stSidebarNav"] ul li a[aria-current="page"] span {
        color: #00b4d8 !important;
    }

    /* ── Linha divisória entre seções ── */
    [data-testid="stSidebarNavSeparator"] {
        border: none !important;
        border-top: 1px solid rgba(255, 255, 255, 0.05) !important;
        margin: 8px 10px !important;
    }

    /* ── Logo / cabeçalho da sidebar ── */
    [data-testid="stSidebarHeader"] {
        background-color: #0d0d14 !important;
        border: none !important;
        box-shadow: none !important;
        padding-bottom: 12px !important;
    }

    /* ── Remove qualquer borda residual do Streamlit ── */
    [data-testid="stSidebar"] > div:first-child,
    [data-testid="stSidebar"] section {
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* ── Botão de toggle da sidebar ── */
    [data-testid="collapsedControl"] {
        background-color: rgba(0, 180, 216, 0.1) !important;
        border: 1px solid rgba(0, 180, 216, 0.2) !important;
        border-radius: 8px !important;
        color: #00b4d8 !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="collapsedControl"]:hover {
        background-color: rgba(0, 180, 216, 0.2) !important;
    }

    /* ── Estilo global da página principal ── */
    .main .block-container {
        font-family: 'DM Sans', sans-serif !important;
    }

    /* ── Botões do Streamlit ── */
    .stButton > button {
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        letter-spacing: 0.02em !important;
        border-radius: 8px !important;
        border: 1px solid rgba(0, 180, 216, 0.4) !important;
        background: transparent !important;
        color: #00b4d8 !important;
        padding: 0.45rem 1.2rem !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover {
        background: rgba(0, 180, 216, 0.1) !important;
        border-color: #00b4d8 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 14px rgba(0, 180, 216, 0.15) !important;
    }

    .stButton > button:active {
        transform: translateY(0) !important;
        box-shadow: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DEFINIÇÃO DAS PÁGINAS ---
sobre_page = st.Page(page="Views/sobre.py", title="Sobre Mim", icon="📝", default=True)
projeto_recente_page = st.Page(page="Views/projetos_recentes.py", title="Projeto Recente", icon="🗂️")
cases_sucesso_page = st.Page(page="Views/cases_sucesso.py", title="Cases de Sucesso", icon="🏆")
projeto_python_page = st.Page(page="Views/projetos_python.py", title="Projetos Python", icon="🚧")
projeto_powerbi_page = st.Page(page="Views/projetos_powerbi.py", title="Projetos Power BI", icon="📊")
treinamento_empresa_page = st.Page(page="Views/treinamento_empresa.py", title="Para Empresas", icon="📋")
cursos_online_page = st.Page(page="Views/cursos_online.py", title="Cursos Online", icon="🛜")
contato = st.Page(page="Views/contato.py", title="Contato", icon="📧")
AIOSAIA = st.Page(page="Views/AIosa_IA.py", title="AIOSA IA", icon="⚛️")
escola_sql = st.Page(page="Views/escola_sql.py", title="Escola SQL", icon="⚛️")
escola_python = st.Page(page="Views/escola_python.py", title="Escola Python", icon="⚛️")
escola_excel = st.Page(page="Views/escola_excel.py", title="Teclas de Atalho Excel", icon="⚛️")
curso_excel = st.Page(page="Views/curso_excel.py", title="Escola Excel", icon="⚛️")
gerar_dados_bi = st.Page(page="Views/gerar_dados_bi.py", title="Gerador Dados BI", icon="⚛️")

# --- NAVEGAÇÃO ---
navigation_dict = {
    "Informações": [sobre_page, projeto_recente_page],
    "Resultados": [cases_sucesso_page],
    "Portifólio": [projeto_python_page, projeto_powerbi_page],
    "Escola de Dados": [escola_sql, escola_python, escola_excel, curso_excel, gerar_dados_bi],
    "Treinamentos": [treinamento_empresa_page, cursos_online_page],
    "Entre em contato": [contato],
    "Assistente IA": [AIOSAIA]
}

pg = st.navigation(navigation_dict)

# --- LÓGICA DE REGISTRO ---
try:
    registrar_acesso(pg.title)
except Exception:
    pass

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

pg.run()
