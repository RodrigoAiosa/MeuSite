import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse
import re

# --- REGISTRO DE ACESSO ---
registrar_acesso("🐍 AIosa Agente de IA")

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
        line-height: 1.6;
    }
    .wa-link {
        color: #00b4d8 !important;
        text-decoration: none;
        font-weight: bold;
    }
    .wa-link:hover {
        text-decoration: underline;
    }
    .iframe-container {
        border: 2px solid #31333F;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 60px;
        background-color: #f0f2f6;
    }
    .highlight-blue {
        color: #00b4d8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título customizado
st.markdown('<h1>🐍 <span class="highlight-blue">AI</span>osa Agente de IA</h1>', unsafe_allow_html=True)

st.write("Aplicações web completas desenvolvidas para automação de processos e análise financeira.")
st.markdown("---")

# --- FUNÇÃO DE TRATAMENTO DE TEXTO (A MÁGICA PARA OS TÓPICOS E LINK) ---
def formatar_texto_ia(texto):
    """
    Esta função garante que:
    1. Tópicos com ✅ ou marcadores comecem em novas linhas.
    2. O número 11977019335 vire um link clicável do WhatsApp.
    """
    if not texto:
        return ""

    # 1. Garante que qualquer ✅ ou marcador de lista (• ou *) force uma quebra de linha
    # Substituímos o emoji por ele mesmo precedido de duas quebras de linha
    texto_formatado = re.sub(r'(✅|•|\*)', r'<br><br>\1', texto)

    # 2. Criação do Hiperlink para o WhatsApp no número 11977019335
    whatsapp_url = "https://wa.me/5511977019335?text=Olá Rodrigo, vim através do seu Agente de IA!"
    link_html = f'<a href="{whatsapp_url}" target="_blank" class="wa-link">11 97701-9335</a>'
    
    # Substitui o número bruto pelo link clicável
    texto_formatado = re.sub(r'11\s?97701-?9335', link_html, texto_formatado)
    
    # Remove quebras de linha duplas excessivas que podem vir da IA
    texto_formatado = texto_formatado.replace("<br><br><br>", "<br><br>")
    
    return texto_formatado

# --- FUNÇÃO PARA RENDERIZAR APPS ---
def render_python_app(title, description, url):
    # Aplicando a formatação na descrição da página
    desc_formatada = formatar_texto_ia(description)

    st.markdown(f'<a href="{url}" target="_blank" class="project-button">{title} ↗️</a>', unsafe_allow_html=True)
    st.markdown(f'<div class="project-description">{desc_formatada}</div>', unsafe_allow_html=True)
    
    clean_url = url.split('#')[0]
    embed_url = f"{clean_url}?embed=true"
    
    st.markdown(
        f"""
        <div class="iframe-container">
            <iframe 
                src="{embed_url}" 
                width="100%" 
                height="700" 
                frameborder="0" 
                allowfullscreen
                sandbox="allow-forms allow-modals allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-downloads">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- LISTA DE PROJETOS ---
render_python_app(
    "🤖 <span class='highlight-blue'>AI</span>OSA — Assistente Virtual Inteligente",
    "Assistente virtual desenvolvido por Rodrigo Aiosa. ✅ Treinamento 100% Personalizado ✅ Levantamento prévio das necessidades ✅ Suporte via WhatsApp: 11977019335",
    "https://aiosaassistente.streamlit.app/"
)

exibir_rodape()
