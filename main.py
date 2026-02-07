import streamlit as st

# --- CONFIGURAÇÃO DAS PÁGINAS ---
# Mapeando os arquivos da sua pasta Views

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

# --- MENU DE NAVEGAÇÃO ---
# Corrigido: Adicionado vírgulas e nomes de variáveis corretos
pg = st.navigation(
    {
        "Informações": [sobre_page, projeto_recente_page],
        "Portfólio": [projeto_python_page, projeto_powerbi_page],
    }
)

# Configuração da aba do navegador
st.set_page_config(page_title="Portfólio Rodrigo Aiosa", page_icon="📊", layout="wide")

# Executa o app
pg.run()