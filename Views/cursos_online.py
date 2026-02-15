import streamlit as st
import os
import sys
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Cursos Online")

# 1. RESOLVENDO O CAMINHO DO MÓDULO UTILS
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from utils import exibir_rodape, registrar_acesso
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado na pasta raiz.")

# ---------------- ESTILO PREMIUM ----------------
st.markdown("""
<style>

/* HERO */
.hero {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 60px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
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
    min-height: 140px;

    opacity: 0;
    transform: translateY(20px);
    animation: fadeUp 0.7s ease forwards;
}

/* Delay para efeito em sequência */
.card1 { animation-delay: 0.1s; }
.card2 { animation-delay: 0.3s; }
.card3 { animation-delay: 0.5s; }

@keyframes fadeUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Glow hover */
.feature-card:hover {
    transform: translateY(-6px);
    border: 1px solid rgba(59,130,246,0.6);
    box-shadow: 0 0 18px rgba(59,130,246,0.35);
}

/* TEXT */
.feature-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.feature-text {
    color: #cbd5e1;
}

/* BOTÕES */
.stLinkButton a {
    background-color: #2563eb !important;
    color: white !important;
    padding: 14px 26px !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
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
        Aprenda exatamente o que o mercado exige, eliminando conteúdos irrelevantes.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card card2">
        <div class="feature-title">💼 Aplicação real</div>
        <div class="feature-text">
        Treinamentos construídos com base em problemas reais do ambiente corporativo.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card card3">
        <div class="feature-title">📈 Valorização profissional</div>
        <div class="feature-text">
        Dominar dados aumenta sua relevância dentro de qualquer empresa.
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
    st.header("Fundamento Power BI")
    st.write(
        """
        O Power BI deixou de ser um diferencial e se tornou uma habilidade essencial
        para profissionais que participam de decisões estratégicas.

        Neste treinamento, você aprende a transformar dados brutos em dashboards
        profissionais e indicadores claros para tomada de decisão.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/DFeDsQV")

st.markdown("")

# --- SQL ---
col3, col4 = st.columns([1, 2], gap="large")

with col3:
    img_sql = os.path.join("assets", "SQL_Fundamentos.png")
    st.image(img_sql, width="stretch")

with col4:
    st.header("SQL Fundamentos")
    st.write(
        """
        SQL é a linguagem que conecta profissionais diretamente aos dados das empresas.
        Desenvolva autonomia analítica e capacidade de extrair informações estratégicas.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/ivdojL8")

st.markdown("")

# --- EXCEL ---
col5, col6 = st.columns([1, 2], gap="large")

with col5:
    img_excel = os.path.join("assets", "excel_para_negocios.png")
    st.image(img_excel, width="stretch")

with col6:
    st.header("Excel Essencial Para Negócios")
    st.write(
        """
        Excel aplicado ao mundo corporativo, automação de tarefas e análises confiáveis
        para profissionais que querem se destacar.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/EEb9ADQ")

st.markdown("---")

# ---------------- GARANTIA ----------------
st.markdown('<div class="section-title">Compromisso com a qualidade</div>', unsafe_allow_html=True)

st.success(
    "Você pode testar o treinamento com tranquilidade. "
    "Caso não perceba valor real no conteúdo, o reembolso é garantido."
)

exibir_rodape()
