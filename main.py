import streamlit as st
from utils import registrar_acesso

# Configuração da página
st.set_page_config(page_title="Portfólio Rodrigo Aiosa", page_icon="📊", layout="wide")

# Estilo CSS
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: rgb(38, 38, 48) !important; }
    .visitor-container-box {
        background: rgba(17, 25, 40, 0.8);
        border: 1px solid rgba(0, 180, 216, 0.3);
        border-radius: 12px;
        padding: 15px;
        margin: 10px 15px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .status-pulse {
        height: 10px; width: 10px;
        background-color: #00ffcc;
        border-radius: 50%;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { opacity: 0.4; }
        50% { opacity: 1; }
        100% { opacity: 0.4; }
    }
    .v-text { color: #a0aec0; font-size: 10px; text-transform: uppercase; }
    .v-number { color: #ffffff; font-weight: 700; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

# Definição das Páginas
sobre_page = st.Page(page="Views/sobre.py", title="Sobre Mim", icon=":material/account_circle:", default=True)
contato_page = st.Page(page="Views/contato.py", title="Contato", icon=":material/mail:")
# ... adicione as outras conforme seu arquivo

pg = st.navigation({"Menu": [sobre_page, contato_page]})

# LÓGICA DE VISITAS
res = registrar_acesso(pg.title)

# Formatação Milhar (Ex: 117.649)
if str(res).isdigit():
    total_visitas = f"{int(res):,}".replace(",", ".")
else:
    total_visitas = "---"

# SIDEBAR
with st.sidebar:
    st.markdown(f"""
        <div class="visitor-container-box">
            <div class="status-pulse"></div>
            <div>
                <div class="v-text">Visitas Totais</div>
                <div class="v-number">{total_visitas}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

pg.run()
