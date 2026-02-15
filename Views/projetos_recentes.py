import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --- CONFIGURAÇÃO ---
st.set_page_config(
    page_title="Portfólio de Projetos",
    page_icon="🚀",
    layout="wide"
)

registrar_acesso("Vitrine de Projetos")

# --- CSS FLIP CARD ---
st.markdown("""
<style>

/* Fundo */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f172a, #0b1120);
    color: white;
}

/* Container do card */
.flip-card {
    background: transparent;
    width: 100%;
    height: 240px;
    perspective: 1000px;
    margin-bottom: 30px;
}

/* Parte interna */
.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.8s;
    transform-style: preserve-3d;
}

/* Efeito ao passar o mouse */
.flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
}

/* Frente e verso */
.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 18px;
    padding: 25px;
    backface-visibility: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.08);
}

/* Verso */
.flip-card-back {
    transform: rotateY(180deg);
}

/* Título */
.project-title {
    font-size: 1.1rem;
    font-weight: 600;
}

/* Resumo */
.project-summary {
    font-size: 0.9rem;
    line-height: 1.5;
    color: #d1d5db;
}

/* Botão */
.view-button {
    background: rgba(0, 180, 216, 0.15);
    color: #00b4d8;
    border: 1px solid rgba(0, 180, 216, 0.4);
    padding: 8px 12px;
    border-radius: 10px;
    text-align: center;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 600;
    transition: 0.3s ease;
}

.view-button:hover {
    background: #00b4d8;
    color: #0f172a;
}

.main-title {
    text-align: center;
    font-size: 2.2rem;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 50px;
}

</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<div class='main-title'>🚀 Portfólio de Projetos</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Passe o mouse para ver detalhes do projeto.</div>", unsafe_allow_html=True)

# --- PROJETOS COM RESUMO (máx 300 caracteres) ---
projects = [
    {
        "title": "🎈 Domando a Web: Automatizando a Coleta de Dados",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7396548688942231552",
        "summary": "Projeto de automação para coleta estruturada de dados na web utilizando Python e técnicas de web scraping. Foco em eficiência, escalabilidade e transformação de dados brutos em informações estratégicas para tomada de decisão."
    },
    {
        "title": "💡 Automatize o Envio de Currículos",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401302855799828480",
        "summary": "Script inteligente que automatiza candidaturas em massa, reduzindo tempo manual e aumentando alcance no mercado de trabalho. Utiliza automação web e lógica estratégica para personalização de envios."
    },
    {
        "title": "🚀 Script que Analisa o Mercado de Trabalho",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7417316742781399040",
        "summary": "Ferramenta que coleta e analisa vagas em tempo real, identificando padrões de mercado, habilidades mais requisitadas e tendências salariais. Auxilia profissionais a se posicionarem estrategicamente."
    },
    {
        "title": "🏛️ Dashboard Automático",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425547898580328449",
        "summary": "Dashboard dinâmico que elimina processos manuais de atualização. Integra dados automaticamente, gera visualizações inteligentes e melhora a gestão com insights claros e acionáveis."
    },
    {
        "title": "📊 Sistemas de Amortização",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425612242248835073/",
        "summary": "Simulador completo de sistemas de amortização com análise comparativa entre modelos. Permite avaliar impacto financeiro e apoiar decisões estratégicas com visualização clara."
    },
    {
        "title": "📍 Prospecção de Alta Performance",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425188593134026752",
        "summary": "Modelo analítico que utiliza dados para identificar leads com maior potencial de conversão. Estratégia orientada por métricas para otimizar vendas e maximizar resultados."
    },
    {
        "title": "🚗 Contagem de Veículos com IA",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422736985196371969",
        "summary": "Sistema de visão computacional capaz de detectar e contar veículos em tempo real. Aplicação prática de IA para monitoramento urbano e análise de fluxo."
    },
    {
        "title": "💡 Pedra, Papel e Tesoura com IA",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422420309632303104",
        "summary": "Aplicação interativa que utiliza visão computacional para reconhecer gestos e jogar em tempo real contra o usuário. Demonstra integração entre IA e experiência interativa."
    },
    {
        "title": "❤️ IA na Vida Real",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7420842332155142144",
        "summary": "Projeto pessoal mostrando como inteligência artificial pode auxiliar decisões cotidianas. Um exemplo real de aplicação prática da tecnologia no contexto familiar."
    }
]

# --- GRID ---
for i in range(0, len(projects), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(projects):
            project = projects[i + j]
            with cols[j]:
                st.markdown(f"""
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div class="project-title">{project['title']}</div>
                            <a href="{project['link']}" target="_blank" class="view-button">
                                Ver Demonstração
                            </a>
                        </div>
                        <div class="flip-card-back">
                            <div class="project-summary">{project['summary']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

exibir_rodape()
