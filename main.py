import streamlit as st
from utils import registrar_acesso, exibir_rodape

# 1. Configuração da página
st.set_page_config(
    page_title="Portfólio Rodrigo Aiosa",
    page_icon="🦉",
    layout="wide"
)

# --- ESTILO CSS: MENU HORIZONTAL NO TOPO ---
st.markdown("""
    <style>
    /* Esconde a sidebar completamente */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    [data-testid="collapsedControl"] {
        display: none !important;
    }

    /* Remove padding do topo do conteúdo principal */
    .block-container {
        padding-top: 0rem !important;
    }

    /* Barra de navegação horizontal */
    .top-nav {
        background: linear-gradient(90deg, rgb(18, 18, 28) 0%, rgb(28, 28, 42) 100%);
        border-bottom: 1px solid rgba(0, 180, 216, 0.3);
        padding: 0 20px;
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 4px;
        position: sticky;
        top: 0;
        z-index: 999;
        box-shadow: 0 2px 20px rgba(0, 180, 216, 0.15);
    }

    /* Logo / Título no nav */
    .nav-brand {
        color: #00b4d8;
        font-weight: 800;
        font-size: 1.1rem;
        padding: 14px 20px 14px 0;
        margin-right: 10px;
        border-right: 1px solid rgba(255,255,255,0.15);
        white-space: nowrap;
        letter-spacing: 0.5px;
    }

    /* Grupo de abas do menu */
    .nav-group {
        display: flex;
        align-items: center;
        gap: 2px;
    }

    /* Separador entre grupos */
    .nav-separator {
        width: 1px;
        height: 20px;
        background: rgba(255,255,255,0.15);
        margin: 0 6px;
    }

    /* Cada botão de navegação */
    .nav-link {
        color: rgba(255, 255, 255, 0.75) !important;
        text-decoration: none !important;
        padding: 10px 14px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 500;
        white-space: nowrap;
        display: flex;
        align-items: center;
        gap: 6px;
        transition: all 0.2s ease;
        border: 1px solid transparent;
        cursor: pointer;
    }
    .nav-link:hover {
        background-color: rgba(0, 180, 216, 0.12);
        border-color: rgba(0, 180, 216, 0.4);
        color: #fff !important;
    }
    .nav-link.active {
        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%);
        color: #FFFFFF !important;
        font-weight: 700;
        border-color: transparent;
    }

    /* Label do grupo (ex: "Portfólio") */
    .nav-label {
        color: rgba(255,255,255,0.35);
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding: 0 6px;
        align-self: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- DEFINIÇÃO DAS PÁGINAS ---
sobre_page              = st.Page(page="Views/sobre.py",              title="Sobre Mim",           icon="📝", default=True)
projeto_recente_page    = st.Page(page="Views/projetos_recentes.py",  title="Projeto Recente",     icon="🗂️")
cases_sucesso_page      = st.Page(page="Views/cases_sucesso.py",      title="Cases de Sucesso",    icon="🏆")
projeto_python_page     = st.Page(page="Views/projetos_python.py",    title="Projetos Python",     icon="🚧")
projeto_powerbi_page    = st.Page(page="Views/projetos_powerbi.py",   title="Projetos Power BI",   icon="📊")
treinamento_empresa_page= st.Page(page="Views/treinamento_empresa.py",title="Para Empresas",       icon="📋")
cursos_online_page      = st.Page(page="Views/cursos_online.py",      title="Cursos Online",       icon="🛜")
contato                 = st.Page(page="Views/contato.py",             title="Contato",             icon="📧")
AIOSAIA                 = st.Page(page="Views/AIosa_IA.py",            title="AIOSA IA",            icon="⚛️")
escola_sql              = st.Page(page="Views/escola_sql.py",          title="Escola SQL",          icon="⚛️")
escola_python           = st.Page(page="Views/escola_python.py",       title="Escola Python",       icon="⚛️")
escola_excel            = st.Page(page="Views/escola_excel.py",        title="Teclas Atalho Excel", icon="⚛️")
curso_excel             = st.Page(page="Views/curso_excel.py",         title="Escola Excel",        icon="⚛️")
gerar_dados_bi          = st.Page(page="Views/gerar_dados_bi.py",      title="Gerador Dados BI",    icon="⚛️")

# --- NAVEGAÇÃO (sidebar oculta via position="hidden") ---
navigation_dict = {
    "Informações":      [sobre_page, projeto_recente_page],
    "Resultados":       [cases_sucesso_page],
    "Portifólio":       [projeto_python_page, projeto_powerbi_page],
    "Treinamentos":     [treinamento_empresa_page, cursos_online_page, escola_sql,
                         escola_python, escola_excel, curso_excel, gerar_dados_bi],
    "Entre em contato": [contato],
    "Assistente IA":    [AIOSAIA],
}

pg = st.navigation(navigation_dict, position="hidden")

# --- REGISTRO DE ACESSO ---
try:
    registrar_acesso(pg.title)
except Exception:
    pass

# --- MONTA O MENU HORIZONTAL DINAMICAMENTE ---
# Mapeia título → objeto Page (para pegar a URL)
all_pages = []
for pages in navigation_dict.values():
    all_pages.extend(pages)

page_map = {p.title: p for p in all_pages}

# Ícones por título
icons = {p.title: p.icon for p in all_pages}

# Gera o HTML do menu
nav_html = '<div class="top-nav">'
nav_html += '<div class="nav-brand">🦉 Rodrigo Aiosa</div>'

for group_label, pages in navigation_dict.items():
    nav_html += '<div class="nav-group">'
    # Pequeno rótulo do grupo (opcional — remova se quiser mais limpo)
    # nav_html += f'<span class="nav-label">{group_label}</span>'
    for p in pages:
        is_active = (p.title == pg.title)
        active_cls = " active" if is_active else ""
        url = p.url if hasattr(p, "url") else "#"
        nav_html += (
            f'<a class="nav-link{active_cls}" href="{url}">'
            f'{icons.get(p.title, "")} {p.title}</a>'
        )
    nav_html += '</div>'
    nav_html += '<div class="nav-separator"></div>'

nav_html += '</div>'

st.markdown(nav_html, unsafe_allow_html=True)

# --- RODA A PÁGINA SELECIONADA ---
pg.run()
