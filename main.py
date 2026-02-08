import streamlit as st



# 1. Configuração da aba do navegador

st.set_page_config(page_title="Portfólio Rodrigo Aiosa", page_icon="📊", layout="wide")



# --- ESTILO CSS PARA A BARRA LATERAL (COR RGB 38, 38, 48) ---

st.markdown(

    """

    <style>

    /* Alterando a cor de fundo de toda a barra lateral */

    [data-testid="stSidebar"] {

        background-color: rgb(38, 38, 48) !important;

    }



    /* Garantir que o container de navegação siga a mesma cor */

    [data-testid="stSidebarNav"] {

        background-color: rgb(38, 38, 48) !important;

        padding-top: 20px;

    }



    /* Estilizando os botões para ficarem vazados com o novo fundo */

    [data-testid="stSidebarNav"] ul li a {

        background-color: transparent !important;

        border-radius: 12px;

        margin: 8px 15px;

        padding: 12px 15px;

        border: 1px solid rgba(0, 180, 216, 0.4); /* Borda azul um pouco mais visível */

        transition: all 0.3s ease;

        text-decoration: none !important;

        display: flex;

        align-items: center;

    }



    /* Efeito de Hover */

    [data-testid="stSidebarNav"] ul li a:hover {

        background-color: rgba(255, 255, 255, 0.05) !important; /* Leve brilho branco no fundo novo */

        border-color: #00b4d8;

        transform: translateX(5px);

    }



    /* Página Ativa (Mantendo seu azul de destaque) */

    [data-testid="stSidebarNav"] ul li a[aria-current="page"] {

        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%) !important;

        color: white !important;

        font-weight: bold;

        border: none;

        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.4);

    }



    /* Texto dos botões */

    [data-testid="stSidebarNav"] ul li a span {

        color: #f0f0f0 !important;

    }



    /* Títulos das seções (INFORMAÇÕES, PORTFÓLIO...) */

    [data-testid="stSidebarNav"] > div:first-child:after {

        color: #00b4d8 !important;

    }

   

    /* Ajuste para os títulos de categoria nativos do Streamlit */

    .st-emotion-cache-1ky8hqv {

        color: #00b4d8 !important;

        background-color: transparent !important;

    }



    /* Remove a linha divisória para um look mais clean */

    [data-testid="stSidebarNavSeparator"] {

        display: none;

    }

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

    title="Treinamento para Empresas",

    icon=":material/school:",

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