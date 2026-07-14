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

/* Estilo da barra de pesquisa */
div[data-testid="stTextInput"] input {
    background-color: #111827 !important;
    color: #ffffff !important;
    border: 1px solid #00b4d8 !important;
    border-radius: 12px !important;
    padding: 12px 20px !important;
    font-size: 1rem !important;
}
div[data-testid="stTextInput"] input::placeholder {
    color: #6b7280 !important;
}
div[data-testid="stTextInput"] input:focus {
    box-shadow: 0 0 0 2px rgba(0, 180, 216, 0.3) !important;
    border-color: #00b4d8 !important;
}
.search-result-count {
    text-align: center;
    color: #6b7280;
    font-size: 0.9rem;
    margin-bottom: 20px;
}
.search-result-count span {
    color: #00b4d8;
    font-weight: bold;
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
# BARRA DE PESQUISA
# --------------------------------------------------
st.markdown(
    "<p style='text-align:center; color:#9ca3af; font-size:1rem; margin-bottom:6px;'>🔍 Filtre os projetos pelo nome ou descrição</p>",
    unsafe_allow_html=True
)

col_s1, col_s2, col_s3 = st.columns([1, 2, 1])
with col_s2:
    search_query = st.text_input(
        label="Pesquisar projeto",
        placeholder="Ex: ENEM, ROI, mapas...",
        key="search_python",
        label_visibility="collapsed"
    )

st.write("")

# --------------------------------------------------
# LISTA DE PROJETOS
# --------------------------------------------------
python_projects = [
    {
        "title": "📒Investigador SQL",
        "desc": "'📒Investigador SQL' é um quebra-cabeça de dedução lógica, com visual de quadrinho noir dos anos 50, onde você não escreve SQL você INVESTIGA até chegar nele.",
        "url": "https://sqlmurdoku.streamlit.app/"
    },
    {
        "title": "🎓 O cursinho que o Brasil não pode pagar — eu construí de graça",
        "desc": "Construí um simulador do ENEM gratuito com Python + Streamlit. E quero te contar por que isso importa",
        "url": "https://enem-simulador.streamlit.app/"
    },
    {
        "title": "🎓 Simulador FUVEST",
        "desc": "Construí um simulador da FUVEST gratuito com Python + Streamlit. E quero te contar por que isso importa.",
        "url": "https://simulador-fuvest.streamlit.app/"
    },
    {
        "title": "✈️ Criei um simulado GRATUITO do ITA com questões reais de 2021 a 2025",
        "desc": "Questões reais, gabarito comentado, cronômetro. Sem cadastro. Sem pagar nada, porque o sonho não pode depender do bolso",
        "url": "https://simulador-ita.streamlit.app/"
    },
    {
        "title": "🚀 BI Data Generator PRO",
        "desc": "Construí uma ferramenta que analisa seu desempenho no ENEM por área, explica cada resposta e aponta onde focar. Open source, gratuito, acessível a qualquer estudante com internet.",
        "url": "https://bi-data-generator.streamlit.app"
    },
    {
        "title": "🗺️ CrimeMap BR — Segurança Pública",
        "desc": "Dashboard interativo com dados abertos oficiais do Rio de Janeiro. Explore ocorrências criminais por município, tipo e período.",
        "url": "https://rodrigoaiosa-crimemap.hf.space"
    },
    {
        "title": "🦉 Calculadora ROI de Automação",
        "desc": "Ferramenta estratégica para estimar o Retorno sobre Investimento (ROI) de projetos de automação empresarial.",
        "url": "https://rodrigoaiosa-roi-automacao.hf.space"
    },
    {
        "title": "💼 APP S.O.S. MULHER",
        "desc": "Aplicação voltada à conscientização e análise de dados relacionados à violência contra a mulher no Brasil.",
        "url": "https://rodrigoaiosa-help-mulher.hf.space"
    },
    {
        "title": "💼 Precificador Profissional para MEI",
        "desc": "Calculadora inteligente de precificação para microempreendedores baseada em custos reais e margem desejada.",
        "url": "https://rodrigoaiosa-precificador-profissional-mei.hf.space"
    },
    {
        "title": "📍 Extrator de Dados - Google Maps",
        "desc": "Ferramenta para extração estruturada de dados públicos do Google Maps para geração de leads.",
        "url": "https://rodrigoaiosa-extrair-dados-googlemaps.hf.space"
    },
]

# --------------------------------------------------
# FILTRO DE PESQUISA
# --------------------------------------------------
if search_query:
    filtered_projects = [
        p for p in python_projects
        if search_query.lower() in p["title"].lower() or search_query.lower() in p["desc"].lower()
    ]
    total = len(filtered_projects)
    label = "resultado" if total == 1 else "resultados"
    st.markdown(
        f"<div class='search-result-count'>🔎 <span>{total}</span> {label} para <span>\"{search_query}\"</span></div>",
        unsafe_allow_html=True
    )
else:
    filtered_projects = python_projects

# --------------------------------------------------
# MENSAGEM QUANDO NÃO HÁ RESULTADOS
# --------------------------------------------------
if not filtered_projects:
    st.markdown(
        """
        <div style='text-align:center; padding: 60px 20px; color: #6b7280;'>
            <div style='font-size: 3rem;'>🔍</div>
            <div style='font-size: 1.2rem; margin-top: 10px;'>Nenhum projeto encontrado.</div>
            <div style='font-size: 0.95rem; margin-top: 5px;'>Tente outro termo de pesquisa.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# RENDERIZAÇÃO DOS CARDS
# --------------------------------------------------
for p in filtered_projects:
    st.markdown(f"""
    <div class="project-card">
        <div class="project-title">{p['title']}</div>
        <div class="project-description">{p['desc']}</div>
        <a href="{p['url']}" target="_blank" class="project-button">
            Abrir Aplicação ↗
        </a>
    </div>
    """, unsafe_allow_html=True)

# --------------------------------------------------
# RODAPÉ
# --------------------------------------------------
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

exibir_rodape()
