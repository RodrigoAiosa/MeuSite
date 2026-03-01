import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --------------------------------------------------
# REGISTRO DE ACESSO
# --------------------------------------------------
registrar_acesso("Projetos Python")

# --------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# --------------------------------------------------
st.set_page_config(
    page_title="Projetos em Python | Rodrigo Aiosa",
    page_icon="🐍",
    layout="wide"
)

# --------------------------------------------------
# ESTILO PREMIUM (PORTFÓLIO SaaS)
# --------------------------------------------------
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    font-weight: 600;
    letter-spacing: -0.5px;
}

.subtitle {
    color: #9CA3AF;
    font-size: 1.1rem;
    margin-bottom: 30px;
}

.project-card {
    background-color: #111827;
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 25px;
    border: 1px solid rgba(255,255,255,0.05);
    transition: all 0.3s ease;
}

.project-card:hover {
    transform: translateY(-3px);
    border: 1px solid #00b4d8;
    box-shadow: 0 10px 25px rgba(0, 180, 216, 0.15);
}

.project-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 8px;
}

.project-description {
    color: #D1D5DB;
    font-size: 0.95rem;
    margin-bottom: 15px;
    line-height: 1.5;
}

.project-button {
    display: inline-block;
    background-color: #00b4d8;
    color: #0E1117 !important;
    font-weight: 600;
    padding: 10px 18px;
    border-radius: 8px;
    text-decoration: none;
    transition: 0.3s;
}

.project-button:hover {
    background-color: #0096c7;
}

.section-divider {
    margin-top: 40px;
    margin-bottom: 40px;
    border-top: 1px solid rgba(255,255,255,0.05);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🐍 Projetos em Python")

st.markdown(
    '<div class="subtitle">Aplicações web completas desenvolvidas para automação, análise financeira e Business Intelligence.</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# --------------------------------------------------
# FUNÇÃO PARA RENDERIZAR PROJETOS (SEM IFRAME)
# --------------------------------------------------
def render_python_app(title, description, url):
    st.markdown(f"""
    <div class="project-card">
        <div class="project-title">{title}</div>
        <div class="project-description">{description}</div>
        <a href="{url}" target="_blank" class="project-button">
            Abrir Aplicação ↗
        </a>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# LISTA DE PROJETOS
# --------------------------------------------------


render_python_app(
    "🎓 O cursinho que o Brasil não pode pagar — eu construí de graça",
    "Construí um simulador do ENEM gratuito com Python + Streamlit. E quero te contar por que isso importa",
    "https://enem-simulador.streamlit.app/"
)

render_python_app(
    "✈️ Criei um simulado GRATUITO do ITA com questões reais de 2021 a 2025",
    "Questões reais, gabarito comentado, cronômetro. Sem cadastro. Sem pagar nada, porque o sonho não pode depender do bolso",
    "https://simulador-ita.streamlit.app/"
)

render_python_app(
    "🚀 BI Data Generator PRO",
    "Construí uma ferramenta que analisa seu desempenho no ENEM por área, explica cada resposta e aponta onde focar. Open source, gratuito, acessível a qualquer estudante com internet.",
     "https://bi-data-generator.streamlit.app"
)

render_python_app(
    "🗺️ CrimeMap BR — Segurança Pública",
    "Dashboard interativo com dados abertos oficiais do Rio de Janeiro. Explore ocorrências criminais por município, tipo e período.",
    "https://rodrigoaiosa-crimemap.hf.space"
)

render_python_app(
    "🦉 Calculadora ROI de Automação",
    "Ferramenta estratégica para estimar o Retorno sobre Investimento (ROI) de projetos de automação empresarial.",
    "https://rodrigoaiosa-roi-automacao.hf.space"
)

render_python_app(
    "💼 APP S.O.S. MULHER",
    "Aplicação voltada à conscientização e análise de dados relacionados à violência contra a mulher no Brasil.",
    "https://rodrigoaiosa-help-mulher.hf.space"
)

render_python_app(
    "💼 Precificador Profissional para MEI",
    "Calculadora inteligente de precificação para microempreendedores baseada em custos reais e margem desejada.",
    "https://rodrigoaiosa-precificador-profissional-mei.hf.space"
)

render_python_app(
    "📍 Extrator de Dados - Google Maps",
    "Ferramenta para extração estruturada de dados públicos do Google Maps para geração de leads.",
    "https://rodrigoaiosa-extrair-dados-googlemaps.hf.space"
)

# --------------------------------------------------
# RODAPÉ
# --------------------------------------------------
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

exibir_rodape()






