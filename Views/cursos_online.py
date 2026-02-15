import streamlit as st
import os
import sys
from utils import exibir_rodape, registrar_acesso

registrar_acesso("Cursos Online")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils import exibir_rodape, registrar_acesso
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado na pasta raiz.")

# ---------------- ESTILO GLOBAL PREMIUM ----------------
st.markdown("""
<style>

/* HERO COM GRADIENTE ANIMADO */
.hero {
    background: linear-gradient(270deg, #0f172a, #1e293b, #0f172a);
    background-size: 400% 400%;
    animation: gradientMove 10s ease infinite;
    padding: 70px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

@keyframes gradientMove {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* SECTION TITLE */
.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 20px;
}

/* FEATURE CARDS */
.feature-card {
    background: #111827;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.08);
    opacity: 0;
    transform: translateY(20px);
    animation: fadeUp 0.7s ease forwards;
}

.card1 { animation-delay: 0.1s; }
.card2 { animation-delay: 0.3s; }
.card3 { animation-delay: 0.5s; }

@keyframes fadeUp {
    to { opacity: 1; transform: translateY(0); }
}

.feature-card:hover {
    transform: translateY(-6px);
    border: 1px solid rgba(59,130,246,0.6);
    box-shadow: 0 0 20px rgba(59,130,246,0.35);
}

.feature-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.feature-text {
    color: #cbd5e1;
}

/* COURSE CARDS */
.course-card {
    background: #0b1220;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.05);
    transition: 0.3s;
    animation: fadeUp 0.6s ease;
}

.course-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 25px rgba(59,130,246,0.25);
}

/* BOTÕES COM MICROINTERAÇÃO */
.stLinkButton a {
    background: linear-gradient(90deg,#2563eb,#3b82f6);
    color: white !important;
    padding: 14px 26px !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    transition: 0.2s;
}

.stLinkButton a:hover {
    transform: scale(1.06);
    box-shadow: 0 6px 20px rgba(37,99,235,0.4);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
<h1>Habilidades que transformam profissionais comuns em profissionais indispensáveis</h1>
<p>Power BI • SQL • Excel aplicados ao mundo real dos negócios</p>
</div>
""", unsafe_allow_html=True)

# ---------------- PROPOSTA DE VALOR ----------------
st.markdown('<div class="section-title">Formação orientada ao mercado</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature-card card1">
        <div class="feature-title">🧠 Clareza</div>
        <div class="feature-text">
        Aprenda exatamente o que o mercado exige.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card card2">
        <div class="feature-title">💼 Aplicação real</div>
        <div class="feature-text">
        Conteúdo baseado em problemas reais de empresas.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card card3">
        <div class="feature-title">📈 Valorização profissional</div>
        <div class="feature-text">
        Profissionais orientados por dados são mais valorizados.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ---------------- CURSOS ----------------
st.markdown('<div class="section-title">Treinamentos disponíveis</div>', unsafe_allow_html=True)

# --- POWER BI ---
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    img_pbi = os.path.join("assets", "fundamentos_power_bi.png")
    st.image(img_pbi, width="stretch")

with col2:
    st.markdown('<div class="course-card">', unsafe_allow_html=True)
    st.header("Fundamento Power BI")
    st.write("Transforme dados em dashboards e indicadores estratégicos.")
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/DFeDsQV")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SQL ---
col3, col4 = st.columns([1, 2], gap="large")

with col3:
    img_sql = os.path.join("assets", "SQL_Fundamentos.png")
    st.image(img_sql, width="stretch")

with col4:
    st.markdown('<div class="course-card">', unsafe_allow_html=True)
    st.header("SQL Fundamentos")
    st.write("Extraia informações estratégicas diretamente das bases de dados.")
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/ivdojL8")
    st.markdown('</div>', unsafe_allow_html=True)

# --- EXCEL ---
col5, col6 = st.columns([1, 2], gap="large")

with col5:
    img_excel = os.path.join("assets", "excel_para_negocios.png")
    st.image(img_excel, width="stretch")

with col6:
    st.markdown('<div class="course-card">', unsafe_allow_html=True)
    st.header("Excel Essencial Para Negócios")
    st.write("Automação, análise e produtividade no ambiente corporativo.")
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/EEb9ADQ")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------------- GARANTIA ----------------
st.markdown('<div class="section-title">Compromisso com a qualidade</div>', unsafe_allow_html=True)

st.success(
    "Você pode testar o treinamento com tranquilidade. "
    "Caso não perceba valor real no conteúdo, o reembolso é garantido."
)

exibir_rodape()
