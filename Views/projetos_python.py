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
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🐍 Projetos em Python")
st.write("Aplicações web completas desenvolvidas para automação de processos e análise financeira.")

# --- FUNÇÃO PARA RENDERIZAR APPS ---
def render_python_app(title, description, url):
    # Botão de Título
    st.markdown(f'<a href="{url}" target="_blank" class="project-button">{title} ↗️</a>', unsafe_allow_html=True)
    
    # Descrição
    st.markdown(f'<div class="project-description">{description}</div>', unsafe_allow_html=True)
    
    # Lógica de conversão de URL para Embed (Tratamento de Segurança)
    embed_url = url
    
    if "huggingface.co/spaces/" in url:
        # Converte a URL do Space para o link direto de embed que permite conexão
        # Ex: https://huggingface.co/spaces/rodrigoaiosa/RIO_AUTOMACAO -> https://rodrigoaiosa-rio-automacao.hf.space
        base_url = url.replace("https://huggingface.co/spaces/", "")
        user_repo = base_url.split('/')
        if len(user_repo) >= 2:
            user = user_repo[0]
            repo = user_repo[1]
            embed_url = f"https://{user}-{repo.replace('_', '-')}.hf.space"
            
    elif "streamlit.app" in url:
        # Adiciona o parâmetro embed para evitar loops de redirecionamento no Streamlit Cloud
        if "?embed=true" not in url:
            embed_url = f"{url.rstrip('/')}/?embed=true"

    # Renderização via HTML para maior compatibilidade com permissões de iframe
    components.html(
        f"""
        <iframe
            src="{embed_url}"
            frameborder="0"
            width="100%"
            height="700"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            style="border: 2px solid #31333F; border-radius: 12px;"
        ></iframe>
        """,
        height=720,
    )

# --- LISTA DE PROJETOS ---

# 1. Projeto Hugging Face
render_python_app(
    "🦉 Calculadora ROI de Automação",
    "Calculadora que estima o Retorno sobre Investimento (ROI) de projetos de automação.",
    "https://huggingface.co/spaces/rodrigoaiosa/RIO_AUTOMACAO"
)

# 2. Projeto SOS Mulher
render_python_app(
    "💼 APP S.O.S. MULHER",
    "Em 2025, dados registrados apontam a maior marca de feminicídios até o momento.",
    "https://sosmulher.streamlit.app/"
)

# 3. Projeto Precificador MEI
render_python_app(
    "💼 Precificador Profissional para MEI",
    "Calculadora de precificação que ajuda a definir o preço de venda com base em custos.",
    "https://calculadora-preco-venda.streamlit.app/"
)

# 4. Projeto Google Maps
render_python_app(
    "📍 Extrator de Dados - Google Maps",
    "Extrai informações públicas diretamente do Google Maps para geração de leads.",
    "https://gerarlead.streamlit.app/"
)

# 5. Projeto Economia Café
render_python_app(
    "☕ Gestão de Custos: Açúcar",
    "Aplicação voltada para eliminação de desperdícios e economia visível.",
    "https://economiacafe.streamlit.app/"
)

exibir_rodape()
