import streamlit as st
import time
import base64
from utils import registrar_acesso, exibir_rodape

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(layout="wide", page_title="Portfolio | Rodrigo Aiosa")

# 2. REGISTRO DE ACESSO
registrar_acesso("Sobre Mim")

# 3. FUNÇÃO PARA CARREGAR IMAGEM EM BASE64
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_b64 = img_to_base64("assets/EU.jpg")

# --- ESTILO LANDING PAGE ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&family=Bebas+Neue&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(0,180,216,0.10) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(0,100,180,0.06) 0%, transparent 50%);
}

[data-testid="stHeader"] { background: transparent !important; }

/* Fonte apenas no conteúdo principal */
.main h1, .main h2, .main h3, .main h4,
.main p, .main a, .main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}

/* Preserva ícones Material do Streamlit */
.material-symbols-rounded,
.material-icons,
[data-testid*="Collapse"] span,
[data-testid*="collapse"] span {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
}

[data-testid="stMarkdownContainer"] { width: 100% !important; }
.block-container {
    max-width: 100% !important;
    padding-left: 4rem !important;
    padding-right: 4rem !important;
}

/* ── PROFILE PHOTO ── */
.profile-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: -10px;
    margin-bottom: 10px;
    position: relative;
}

.profile-pic-border {
    position: relative;
    width: 210px;
    height: 210px;
    background: #060912;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    overflow: hidden;
    box-shadow: 0 4px 30px rgba(0,180,216,0.2);
}

.profile-pic-border::before {
    content: '';
    position: absolute;
    width: 150%;
    height: 150%;
    background: conic-gradient(transparent, #00b4d8, #48cae4, transparent 40%);
    animation: rotate-border 4s linear infinite;
}

.profile-pic-border img {
    width: 200px;
    height: 200px;
    border-radius: 50%;
    object-fit: cover;
    z-index: 1;
    background-color: #060912;
    border: 3px solid #060912;
}

@keyframes rotate-border {
    0%   { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.main-title {
    font-family: 'Syne', sans-serif !important;
    text-align: center;
    font-size: clamp(2rem, 4vw, 3rem) !important;
    font-weight: 800 !important;
    letter-spacing: -1.5px !important;
    color: #f0f4ff !important;
    margin-top: 12px !important;
    margin-bottom: 8px !important;
}

/* ── CARDS CONTAINER (FLIP) ── */
.cards-container {
    display: flex;
    justify-content: space-between;
    gap: 16px;
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

.flip-card:hover {
    transform: scale(1.08);
    z-index: 10;
}

.cards-container:hover .flip-card:not(:hover) {
    filter: blur(6px);
    transform: scale(0.92);
    opacity: 0.5;
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
}

.flip-card-front {
    background: linear-gradient(145deg, rgba(255,255,255,0.04) 0%, rgba(0,0,0,0.25) 100%);
    border: 1px solid rgba(255,255,255,0.05);
    color: #f0f4ff;
    position: relative;
    overflow: hidden;
}

.flip-card-front::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.4), transparent);
}

.flip-card-back {
    background: linear-gradient(135deg, rgba(0,180,216,0.15) 0%, rgba(0,100,180,0.2) 100%);
    border: 1px solid rgba(0,180,216,0.35);
    color: #e2e8f0;
    transform: rotateY(180deg);
    font-size: 0.88rem;
    font-weight: 400;
    line-height: 1.65;
    backdrop-filter: blur(8px);
}

.card-icon  { font-size: 26px; margin-bottom: 6px; }
.card-number {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.8rem;
    font-weight: 800;
    color: #00b4d8;
    line-height: 1;
}
.card-title {
    font-size: 0.78rem;
    color: #4a5568;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 5px;
}

/* ── CENTERED TEXT ── */
.centered-text {
    text-align: center;
    max-width: 900px;
    margin: 0 auto;
    font-size: 1rem;
    color: #4a5568;
    line-height: 1.8;
    font-weight: 300;
}

/* ── EXP CARDS ── */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to   { opacity: 1; transform: translateY(0); }
}

.exp-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.25) 100%);
    padding: 26px 28px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.05);
    border-left: 3px solid #00b4d8;
    height: 160px;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: default;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.8s ease-out forwards;
}

.exp-card:hover {
    transform: translateY(-8px);
    border-left: 4px solid #00b4d8;
    border-color: rgba(0,180,216,0.25);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 0 1px rgba(0,180,216,0.1);
}

.exp-card h3 { transition: color 0.3s ease; }
.exp-card:hover h3 { color: #00b4d8 !important; }

.delay-1 { animation-delay: 0.2s; }
.delay-2 { animation-delay: 0.4s; }
.delay-3 { animation-delay: 0.6s; }
.delay-4 { animation-delay: 0.8s; }

/* ── FLOATING CTA BUTTON ── */
.promo-float-btn {
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 9997;
    background: linear-gradient(135deg, #d4910e, #f5a623, #d4910e);
    color: #1a0800 !important;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 14px;
    letter-spacing: 2px;
    padding: 14px 22px;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    box-shadow: 0 4px 0 #7a4e00, 0 6px 24px rgba(200,134,10,0.5);
    text-transform: uppercase;
    text-decoration: none !important;
    animation: floatPulse 2s ease-in-out infinite;
    display: flex;
    align-items: center;
    gap: 8px;
}

.promo-float-btn:hover {
    background: linear-gradient(135deg, #e5a020, #ffc040, #e5a020);
    transform: translateY(-3px) scale(1.04);
    box-shadow: 0 6px 0 #7a4e00, 0 10px 30px rgba(200,134,10,0.7);
}

@keyframes floatPulse {
    0%, 100% { box-shadow: 0 4px 0 #7a4e00, 0 6px 24px rgba(200,134,10,0.5); }
    50%       { box-shadow: 0 4px 0 #7a4e00, 0 6px 36px rgba(200,134,10,0.85); }
}

hr {
    border: none !important;
    border-top: 1px solid rgba(255,255,255,0.05) !important;
    margin: 40px 0 !important;
}

.footer-spacer { height: 60px; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #060912; }
::-webkit-scrollbar-thumb { background: rgba(0,180,216,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0,180,216,0.4); }

</style>
""", unsafe_allow_html=True)

# --- BOTÃO FLUTUANTE ---
st.markdown(
    """
    <!-- BOTÃO FLUTUANTE -->
    <a href="https://rodrigoaiosa.github.io/promocao_curso_online/" target="_blank" class="promo-float-btn">
        🔥 Promoção Treinamento Online
    </a>
    """,
    unsafe_allow_html=True
)

# --- CABEÇALHO ---
st.markdown(
    f"""
    <div class="profile-container">
        <div class="profile-pic-border">
            <img src="data:image/jpeg;base64,{img_b64}">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="main-title">Rodrigo Aiosa</h1>', unsafe_allow_html=True)
st.markdown(
    '<div style="text-align:center; font-family:\'Syne\',sans-serif; font-size:0.8rem; color:#00b4d8; font-weight:700; letter-spacing:3px; text-transform:uppercase; margin-bottom:8px;">Python &nbsp;|&nbsp; Excel &nbsp;|&nbsp; Power BI &nbsp;|&nbsp; ETL &nbsp;|&nbsp; SQL SERVER &nbsp;|&nbsp; Linguagem M &nbsp;|&nbsp; DAX</div>',
    unsafe_allow_html=True
)

st.write("")

# --- CARDS COM CONTADOR E EFEITOS DE HOVER ---
st.markdown(
    '<p style="font-family:\'Syne\',sans-serif; font-size:1.1rem; font-weight:800; color:#e2e8f0; letter-spacing:-0.3px;">⭐ Experiência e Resultados</p>',
    unsafe_allow_html=True
)

card_placeholders = st.empty()

back_texts = [
    "Expertise em automação de processos e análise preditiva.",
    "Soluções personalizadas para grandes players do mercado.",
    "Dashboards estratégicos focados em KPIs de alto nível.",
    "Parceria contínua baseada em confiança e resultados reais."
]

for i in range(0, 101, 5):
    val_exp  = int(20  * i / 100)
    val_emp  = int(450 * i / 100)
    val_proj = int(500 * i / 100)
    val_rec  = int(87  * i / 100)

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
    st.markdown(
        """
        <div class="exp-card delay-1">
            <h3 style="color:#e2e8f0; margin-bottom:8px; font-family:'Syne',sans-serif; font-size:1.05rem; font-weight:700; letter-spacing:-0.3px;">🔎 Análise Avançada e Automação</h3>
            <p style="color:#4a5568; font-size:0.9rem; font-weight:300; line-height:1.65;">Desenvolvimento de scripts Python e modelos em Excel para otimização de tempo e processos.</p>
        </div>
        <br>
        <div class="exp-card delay-2">
            <h3 style="color:#e2e8f0; margin-bottom:8px; font-family:'Syne',sans-serif; font-size:1.05rem; font-weight:700; letter-spacing:-0.3px;">📊 Business Intelligence (BI)</h3>
            <p style="color:#4a5568; font-size:0.9rem; font-weight:300; line-height:1.65;">Criação de ecossistemas de dados robustos utilizando Power BI, Linguagem M e DAX.</p>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="exp-card delay-3">
            <h3 style="color:#e2e8f0; margin-bottom:8px; font-family:'Syne',sans-serif; font-size:1.05rem; font-weight:700; letter-spacing:-0.3px;">🗄️ Gerenciamento de Dados</h3>
            <p style="color:#4a5568; font-size:0.9rem; font-weight:300; line-height:1.65;">Estruturação de bancos de dados SQL Server e fluxos de ETL eficientes para alta performance.</p>
        </div>
        <br>
        <div class="exp-card delay-4">
            <h3 style="color:#e2e8f0; margin-bottom:8px; font-family:'Syne',sans-serif; font-size:1.05rem; font-weight:700; letter-spacing:-0.3px;">🎯 Minha Abordagem</h3>
            <p style="color:#4a5568; font-size:0.9rem; font-weight:300; line-height:1.65;">Foco total na solução da dor do cliente, visando agilidade e a geração de valor imediato.</p>
        </div>
        """, unsafe_allow_html=True
    )

st.write("")

# --- SEÇÃO DE CLIENTES ---
st.markdown(
    """
    <div class="centered-text">
        <p style="color:#e2e8f0; font-weight:600; margin-bottom:8px;">Clientes em Destaque:</p>
        <p>Cimed, Unimed Seguros, Ouro Safra, Kraft Heinz, Loggi, Usina Santa Terezinha, Megavig, Lowell e BSS Blindagens.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

col_img1, col_img2, col_img3 = st.columns([1, 8, 1])
with col_img2:
    st.image("assets/clientes_atendidos.jpg", width=None, use_container_width=True)

st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

exibir_rodape()
