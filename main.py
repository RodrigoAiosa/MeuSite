import streamlit as st
from utils import registrar_acesso

# 1. Configuração da página
st.set_page_config(
    page_title="Portfólio Rodrigo Aiosa", 
    page_icon="📊", 
    layout="wide"
)

# --- ESTILO CSS ATUALIZADO (Foco em Responsividade) ---
st.markdown("""
    <style>
    /* Estilização da Sidebar */
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

    /* Estilo do Contador Adaptado para Mobile */
    .visitor-counter {
        margin: 20px 15px; /* Margem lateral para não colar na borda no mobile */
        background: rgba(17, 25, 40, 0.75);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 12px 15px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .status-dot {
        height: 10px;
        width: 10px;
        background-color: #00ffcc;
        border-radius: 50%;
        box-shadow: 0 0 8px #00ffcc;
        animation: pulse 2s infinite;
        flex-shrink: 0; /* Impede que a bolinha amasse no mobile */
    }

    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 204, 0.7); }
        70% { transform: scale(1); box-shadow: 0 0 0 5px rgba(0, 255, 204, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 204, 0); }
    }

    .visitor-text {
        color: #a0aec0;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
        line-height: 1;
    }

    .visitor-count {
        color: #ffffff;
        font-weight: bold;
        font-size: 16px;
        font-family: 'Inter', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DEFINIÇÃO DAS PÁGINAS ---
sobre_page = st.Page(page="Views/sobre.py", title="Sobre Mim", icon=":material/account_circle:", default=True)
projeto_recente_page = st.Page(page="Views/projetos_recentes.py", title="Projeto Recente", icon=":material/history:")
contato_page = st.Page(page="Views/contato.py", title="Contato", icon=":material/mail:")
cases_sucesso_page = st.Page(page="Views/cases_sucesso.py", title="Cases de Sucesso", icon=":material/emoji_events:")
projeto_python_page = st.Page(page="Views/projetos_python.py", title="Projetos Python", icon=":material/code:")
projeto_powerbi_page = st.Page(page="Views/projetos_powerbi.py", title="Projetos Power BI", icon=":material/bar_chart:")
treinamento_empresa_page = st.Page(page="Views/treinamento_empresa.py", title="Para Empresas", icon=":material/school:")
cursos_online_page = st.Page(page="Views/cursos_online.py", title="Cursos Online", icon=":material/local_library:")

navigation_dict = {
    "Informações": [sobre_page, projeto_recente_page, contato_page],
    "Resultados": [cases_sucesso_page],
    "Portifólio": [projeto_python_page, projeto_powerbi_page],
    "Treinamentos": [treinamento_empresa_page, cursos_online_page]
}

pg = st.navigation(navigation_dict)

# --- LÓGICA DE ACESSO ---
resultado_visitas = registrar_acesso(pg.title)

# Formatação com ponto como separador de milhar (Ex: 117.649)
if isinstance(resultado_visitas, int):
    total_visitas = f"{resultado_visitas:,}".replace(",", ".")
else:
    total_visitas = "Carregando..."

# --- SIDEBAR ---
with st.sidebar:
    # Opcional: Adiciona um espaço flexível para empurrar o contador para o fundo
    st.markdown("<div style='height: 5vh;'></div>", unsafe_allow_html=True)
    
    # Badge do contador
    st.markdown(f"""
        <div class="visitor-counter">
            <span class="status-dot"></span>
            <div>
                <div class="visitor-text">Visitas Totais</div>
                <div class="visitor-count">{total_visitas}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

pg.run()
