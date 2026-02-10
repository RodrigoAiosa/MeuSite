import streamlit as st
from utils import registrar_acesso, exibir_rodape

# 1. Configuração da página
st.set_page_config(
    page_title="Portfólio Rodrigo Aiosa", 
    page_icon="📊", 
    layout="wide"
)

# --- INICIALIZAÇÃO DA MEMÓRIA DO CONTADOR ---
if "ultimo_valor_valido" not in st.session_state:
    st.session_state["ultimo_valor_valido"] = "---"

# --- ESTILO CSS COMPLETO ---
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

    .visitor-container-box {
        background: rgba(17, 25, 40, 0.85);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 180, 216, 0.3);
        border-radius: 12px;
        padding: 15px;
        margin: 15px;
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .status-pulse {
        height: 10px; width: 10px;
        background-color: #00ffcc;
        border-radius: 50%;
        box-shadow: 0 0 10px #00ffcc;
        animation: pulse-animation 2s infinite;
        flex-shrink: 0;
    }

    @keyframes pulse-animation {
        0% { transform: scale(0.95); opacity: 0.7; }
        70% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(0.95); opacity: 0.7; }
    }

    .v-text {
        color: #a0aec0;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1.2px;
    }

    .v-number {
        color: #ffffff;
        font-weight: 700;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DEFINIÇÃO DAS PÁGINAS (CONTATO REMOVIDO) ---
sobre_page = st.Page(page="Views/sobre.py", title="Sobre Mim", icon=":material/account_circle:", default=True)
projeto_recente_page = st.Page(page="Views/projetos_recentes.py", title="Projeto Recente", icon=":material/history:")
cases_sucesso_page = st.Page(page="Views/cases_sucesso.py", title="Cases de Sucesso", icon=":material/emoji_events:")
projeto_python_page = st.Page(page="Views/projetos_python.py", title="Projetos Python", icon=":material/code:")
projeto_powerbi_page = st.Page(page="Views/projetos_powerbi.py", title="Projetos Power BI", icon=":material/bar_chart:")
treinamento_empresa_page = st.Page(page="Views/treinamento_empresa.py", title="Para Empresas", icon=":material/school:")
cursos_online_page = st.Page(page="Views/cursos_online.py", title="Cursos Online", icon=":material/local_library:")

# --- NAVEGAÇÃO ---
navigation_dict = {
    "Informações": [sobre_page, projeto_recente_page],
    "Resultados": [cases_sucesso_page],
    "Portifólio": [projeto_python_page, projeto_powerbi_page],
    "Treinamentos": [treinamento_empresa_page, cursos_online_page]
}

pg = st.navigation(navigation_dict)

# --- LÓGICA DO CONTADOR ---
try:
    res = registrar_acesso(pg.title)
    if res and str(res).isdigit() and int(res) > 0:
        valor_formatado = f"{int(res):,}".replace(",", ".")
        st.session_state["ultimo_valor_valido"] = valor_formatado
except Exception:
    pass

total_visitas = st.session_state["ultimo_valor_valido"]

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
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

pg.run()
exibir_rodape()
