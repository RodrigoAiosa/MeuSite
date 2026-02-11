import streamlit as st
from utils import registrar_acesso, exibir_rodape

# --------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------
st.set_page_config(
    page_title="Portfólio Rodrigo Aiosa",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# ESTILO SIDEBAR
# --------------------------------------------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: rgb(38, 38, 48) !important;
    }
    
    [data-testid="stSidebarNav"] {
        background-color: rgb(38, 38, 48) !important;
        padding-top: 10px;
    }

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
        color: white !important;
    }

    [data-testid="stSidebarNav"] ul li a:hover {
        background-color: rgba(0, 180, 216, 0.1) !important;
        border: 1px solid #00b4d8;
        transform: translateX(5px);
    }

    [data-testid="stSidebarNav"] ul li a[aria-current="page"] {
        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%) !important;
        color: white !important;
        font-weight: bold;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DEFINIÇÃO DAS PÁGINAS
# --------------------------------------------------
sobre_page = st.Page("Views/sobre.py", title="Sobre Mim", icon=":material/account_circle:", default=True)
projeto_recente_page = st.Page("Views/projetos_recentes.py", title="Projeto Recente", icon=":material/history:")
cases_sucesso_page = st.Page("Views/cases_sucesso.py", title="Cases de Sucesso", icon=":material/emoji_events:")

projeto_python_page = st.Page("Views/projetos_python.py", title="Projetos Python", icon=":material/code:")
projeto_powerbi_page = st.Page("Views/projetos_powerbi.py", title="Projetos Power BI", icon=":material/bar_chart:")

# 🔥 NOVA PÁGINA
postagem_linkedin_page = st.Page(
    "Views/postagem_linkedin.py",
    title="Postagem Linkedin",
    icon=":material/article:"
)

treinamento_empresa_page = st.Page("Views/treinamento_empresa.py", title="Para Empresas", icon=":material/school:")
cursos_online_page = st.Page("Views/cursos_online.py", title="Cursos Online", icon=":material/local_library:")
contato = st.Page("Views/contato.py", title="Contato", icon=":material/mail:")

# --------------------------------------------------
# NAVEGAÇÃO
# --------------------------------------------------
navigation_dict = {
    "Informações": [sobre_page, projeto_recente_page],
    "Resultados": [cases_sucesso_page],
    "Portifólio": [
        projeto_python_page,
        projeto_powerbi_page,
        postagem_linkedin_page  # ✅ Adicionado aqui
    ],
    "Treinamentos": [treinamento_empresa_page, cursos_online_page],
    "Entre em contato": [contato]
}

pg = st.navigation(navigation_dict)

# --------------------------------------------------
# REGISTRO DE ACESSO (backend)
# --------------------------------------------------
try:
    registrar_acesso(pg.title)
except Exception:
    pass

# --------------------------------------------------
# SIDEBAR LIMPA
# --------------------------------------------------
with st.sidebar:
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)

pg.run()
