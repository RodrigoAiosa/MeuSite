import streamlit as st
import time
import sys
import os

# --- AJUSTE DE CAMINHO ---
# Como sobre.py está em 'Views/', subimos um nível para encontrar 'utils.py' na raiz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils import registrar_acesso_db, exibir_rodape
except ImportError:
    st.error("Erro técnico: Não foi possível localizar as ferramentas de banco de dados.")

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(layout="wide", page_title="Portfolio | Rodrigo Aiosa")

# 2. REGISTRO DE ACESSO (PostgreSQL Aiven)
# Esta função utiliza o 'defaultdb' configurado no seu secrets.toml
registrar_acesso_db("Sobre Mim")

# --- ESTILO CSS GLOBAL ---
st.markdown(
    """
    <style>
    .profile-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: -30px;
        position: relative;
    }

    .profile-pic-border {
        position: relative;
        width: 210px;
        height: 210px;
        background: #151515;
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 50%;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    .profile-pic-border::before {
        content: '';
        position: absolute;
        width: 150%;
        height: 150%;
        background: conic-gradient(transparent, #00b4d8, #00b4d8, transparent 40%);
        animation: rotate-border 4s linear infinite;
    }

    .profile-pic-border img {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        z-index: 1;
        background-color: #151515;
        border: 2px solid #151515;
    }

    @keyframes rotate-border {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .main-title {
        text-align: center;
        margin-top: 10px;
    }

    /* CARDS FLIP */
    .cards-container {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        width: 100%;
    }

    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 180px;
        perspective: 1000px;
        margin-bottom: 20px;
        transition: transform 400ms, filter 400ms;
    }

    .flip-card:hover { transform: scale(1.1); z-index: 10; }

    .cards-container:hover .flip-card:not(:hover) {
        filter: blur(8px);
        transform: scale(0.9);
        opacity: 0.6;
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.6s;
        transform-style: preserve-3d;
        cursor: pointer;
    }

    .flip-card:hover .flip-card-inner { transform: rotateY(180deg); }

    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        backface-visibility: hidden;
        border-radius: 18px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
        border: 1px solid #1f2937;
    }

    .flip-card-front { background-color: #111827; color: white; }
    .flip-card-back {
        background-color: #00b4d8;
        color: #111827;
        transform: rotateY(180deg);
        font-weight: bold;
        font-size: 15px;
    }

    .card-icon { font-size:28px; margin-bottom:5px; }
    .card-number { font-size:26px; font-weight:bold; color:#00b4d8; }
    .card-title { font-size:14px; color:#9ca3af; }

    /* EXPERIÊNCIA CARDS */
    .exp-card {
        background-color: #111827;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00b4d8;
        height: 160px;
        transition: all 0.4s ease;
    }
    
    .exp-card:hover {
        transform: translateY(-10px);
        background-color: #1f2937;
        box-shadow: 0 10px 30px -5px rgba(0, 180, 216, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CONTEÚDO VISUAL ---
st.markdown(
    """
    <div class="profile-container">
        <div class="profile-pic-border">
            <img src="https://media.licdn.com/dms/image/v2/D5603AQFTfyqJswUYwg/profile-displayphoto-scale_200_200/B56ZxDaPuZK4AY-/0/1770657482765?e=1772064000&v=beta&t=1PXFrPJTt5w46Y7NUTgqCQ3H2jjMmkE1QwFi-lwwwko">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="main-title">Rodrigo Aiosa</h1>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; color: #00b4d8; font-weight: bold;">Python | Excel | Power BI | ETL | SQL SERVER</div>', unsafe_allow_html=True)

st.write("")

# --- CONTADORES ANIMADOS ---
st.markdown("### ⭐ Experiência e Resultados")
card_placeholders = st.empty()

for i in range(0, 101, 10):
    v_exp, v_emp, v_proj, v_rec = int(20*i/100), int(450*i/100), int(500*i/100), int(87*i/100)
    html_cards = f"""
    <div class="cards-container">
        <div class="flip-card"><div class="flip-card-inner"><div class="flip-card-front">🏆<br>{v_exp}+<br>Anos</div><div class="flip-card-back">Especialista em Automação</div></div></div>
        <div class="flip-card"><div class="flip-card-inner"><div class="flip-card-front">🏢<br>{v_emp}+<br>Empresas</div><div class="flip-card-back">Soluções Corporativas</div></div></div>
        <div class="flip-card"><div class="flip-card-inner"><div class="flip-card-front">📊<br>{v_proj}+<br>Projetos</div><div class="flip-card-back">Dashboards de Alto Nível</div></div></div>
        <div class="flip-card"><div class="flip-card-inner"><div class="flip-card-front">🤝<br>{v_rec}%<br>Retenção</div><div class="flip-card-back">Confiança e Resultados</div></div></div>
    </div>
    """
    card_placeholders.markdown(html_cards, unsafe_allow_html=True)
    time.sleep(0.01)

st.markdown("---")

# --- EXPERIÊNCIA DE MERCADO ---
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="exp-card"><h3>🔎 Análise e Automação</h3><p>Scripts Python e modelos Excel para otimização.</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="exp-card"><h3>📊 Power BI e DAX</h3><p>Ecossistemas de dados robustos e estratégicos.</p></div>', unsafe_allow_html=True)

st.write("")
col_img1, col_img2, col_img3 = st.columns([1, 8, 1])
with col_img2:
    st.image("assets/clientes_atendidos.jpg", use_container_width=True)

# --- RODAPÉ ---
exibir_rodape()
