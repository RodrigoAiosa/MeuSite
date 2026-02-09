import streamlit as st
from utils import registrar_acesso, exibir_rodape

# 1. Configuração da página - Resolve avisos de 2026
st.set_page_config(
    page_title="Portfólio Rodrigo Aiosa", 
    page_icon="📊", 
    layout="wide"
)

# --- ESTILO CSS COMPLETO (Sidebar, Hover e Ajustes de Layout) ---
st.markdown("""
    <style>
    /* Estilização da Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgb(38, 38, 48) !important;
    }
    
    /* Estilização dos itens do Menu de Navegação */
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

    /* Item Ativo (Página Atual) */
    [data-testid="stSidebarNav"] ul li a[aria-current="page"] {
        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%) !important;
        color: white !important;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.3);
    }

    /* Títulos de Categorias na Navegação */
    [data-testid="stSidebarNav"] [data-testid="stSidebarNavSeparator"] + div {
        color: #00b4d8 !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 1px;
        margin-left: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DEFINIÇÃO DAS PÁGINAS ---
sobre_page = st.Page(
    page="Views/sobre.py", 
    title="Sobre Mim", 
    icon=":material/account_circle:", 
    default=True
)

projeto_recente_page = st.Page(
    page="Views/projetos_recentes.py", 
    title="Projeto Recente", 
    icon=":material/history:"
)

contato_page = st.Page(
    page="Views/contato.py", 
    title="Contato", 
    icon=":material/mail:"
)

cases_sucesso_page = st.Page(
    page="Views/cases_sucesso.py", 
    title="Cases de Sucesso", 
    icon=":material/emoji_events:"
)

projeto_python_page = st.Page(
    page="Views/projetos_python.py", 
    title="Projetos Python", 
    icon=":material/code:"
)

projeto_powerbi_page = st.Page(
    page="Views/projetos_powerbi.py", 
    title="Projetos Power BI", 
    icon=":material/bar_chart:"
)

treinamento_empresa_page = st.Page(
    page="Views/treinamento_empresa.py", 
    title="Para Empresas", 
    icon=":material/school:"
)

cursos_online_page = st.Page(
    page="Views/cursos_online.py", 
    title="Cursos Online", 
    icon=":material/local_library:"
)

# --- NAVEGAÇÃO ESTRUTURADA ---
pg = st.navigation({
    "Informações": [sobre_page, projeto_recente_page, contato_page],
    "Resultados": [cases_sucesso_page],
    "Portifólio": [projeto_python_page, projeto_powerbi_page],
    "Treinamentos": [treinamento_empresa_page, cursos_online_page]
})

# --- EXECUÇÃO ---
# 1. Registra o acesso da página atual na planilha antes de carregar
registrar_acesso(st.session_state.get("current_page", "Início"))

# 2. Carrega a página selecionada
pg.run()

# 3. Exibe o rodapé em todas as páginas automaticamente
exibir_rodape()
