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

# ---------------- ESTILO PREMIUM (SEM ALTERAR FUNDO) ----------------
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

.hero h1 {
    font-size: 42px;
    font-weight: 800;
}

.hero p {
    font-size: 20px;
    color: #e2e8f0;
}

/* CTA BUTTON */
.stLinkButton a {
    background-color: #2563eb !important;
    color: white !important;
    padding: 14px 26px !important;
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
    margin-top: 40px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
<h1>Habilidades que transformam profissionais comuns em profissionais indispensáveis</h1>
<p>Power BI • SQL • Excel aplicados ao mundo real dos negócios</p>
</div>
""", unsafe_allow_html=True)

# ---------------- PROPOSTA DE VALOR ----------------
st.markdown('<div class="section-title">Formação orientada ao mercado</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

c1.markdown(
    "### 🧠 Clareza\n"
    "Aprenda exatamente o que o mercado exige, eliminando conteúdos irrelevantes."
)

c2.markdown(
    "### 💼 Aplicação real\n"
    "Treinamentos construídos com base em problemas reais do ambiente corporativo."
)

c3.markdown(
    "### 📈 Valorização profissional\n"
    "Dominar dados aumenta sua relevância dentro de qualquer empresa."
)

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

        Não é apenas sobre aprender a ferramenta — é sobre desenvolver pensamento analítico.
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

        Este treinamento desenvolve a capacidade de consultar, analisar e extrair
        informações estratégicas de bases de dados reais.

        Profissionais que dominam SQL conquistam autonomia analítica
        e se tornam muito mais valiosos para o negócio.
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
        Excel continua sendo uma das ferramentas mais utilizadas no ambiente corporativo,
        mas poucos profissionais sabem utilizá-lo de forma estratégica.

        Neste treinamento, você aprende Excel aplicado ao mundo dos negócios,
        automação de tarefas e construção de análises confiáveis.

        A diferença entre usar Excel e dominar Excel
        é o que separa operadores de profissionais estratégicos.
        """
    )
    st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/EEb9ADQ")

st.markdown("---")

# ---------------- GARANTIA ----------------
st.markdown('<div class="section-title">Compromisso com a qualidade</div>', unsafe_allow_html=True)

st.success(
    """
    Você pode testar o treinamento com tranquilidade.
    Caso não perceba valor real no conteúdo, o reembolso é garantido dentro do prazo da plataforma.
    """
)

exibir_rodape()
