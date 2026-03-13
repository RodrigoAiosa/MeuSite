import streamlit as st
import os
import sys

# =========================================================
# 🔹 BASE PATH (considerando que este arquivo está em Views/)
# =========================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# =========================================================
# 🔹 IMPORT UTILS
# =========================================================
sys.path.append(BASE_DIR)

try:
    from utils import exibir_rodape, registrar_acesso
except ImportError:
    st.error("Erro: O arquivo 'utils.py' não foi encontrado na pasta raiz.")

# =========================================================
# 🔹 REGISTRO DE ACESSO
# =========================================================
registrar_acesso("Cursos Online")

# =========================================================
# 🔹 FUNÇÃO SEGURA PARA EXIBIR IMAGEM
# =========================================================
def carregar_imagem(nome_arquivo):
    caminho = os.path.join(ASSETS_DIR, nome_arquivo)
    if os.path.exists(caminho):
        st.image(caminho, use_container_width=True)
    else:
        st.warning(f"Imagem não encontrada: {nome_arquivo}")

# =========================================================
# 🔹 ESTILO LANDING PAGE
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

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

/* ── HERO ── */
.hero {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.3) 100%);
    border: 1px solid rgba(0,180,216,0.15);
    border-radius: 24px;
    padding: 80px 60px;
    text-align: center;
    margin-bottom: 60px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(0,180,216,0.1);
}

.hero::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.5), transparent);
}

.hero h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2rem, 4vw, 3.2rem) !important;
    font-weight: 800 !important;
    line-height: 1.15 !important;
    letter-spacing: -1.5px !important;
    background: linear-gradient(135deg, #f0f4ff 40%, #00b4d8 100%);
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    margin-bottom: 20px !important;
}

.hero p {
    font-size: 1rem !important;
    color: #4a5568 !important;
    font-weight: 300 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    margin: 0 !important;
}

/* ── SECTION TITLE ── */
.section-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.5rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    color: #f0f4ff;
    margin-top: 50px;
    margin-bottom: 28px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(0,180,216,0.15);
    position: relative;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: -1px; left: 0;
    width: 48px; height: 2px;
    background: #00b4d8;
}

/* ── FEATURE CARDS ── */
.feature-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.25) 100%);
    padding: 28px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.05);
    min-height: 140px;
    opacity: 0;
    transform: translateY(20px);
    animation: fadeUp 0.7s ease forwards;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.4), transparent);
    opacity: 0;
    transition: opacity 0.35s ease;
}

.card1 { animation-delay: 0.1s; }
.card2 { animation-delay: 0.3s; }
.card3 { animation-delay: 0.5s; }

@keyframes fadeUp {
    to { opacity: 1; transform: translateY(0); }
}

.feature-card:hover {
    transform: translateY(-5px);
    border-color: rgba(0,180,216,0.25);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 0 1px rgba(0,180,216,0.1);
}

.feature-card:hover::before { opacity: 1; }

.feature-title {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.05rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 10px;
    letter-spacing: -0.2px;
}

.feature-text {
    color: #4a5568;
    font-size: 0.9rem;
    line-height: 1.65;
    font-weight: 300;
}

/* ── CURSO SECTION ── */
.curso-wrapper {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 36px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.curso-wrapper::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.35), transparent);
    opacity: 0;
    transition: opacity 0.35s ease;
}

.curso-wrapper:hover {
    border-color: rgba(0,180,216,0.18);
    box-shadow: 0 20px 40px rgba(0,0,0,0.35);
}

.curso-wrapper:hover::before { opacity: 1; }

/* ── STREAMLIT OVERRIDES ── */
.stExpander {
    background: linear-gradient(145deg, rgba(255,255,255,0.02) 0%, rgba(0,0,0,0.15) 100%) !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    border-radius: 12px !important;
}

.stExpander [data-testid="stExpanderToggleButton"] {
    color: #00b4d8 !important;
    font-weight: 600;
}

.stLinkButton a {
    background: rgba(0,180,216,0.12) !important;
    color: #00b4d8 !important;
    padding: 12px 28px !important;
    border-radius: 12px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    border: 1px solid rgba(0,180,216,0.3) !important;
    transition: all 0.3s ease !important;
    text-decoration: none !important;
}

.stLinkButton a:hover {
    background: rgba(0,180,216,0.22) !important;
    border-color: rgba(0,180,216,0.55) !important;
    box-shadow: 0 4px 20px rgba(0,180,216,0.2) !important;
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

# =========================================================
# 🔹 HERO
# =========================================================
st.markdown("""
<div class="hero">
    <h1>Habilidades que transformam profissionais comuns em profissionais indispensáveis</h1>
    <p>Power BI &nbsp;•&nbsp; SQL &nbsp;•&nbsp; Excel aplicados ao mundo real dos negócios</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 🔹 PROPOSTA DE VALOR
# =========================================================
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
        Conteúdo baseado em problemas reais do ambiente corporativo.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card card3">
        <div class="feature-title">📈 Valorização profissional</div>
        <div class="feature-text">
        Dominar dados aumenta sua relevância na empresa.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# 🔹 CURSOS
# =========================================================
st.markdown('<div class="section-title">Treinamentos disponíveis</div>', unsafe_allow_html=True)

# ================= POWER BI =================
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    carregar_imagem("fundamentos_power_bi.png")

with col2:
    st.header("Fundamento Power BI")
    st.write("""
    Transforme dados brutos em dashboards profissionais e indicadores estratégicos.
    """)
    st.link_button("Comprar", "https://pay.kiwify.com.br/DFeDsQV")

    with st.expander("📚 Ver conteúdo programático"):
        st.markdown("""
        1. Introdução ao Power BI  
        2. Power Query (Tratamento de Dados)  
        3. Modelagem de Dados (Modelo Estrela)  
        4. Relacionamentos entre Tabelas  
        5. Fundamentos de DAX  
        6. Medidas e KPIs  
        7. Dashboards Interativos  
        8. Storytelling com Dados  
        9. Publicação no Power BI Service  
        10. Projeto Final Aplicado  
        """)

st.markdown("")

# ================= SQL =================
col3, col4 = st.columns([1, 2], gap="large")

with col3:
    carregar_imagem("SQL_Fundamentos.jpg")

with col4:
    st.header("SQL Fundamentos")
    st.write("""
    Desenvolva autonomia analítica e capacidade de extrair informações estratégicas.
    """)
    st.link_button("Comprar", "https://pay.kiwify.com.br/ivdojL8")

    with st.expander("📚 Ver conteúdo programático"):
        st.markdown("""
        1. Conceitos de Banco de Dados  
        2. SELECT, WHERE e ORDER BY  
        3. Funções Agregadas  
        4. GROUP BY e HAVING  
        5. INNER JOIN e LEFT JOIN  
        6. Subqueries  
        7. Views  
        8. Manipulação de Datas  
        9. Otimização de Consultas  
        10. Projeto Final Corporativo  
        """)

st.markdown("")

# ================= EXCEL =================
col5, col6 = st.columns([1, 2], gap="large")

with col5:
    carregar_imagem("excel_para_negocios.png")

with col6:
    st.header("Excel Essencial Para Negócios")
    st.write("""
    Excel aplicado ao mundo corporativo, automação e análises estratégicas.
    """)
    st.link_button("Comprar", "https://pay.kiwify.com.br/EEb9ADQ")

    with st.expander("📚 Ver conteúdo programático"):
        st.markdown("""
        1. Fundamentos do Excel Corporativo  
        2. Fórmulas Essenciais  
        3. PROCV e PROCX  
        4. Tabelas Dinâmicas  
        5. Dashboards no Excel  
        6. Formatação Condicional  
        7. Indicadores Financeiros  
        8. Power Query no Excel  
        9. Introdução a Macros  
        10. Projeto Final Aplicado  
        """)

st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

exibir_rodape()
