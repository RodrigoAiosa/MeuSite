import streamlit as st
import streamlit.components.v1 as components
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
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
    /* Estilização para o container do componente oficial */
    .stIFrame {
        border: 2px solid #31333F;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🐍 Projetos em Python")
st.write("Aplicações web completas desenvolvidas para automação de processos e análise financeira.")

# --- FUNÇÃO ATUALIZADA PARA MELHOR COMPATIBILIDADE ---
def render_python_app(title, description, url):
    # Botão de Título
    st.markdown(f'<a href="{url}" target="_blank" class="project-button">{title} ↗️</a>', unsafe_allow_html=True)
    
    # Descrição
    st.markdown(f'<div class="project-description">{description}</div>', unsafe_allow_html=True)
    
    # Renderização via componente oficial do Streamlit (mais seguro para embeds)
    # Adicionamos ?embed=true para o Hugging Face entender que é um iframe
    embed_url = f"{url}?embed=true" if "hf.space" in url else url
    
    try:
        components.iframe(embed_url, height=700, scrolling=True)
    except:
        st.warning("Ocorreu um problema ao carregar o app incorporado. Clique no botão acima para acessar diretamente.")

# --- LISTA DE PROJETOS ---

# Projeto Novo: Calculadora ROI
render_python_app(
    "🦉 Calculadora ROI de Automação",
    "Calculadora que estima o Retorno sobre Investimento (ROI) de projetos de automação, comparando custos e ganhos financeiros.",
    "https://rodrigoaiosa-rio-automacao.hf.space"
)

# Projeto: SOS Mulher
render_python_app(
    "💼 APP S.O.S. MULHER",
    "Em 2025, dados publicados pelo Ministério da Justiça e Segurança Pública apontam que foram registrados 1.518 feminicídios.",
    "https://sosmulher.streamlit.app/"
)

# Projeto: Precificador MEI
render_python_app(
    "💼 Precificador Profissional para MEI",
    "Calculadora profissional de precificação para MEI que ajuda a definir o preço de venda com base em custos e margens.",
    "https://calculadora-preco-venda.streamlit.app/"
)

# Projeto: Google Maps Leads
render_python_app(
    "📍 Extrator de Dados - Google Maps",
    "Solução de automação para prospecção B2B. Extrai informações públicas diretamente do Google Maps.",
    "https://gerarlead.streamlit.app/"
)

# Projeto: Economia Café
render_python_app(
    "☕ Gestão de Custos: Açúcar",
    "Sabe aquela economia que ninguém vê? Aquela que parece pequena… até que você coloca os números na mesa?",
    "https://economiacafe.streamlit.app/"
)

exibir_rodape()
