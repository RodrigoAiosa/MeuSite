import streamlit as st
from utils import exibir_rodape, registrar_acesso  # Importação atualizada

# --- REGISTRO DE ACESSO ---
# Registra a entrada do usuário na página de Projetos Python
registrar_acesso("Projetos Python")

# --- ESTILO CSS ---
st.markdown(
    """
    <style>
    .project-button {
        display: inline-block;
        background-color: #262730;
        color: #00b4d8 !important;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 12px 20px;
        margin-bottom: 5px;
        border-radius: 10px;
        text-decoration: none;
        transition: transform 0.3s, box-shadow 0.3s;
        border: 1px solid rgba(0, 180, 216, 0.2);
        width: 100%;
        max-width: 800px;
        cursor: pointer;
        text-align: left;
    }
    .project-button:hover {
        transform: scale(1.01);
        box-shadow: 0 8px 16px rgba(0, 180, 216, 0.3);
        border-color: #00b4d8;
    }
    .project-description {
        color: #ffffff;
        font-size: 0.95rem;
        margin-bottom: 15px;
        padding-left: 5px;
        max-width: 800px;
        line-height: 1.4;
    }
    .iframe-container {
        border: 2px solid #31333F;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 60px;
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🐍 Projetos em Python")
st.write("Aplicações web completas desenvolvidas para automação de processos e análise financeira.")

# --- FUNÇÃO PARA RENDERIZAR APPS COM DESCRIÇÃO ---
def render_python_app(title, description, url):
    # Botão
    st.markdown(f'<a href="{url}" target="_blank" class="project-button">{title} ↗️</a>', unsafe_allow_html=True)
    # Descrição
    st.markdown(f'<div class="project-description">{description}</div>', unsafe_allow_html=True)
    # App incorporado
    st.markdown(
        f"""
        <div class="iframe-container">
            <iframe 
                src="{url}?embed=true" 
                width="100%" 
                height="700" 
                frameborder="0" 
                allowfullscreen>
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- LISTA DE PROJETOS ---

# Projeto
render_python_app(
    "🦉 Calculadora ROI de Automação",
    "Calculadora que estima o Retorno sobre Investimento (ROI) de projetos de automação, comparando custos, economia de tempo e ganhos financeiros para apoiar decisões estratégicas.",
    "https://rodrigoaiosa-rio-automacao.hf.space"
)

# Projeto
render_python_app(
    "💼 APP S.O.S. MULHER",
    "Em 2025, dados publicados pelo Ministério da Justiça e Segurança Pública apontam que foram registrados 1.518 feminicídios, a maior marca já registrada até o momento.",
    "https://sosmulher.streamlit.app/"
)

# Projeto
render_python_app(
    "💼 Precificador Profissional para MEI",
    "Calculadora profissional de precificação para MEI que ajuda a definir o preço de venda com base em custos, impostos, comissões e margem de lucro. Inclui markup automático, ponto de equilíbrio, gráficos financeiros e exportação de relatórios em Excel.",
    "https://calculadora-preco-venda.streamlit.app/"
)

# Projeto 16/02/2026 00:38 
# render_python_app(
#      "📝 Análise de Custo: CLT",
#      "Pare de errar nos cálculos trabalhistas! Calcule com precisão todos os custos de CLT e PJ, compare regimes, descubra a margem real de lucro por funcionário e processe equipes inteiras. Gere relatórios profissionais em segundos. Grátis e fácil de usar!",
#      "https://rhexpert.streamlit.app/"
# )

# # Projeto 
# render_python_app(
#      "⚖️ Calculadora de Viabilidade de Leilão Profissional",
#      "Ferramenta estratégica para investidores imobiliários. Calcula automaticamente impostos (ITBI), custos cartoriais, comissões de leiloeiro e margem de lucro líquida para arrematações seguras.",
#      "https://calculadoraleilao.streamlit.app/"
# )

# Projeto 
render_python_app(
    "📍 Extrator de Dados - Google Maps",
    "Solução de automação para prospecção B2B. Extrai informações públicas diretamente do Google Maps, como nomes, telefones e localizações, facilitando a geração de listas de leads qualificadas.",
    "https://gerarlead.streamlit.app/"
)

# # Projeto 
# render_python_app(
#      "📊 Análise Pro: Sistemas de Amortização",
#      "Simulador financeiro avançado que compara os sistemas SAC e PRICE. Ideal para análise de financiamentos de longo prazo, permitindo visualizar a evolução do saldo devedor e economia com amortizações antecipadas.",
#      "https://guiadaamortizacao.streamlit.app/"
# )

# Projeto 
render_python_app(
    "☕ Gestão de Custos: Açúcar 💵 Como eliminei mais de R$ 25 mil por ano em desperdício só no café.",
    "Aplicação voltada para qualquer empresa. Sabe aquela economia que ninguém vê? Aquela que parece pequena… até que você coloca os números na mesa?",
    "https://economiacafe.streamlit.app/"
)

exibir_rodape()
