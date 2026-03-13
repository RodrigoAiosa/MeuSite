import streamlit as st
from utils import registrar_acesso, exibir_rodape

# 1. Configuração da página
st.set_page_config(
    page_title="Portfólio Rodrigo Aiosa", 
    page_icon="🦉", 
    layout="wide"
)

# --- ESTILO CSS ATUALIZADO (Forçando visibilidade em qualquer tema) ---
st.markdown("""
    <style>
    /* Fundo da Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgb(38, 38, 48) !important;
    }
    
    [data-testid="stSidebarNav"] {
        background-color: rgb(38, 38, 48) !important;
        padding-top: 10px;
    }

    /* Títulos das Categorias (Informações, Resultados, etc.) */
    [data-testid="stSidebarNav"] [data-testid="stSidebarNavSeparator"] + div span {
        color: rgba(255, 255, 255, 0.8) !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        font-size: 0.85rem;
    }

    /* Estilo dos Links/Botões da Sidebar */
    [data-testid="stSidebarNav"] ul li a {
        background-color: transparent !important;
        border-radius: 12px;
        margin: 8px 15px;
        padding: 12px 15px;
        border: 1px solid rgba(0, 180, 216, 0.3) !important;
        transition: all 0.3s ease;
        text-decoration: none !important;
        display: flex;
        align-items: center;
        color: #FFFFFF !important; /* Força o texto sempre branco */
    }

    /* Força a cor dos ícones (Material Icons) */
    [data-testid="stSidebarNav"] ul li a span {
        color: #FFFFFF !important;
    }

    /* Efeito de Hover */
    [data-testid="stSidebarNav"] ul li a:hover {
        background-color: rgba(0, 180, 216, 0.1) !important;
        border: 1px solid #00b4d8 !important;
        transform: translateX(5px);
    }

    /* Página Ativa (Selecionada) */
    [data-testid="stSidebarNav"] ul li a[aria-current="page"] {
        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%) !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        border: none !important;
    }

    /* Força o ícone da página ativa a ser branco */
    [data-testid="stSidebarNav"] ul li a[aria-current="page"] span {
        color: #FFFFFF !important;
    }
    
    /* Remove a linha divisória padrão se houver */
    [data-testid="stSidebarNavSeparator"] {
        border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
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
#curso_sql = st.Page(page="Views/curso_sql.py", title="Curso SQL gratuíto", icon="📋")


# --- NAVEGAÇÃO ---
navigation_dict = {
    "Informações": [sobre_page, projeto_recente_page],
    "Resultados": [cases_sucesso_page],
    "Portifólio": [projeto_python_page, projeto_powerbi_page, escola_sql, escola_python],
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
