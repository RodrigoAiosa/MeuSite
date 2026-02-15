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

registrar_acesso("Cursos Online")

# ---------------- ESTILO PREMIUM ----------------
st.markdown("""
<style>

.stApp {
    background-color: #f8fafc;
}

/* HERO */
.hero {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 60px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 42px;
    font-weight: 800;
}

.hero p {
    font-size: 20px;
    color: #e2e8f0;
}

/* CARD */
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.08);
}

/* CTA BUTTON */
.stLinkButton a {
    background-color: #2563eb !important;
    color: white !important;
    padding: 14px 24px !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
}

.stLinkButton a:hover {
    background-color: #1d4ed8 !important;
    transform: scale(1.03);
}

/* SECTION TITLE */
.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-top: 30px;
}

.testimonial {
    background: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
<h1>Domine as habilidades mais valorizadas do mercado</h1>
<p>Power BI • SQL • Excel aplicados ao mundo real</p>
</div>
""", unsafe_allow_html=True)

st.link_button("Começar agora", "https://pay.kiwify.com.br/DFeDsQV")

st.markdown("---")

# ---------------- PROPOSTA DE VALOR ----------------
st.markdown('<div class="section-title">Por que aprender comigo?</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

c1.markdown("### 🎯 Direto ao ponto\nConteúdo prático e aplicável no trabalho.")
c2.markdown("### 📊 Foco no mercado\nHabilidades que empresas realmente usam.")
c3.markdown("### 🚀 Evolução rápida\nAprenda mais rápido do que em cursos tradicionais.")

st.markdown("---")

# ---------------- CURSOS ----------------
st.markdown('<div class="section-title">Cursos disponíveis</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    img_pbi = os.path.join("assets", "fundamentos_power_bi.png")
    st.image(img_pbi, width="stretch")

with col2:
    st.header("Fundamento Power BI")
    st.write(
        "Aprenda Power BI do zero e construa dashboards profissionais."
    )
    st.link_button("Ver curso", "https://pay.kiwify.com.br/DFeDsQV")

st.markdown("")

col3, col4 = st.columns([1, 2], gap="large")

with col3:
    img_sql = os.path.join("assets", "SQL_Fundamentos.png")
    st.image(img_sql, width="stretch")

with col4:
    st.header("SQL Fundamentos")
    st.write("Domine consultas SQL e análise de dados.")
    st.link_button("Ver curso", "https://pay.kiwify.com.br/ivdojL8")

st.markdown("")

col5, col6 = st.columns([1, 2], gap="large")

with col5:
    img_excel = os.path.join("assets", "excel_para_negocios.png")
    st.image(img_excel, width="stretch")

with col6:
    st.header("Excel Essencial Para Negócios")
    st.write("Excel aplicado ao mundo corporativo.")
    st.link_button("Ver curso", "https://pay.kiwify.com.br/EEb9ADQ")

st.markdown("---")

# ---------------- PROVA SOCIAL ----------------
st.markdown('<div class="section-title">O que alunos dizem</div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns(3)

t1.markdown("""
<div class="testimonial">
"Didática excelente e muito prática."
<br><br>
<b>Aluno</b>
</div>
""", unsafe_allow_html=True)

t2.markdown("""
<div class="testimonial">
"Consegui aplicar no trabalho na primeira semana."
<br><br>
<b>Aluno</b>
</div>
""", unsafe_allow_html=True)

t3.markdown("""
<div class="testimonial">
"Um dos cursos mais objetivos que já fiz."
<br><br>
<b>Aluno</b>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- GARANTIA ----------------
st.markdown('<div class="section-title">Garantia</div>', unsafe_allow_html=True)

st.info("7 dias de garantia incondicional. Se não gostar, devolvemos seu dinheiro.")

st.markdown("---")

# ---------------- CTA FINAL ----------------
st.markdown("""
<div class="hero">
<h1>Comece hoje sua evolução profissional</h1>
<p>Invista em você e destaque-se no mercado.</p>
</div>
""", unsafe_allow_html=True)

st.link_button("Quero começar agora", "https://pay.kiwify.com.br/DFeDsQV")

exibir_rodape()
