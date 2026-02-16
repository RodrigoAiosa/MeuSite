import streamlit as st
import os

# =========================================================
# 🔹 BASE PATH
# =========================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# =========================================================
# 🔹 IMPORT UTILS (IMPORT DIRETO DA RAIZ)
# =========================================================
from utils import exibir_rodape, registrar_acesso, registrar_clique_botao

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
# 🔹 ESTILO PREMIUM
# =========================================================
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    padding: 60px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}
.section-title {
    font-size: 32px;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 20px;
}
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
.card1 { animation-delay: 0.1s; }
.card2 { animation-delay: 0.3s; }
.card3 { animation-delay: 0.5s; }

@keyframes fadeUp {
    to { opacity: 1; transform: translateY(0); }
}

.feature-card:hover {
    transform: translateY(-6px);
    border: 1px solid rgba(59,130,246,0.6);
    box-shadow: 0 0 18px rgba(59,130,246,0.35);
}

.feature-title {
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
}

.feature-text { 
    color: #cbd5e1; 
}

.stLinkButton a {
    background-color: #2563eb !important;
    color: white !important;
    padding: 14px 26px !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# 🔹 HERO
# =========================================================
st.markdown("""
<div class="hero">
<h1>Habilidades que transformam profissionais comuns em profissionais indispensáveis</h1>
<p>Power BI • SQL • Excel aplicados ao mundo real dos negócios</p>
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
    st.write("Transforme dados brutos em dashboards profissionais e indicadores estratégicos.")

    if st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/DFeDsQV"):
        registrar_clique_botao("Curso Power BI")

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
    st.write("Desenvolva autonomia analítica e capacidade de extrair informações estratégicas.")

    if st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/ivdojL8"):
        registrar_clique_botao("Curso SQL")

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
    st.write("Excel aplicado ao mundo corporativo, automação e análises estratégicas.")

    if st.link_button("Saiba mais sobre o curso", "https://pay.kiwify.com.br/EEb9ADQ"):
        registrar_clique_botao("Curso Excel")

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

st.markdown("---")

# =========================================================
# 🔹 GARANTIA
# =========================================================
st.markdown('<div class="section-title">Compromisso com a qualidade</div>', unsafe_allow_html=True)

st.success(
    "Você pode testar o treinamento com tranquilidade. "
    "Caso não perceba valor real no conteúdo, o reembolso é garantido."
)

# =========================================================
# 🔹 RODAPÉ
# =========================================================
exibir_rodape()
