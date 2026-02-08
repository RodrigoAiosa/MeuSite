import streamlit as st

# Configuração da aba do navegador (DEVE SER A PRIMEIRA COISA)
st.set_page_config(page_title="Portfólio Rodrigo Aiosa", page_icon="📊", layout="wide")

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

# Corrigido: Variável única para Treinamento (antes estava sobrescrevendo projeto_powerbi_page)
treinamento_empresa_page = st.Page(
    page="Views/treinamento_empresa.py",
    title="Treinamento para Empresas",
    icon=":material/school:", # Alterado para ícone de escola/treino
)


# --- MENU DE NAVEGAÇÃO ---
pg = st.navigation(
    {
        "Informações": [sobre_page, projeto_recente_page, contato_page, treinamento_empresa_page],
        "Resultados": [cases_sucesso_page],
        "Portfólio": [projeto_python_page, projeto_powerbi_page],
    }
)

# Executa o app
pg.run()