import streamlit as st
import time
from utils import registrar_acesso, exibir_rodape

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(layout="wide", page_title="Portfolio | Rodrigo Aiosa")

# 2. REGISTRO DE ACESSO
registrar_acesso("Sobre Mim")

# --- ESTILO CSS GLOBAL ATUALIZADO ---
st.markdown(
    """
    <style>
    /* Container da Foto com Efeito de Borda Animada */
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

    /* --- NOVOS EFEITOS NOS CARDS --- */
    /* Container pai para aplicar o efeito de desfoque nos irmãos */
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
        transition: transform 400ms, filter 400ms; /* Transição suave para zoom e blur */
    }

    /* Efeito: Aumenta o card que está com o mouse em cima */
    .flip-card:hover {
        transform: scale(1.1);
        z-index: 10;
    }

    /* Efeito: Desfoca e diminui os outros cards quando um estiver em hover */
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

    .flip-card:hover .flip-card-inner {
        transform: rotateY(180deg);
    }

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

    .flip-card-front {
        background-color: #111827;
        color: white;
    }

    .flip-card-back {
        background-color: #00b4d8;
        color: #111827;
        transform: rotateY(180deg);
        font-weight: bold;
        font-size: 15px;
        line-height: 1.4;
    }

    .card-icon { font-size:28px; margin-bottom:5px; }
    .card-number { font-size:26px; font-weight:bold; color:#00b4d8; }
    .card-title { font-size:14px; color:#9ca3af; }

    /* TEXTO CENTRALIZADO */
    .centered-text {
        text-align: center;
        max-width: 900px;
        margin: 0 auto;
        font-size: 1.1em;
        color: #9ca3af;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CABEÇALHO ---
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
st.markdown('<div style="text-align: center; font-size: 1.2em; color: #00b4d8; font-weight: bold;">Python | Excel | Power BI | ETL | SQL SERVER | Linguagem M | DAX</div>', unsafe_allow_html=True)

st.write("")

# --- CARDS COM CONTADOR E EFEITOS DE HOVER ---
st.markdown("### ⭐ Experiência e Resultados")

# Criamos placeholders para os cards dentro da lógica de animação
# Para o efeito de "blur nos outros" funcionar no Streamlit, precisamos injetar o HTML em um único bloco ou garantir o container CSS.
# Como o Streamlit usa iframes e divs próprias, vamos envolver os placeholders em uma div personalizada.

card_placeholders = st.empty()

back_texts = [
    "Expertise em automação de processos e análise preditiva.",
    "Soluções personalizadas para grandes players do mercado.",
    "Dashboards estratégicos focados em KPIs de alto nível.",
    "Parceria contínua baseada em confiança e resultados reais."
]

# Loop de animação dos números
for i in range(0, 101, 5):
    val_exp = int(20 * i / 100)
    val_emp = int(450 * i / 100)
    val_proj = int(500 * i / 100)
    val_rec = int(87 * i / 100)

    # Construindo o HTML de todos os cards juntos para respeitar o seletor CSS de "irmãos"
    html_cards = f"""
    <div class="cards-container">
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <div class="card-icon">🏆</div>
                    <div class="card-number">{val_exp}+</div>
                    <div class="card-title">Anos de experiência</div>
                </div>
                <div class="flip-card-back">{back_texts[0]}</div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <div class="card-icon">🏢</div>
                    <div class="card-number">{val_emp}+</div>
                    <div class="card-title">Empresas atendidas</div>
                </div>
                <div class="flip-card-back">{back_texts[1]}</div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <div class="card-icon">📊</div>
                    <div class="card-number">{val_proj}+</div>
                    <div class="card-title">Projetos entregues</div>
                </div>
                <div class="flip-card-back">{back_texts[2]}</div>
            </div>
        </div>
        <div class="flip-card">
            <div class="flip-card-inner">
                <div class="flip-card-front">
                    <div class="card-icon">🤝</div>
                    <div class="card-number">{val_rec}%</div>
                    <div class="card-title">Recompra de clientes</div>
                </div>
                <div class="flip-card-back">{back_texts[3]}</div>
            </div>
        </div>
    </div>
    """
    card_placeholders.markdown(html_cards, unsafe_allow_html=True)
    time.sleep(0.02)

st.markdown("---")

# --- EXPERIÊNCIA DE MERCADO ---
st.subheader("🤝 Experiência de Mercado")
st.write("Especialista em Análise de Dados e Business Intelligence, transformando dados brutos em decisões inteligentes.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🔎 Análise Avançada e Automação")
    st.write("Desenvolvimento de scripts Python e modelos em Excel para otimização de tempo.")
    st.markdown("### 📊 Business Intelligence (BI)")
    st.write("Criação de ecossistemas de dados com Power BI, DAX e M.")
with col2:
    st.markdown("### 🗄️ Gerenciamento de Dados")
    st.write("Estruturação de bancos de dados SQL Server e fluxos de ETL eficientes.")
    st.markdown("### 🎯 Minha Abordagem")
    st.write("Foco total na dor do cliente e na geração de valor imediato.")

st.write("")

# --- SEÇÃO DE CLIENTES CENTRALIZADA ---
st.markdown(
    """
    <div class="centered-text">
        <p><strong>Clientes em Destaque:</strong></p>
        <p>Cimed, Unimed Seguros, Ouro Safra, Kraft Heinz, Loggi, Usina Santa Terezinha, Megavig, Lowell e BSS Blindagens.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

st.write("")

col_img1, col_img2, col_img3 = st.columns([1, 8, 1])
with col_img2:
    st.image("assets/clientes_atendidos.jpg", width=None, use_container_width=True)
    
exibir_rodape()
