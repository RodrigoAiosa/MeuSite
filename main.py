import streamlit as st

# 1. Configuração da aba do navegador
st.set_page_config(page_title="Portfólio Rodrigo Aiosa", page_icon="📊", layout="wide")

# --- ESTILO CSS PARA A BARRA LATERAL (MANTIDO) ---
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] { background-color: rgb(38, 38, 48) !important; }
    [data-testid="stSidebarNav"] { background-color: rgb(38, 38, 48) !important; padding-top: 20px; }
    [data-testid="stSidebarNav"] ul li a {
        background-color: transparent !important;
        border-radius: 12px;
        margin: 8px 15px;
        padding: 12px 15px;
        border: 1px solid rgba(0, 180, 216, 0.4);
        transition: all 0.3s ease;
        text-decoration: none !important;
        display: flex;
        align-items: center;
    }
    [data-testid="stSidebarNav"] ul li a:hover {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-color: #00b4d8;
        transform: translateX(5px);
    }
    [data-testid="stSidebarNav"] ul li a[aria-current="page"] {
        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%) !important;
        color: white !important;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.4);
    }
    [data-testid="stSidebarNav"] ul li a span { color: #f0f0f0 !important; }
    .st-emotion-cache-1ky8hqv { color: #00b4d8 !important; background-color: transparent !important; }
    [data-testid="stSidebarNavSeparator"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CONFIGURAÇÃO DAS PÁGINAS ---

sobre_page = st.Page(
    page="Views/sobre.py",
    title="Sobre Mim",
    icon=":material/account_circle:",
    default=True,
)

projeto_recente_page = st.Page(
    page="Views/projetos_recentes.py",
    title="Projeto Recente",
    icon=":material/history:",
)

contato_page = st.Page(
    page="Views/contato.py",
    title="Contato",
    icon=":material/mail:",
)

cases_sucesso_page = st.Page(
    page="Views/cases_sucesso.py",
    title="Cases de Sucesso",
    icon=":material/emoji_events:",
)

projeto_python_page = st.Page(
    page="Views/projetos_python.py",
    title="Projetos Python",
    icon=":material/code:",
)

projeto_powerbi_page = st.Page(
    page="Views/projetos_powerbi.py",
    title="Projetos Power BI",
    icon=":material/bar_chart:",
)

treinamento_empresa_page = st.Page(
    page="Views/treinamento_empresa.py",
    title="Para Empresas",
    icon=":material/school:",
)

# --- NOVA PÁGINA ADICIONADA AQUI ---
cursos_online_page = st.Page(
    page="Views/cursos_online.py",
    title="Cursos Online",
    icon=":material/local_library:",
)

# --- MENU DE NAVEGAÇÃO ATUALIZADO ---
pg = st.navigation(
    {
        "Informações": [sobre_page, projeto_recente_page, contato_page],
        "Resultados": [cases_sucesso_page],
        "Portfólio": [projeto_python_page, projeto_powerbi_page],
        "Treinamentos": [treinamento_empresa_page, cursos_online_page] # Adicionado aqui
    }
)

# Executa o app
pg.run()