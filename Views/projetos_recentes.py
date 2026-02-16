import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- CONFIG ---
st.set_page_config(page_title="Portfólio", page_icon="🚀", layout="wide")

# --- REGISTRO ---
registrar_acesso("Vitrine de Projetos")

# --- CSS + FONT AWESOME ---
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
    .project-card {
        background: #111827;
        border-radius: 18px;
        padding: 25px;
        border: 1px solid #1f2937;
        margin-bottom: 20px;
        text-align: center;
        transition: 0.3s;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 280px;
    }

    .project-card:hover {
        transform: translateY(-6px);
        border: 1px solid #00b4d8;
    }

    .project-title {
        font-size: 1.1rem;
        font-weight: bold;
        color: white;
        margin-bottom: 20px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .view-button {
        background-color: #00b4d8 !important;
        color: #111827 !important;
        padding: 10px 20px;
        border-radius: 8px;
        text-decoration: none !important;
        font-weight: bold;
        font-size: 0.9rem;
        display: inline-block;
        margin-bottom: 15px;
    }

    .share-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        border-top: 1px solid #1f2937;
        padding-top: 15px;
    }

    .share-icon {
        color: #9ca3af !important;
        font-size: 1.5rem;
        transition: 0.3s;
        text-decoration: none !important;
    }

    .icon-li:hover { color: #0077b5 !important; }
    .icon-wa:hover { color: #25d366 !important; }
</style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.markdown("<h1 style='text-align:center'>🚀 Portfólio de Projetos</h1>", unsafe_allow_html=True)
st.write("")

# --- PROJETOS ---
projects = [

     {
        "title": "📊 Automatizei o cálculo de custo de funcionários e o resultado é impressionante!",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7429183442157989888",
    },

     {
        "title": "✅Solução para Extração de Dados de PDFs: ''Movimentação de Pintos e Matrizes''",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7232036572035002371",
    },

     {
        "title": "🚀 Automação em Alta Velocidade: Gerando Mil Arquivos em 30 Segundos com Python ⚡",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7250105059819040768",
    },

     {
        "title": "🎰💎A Perigosa Armadilha dos Jogos de Azar: Caça-Níqueis Manipulados 🎰💎",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7248134736940818432",
    },

     {
        "title": "🐍🐍Automação de Processos em Python: Extraindo Dados de 344 PDFs para Excel com Precisão e Eficiência",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7258568013845585920",
    },

    {
        "title": "🔵 Criei 15 medidas em DAX com um ÚNICO CLIQUE!",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7340413603101011969",
    },

    {
        "title": "🚀 Preenchimento Automático: Eficiência Total com Automação Inteligente 💡",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7368611651706617856",
    },

    {
        "title": "🦉 Python + ACCESS + HTML + CSS",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7363944902973411332",
    },

    {
        "title": "💡 A espinha dorsal do B.I. começa no Power Query💡",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7380426662678650882",
    },
    
    {
        "title": "⏳ De horas de trabalho para SEGUNDOS de execução: como a automação transforma dados em poder 🚀",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7378444187920359424",
    },

    {
        "title": "🔎 Documentar no Power BI nunca foi tão fácil: tudo em um único clique!",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7376613833274003457",
    },

    {
        "title": "🚀 Web Scraping com Python: dados certos, do jeito certo.",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7384454430533787648",
    },

    {
        "title": "✅ Pare de Perder Horas: Descubra Como a Automação Revoluciona a Coleta de Dados✅",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7387300096381595649",
    },

    {
        "title": "🎈Criando o clássico jogo TETRIS com python e usando I.A. para jogar",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401703226657406976",
    },
    
    {
        "title": "🚀 Técnicas avançadas em BI: conectando relatórios ao banco de dados com performance",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7406927292955865088",
    },

    {
        "title": "🧠 Por que conhecer as tabelas e seus relacionamentos é vital em qualquer projeto de BI?",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7415581668649877504",
    },

    {
        "title": "🚗 Contagem de veículos em tempo real: um projeto prático de visão computacional com Python",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422736985196371969",
    },
    
    {
        "title": "🚗💡 Evoluindo o Sistema de Contagem de Veículos: Agora com Áreas Personalizadas",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7423354824370470912",
    },
    
    {
        "title": "🎈 Domando a Web: Automatizando a Coleta de Dados",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7396548688942231552",
    },
    {
        "title": "💡 Chega de Sofrer Enviando Currículo na Mão – Automatize AGORA",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7401302855799828480",
    },
    {
        "title": "🚀 Por que este script muda a forma de olhar para o mercado de trabalho",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7417316742781399040",
    },
    {
        "title": "🏛️ O Fim da Era Manual: Dashboard Automático",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425547898580328449",
    },
    {
        "title": "📊 Análise Pro: Sistemas de Amortização",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425612242248835073/",
    },
    {
        "title": "📍 Ciência por trás da Prospecção de Alta Performance",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7425188593134026752",
    },
    {
        "title": "🚗 Contagem de Veículos em Tempo Real (Visão Computacional)",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422736985196371969",
    },
    {
        "title": "💡 Pedra, Papel e Tesoura com Inteligência Artificial",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7422420309632303104",
    },
    {
        "title": "❤️ O dia em que a IA me ajudou como PAI",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7420842332155142144",
    },
     {
        "title": "🚀 A Revolução na Produtividade do BI: Conheça a Nova Guia que Transforma Análises em Resultados!",
        "link": "https://www.linkedin.com/feed/update/urn:li:activity:7276209357732659200",
    }
]
# --- GRID ---
cols = st.columns(3)

for idx, p in enumerate(projects):
    # Para o LinkedIn, vamos usar apenas a URL do conteúdo
    li_share_url = f"https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(p['link'])}"
    
    # WhatsApp com mensagem personalizada
    wa_msg = f"Olá Rodrigo! Vi seu projeto '{p['title']}' no seu portfólio e gostaria de conversar sobre ele. O projeto é: https://www.linkedin.com/sharing/share-offsite/?url={urllib.parse.quote(p['link'])}"
    
    wa_link = f"https://wa.me/5511977019335?text={urllib.parse.quote(wa_msg)}"
    
    with cols[idx % 3]:
        # Criamos o HTML concatenando strings curtas para forçar o Streamlit a renderizar corretamente
        card_html = "<div class='project-card'>"
        card_html += f"<div class='project-title'>{p['title']}</div>"
        card_html += f"<div><a href='{p['link']}' target='_blank' class='view-button'>Ver Demonstração</a></div>"
        card_html += "<div class='share-container'>"
        card_html += f"<a href='{li_share_url}' target='_blank' class='share-icon icon-li'><i class='fab fa-linkedin'></i></a>"
        card_html += f"<a href='{wa_link}' target='_blank' class='share-icon icon-wa'><i class='fab fa-whatsapp'></i></a>"
        card_html += "</div></div>"
        
        st.markdown(card_html, unsafe_allow_html=True)

# --- RODAPÉ ---
exibir_rodape()



