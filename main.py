import streamlit as st
from utils import registrar_acesso

# 1. Configuração da página - Deve ser a primeira instrução
st.set_page_config(
    page_title="Portfólio Rodrigo Aiosa", 
    page_icon="📊", 
    layout="wide"
)

# --- LÓGICA DE DADOS (Executa antes de tudo) ---
# Chamamos a função e já tratamos o formato com separador de milhar brasileiro
try:
    resultado_visitas = registrar_acesso(st.session_state.get("current_page", "Home"))
    if isinstance(resultado_visitas, (int, float)):
        # Formato: 117.649
        total_visitas = f"{int(resultado_visitas):,}".replace(",", ".")
    else:
        total_visitas = resultado_visitas 
except Exception:
    total_visitas = "except"

# --- ESTILO CSS (Otimizado para Mobile) ---
st.markdown("""
    <style>
    /* Sidebar Background */
    [data-testid="stSidebar"] {
        background-color: rgb(38, 38, 48) !important;
    }
    
    /* Menu de Navegação */
    [data-testid="stSidebarNav"] {
        background-color: rgb(38, 38, 48) !important;
        padding-top: 10px;
    }

    /* Itens do Menu */
    [data-testid="stSidebarNav"] ul li a {
        background-color: transparent !important;
        border-radius: 12px;
        margin: 8px 15px;
        padding: 12px 15px;
        border: 1px solid rgba(0, 180, 216, 0.4);
        color: white !important;
        text-decoration: none !important;
        display: flex;
        align-items: center;
    }

    /* CSS do Contador - Removido Fixed para funcionar no Mobile */
    .visitor-container-box {
        background: rgba(17, 25, 40, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 180, 216, 0.3);
        border-radius: 12px;
        padding: 15px;
        margin: 20px 15px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .status-pulse {
        height: 10px;
        width: 10px;
        background-color: #00ffcc;
        border-radius: 50%;
        box-shadow: 0 0 10px #00ffcc;
        animation: pulse-animation 2s infinite;
        flex-shrink: 0;
    }

    @keyframes pulse-animation {
        0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 204, 0.6); }
        70% { transform: scale(1); box-shadow: 0 0 0 6px rgba(0, 255, 204, 0); }
        100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(0, 255, 204, 0); }
    }

    .v-text {
        color: #a0aec0;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 2px;
    }

    .v-number {
        color: #ffffff;
        font-weight: 700;
        font-size: 18px;
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

# --- SIDEBAR (Renderização do Contador) ---
with st.sidebar:
    # Espaçador para o topo
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
    
    # Renderização do Badge
    st.markdown(f"""
        <div class="visitor-container-box">
            <div class="status-pulse"></div>
            <div>
                <div class="v-text">Visitas Totais</div>
                <div class="v-number">{total_visitas}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

# Execução da página
pg.run()



