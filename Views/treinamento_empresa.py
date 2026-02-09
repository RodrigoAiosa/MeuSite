import streamlit as st
import urllib.parse
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Treinamento Corporativo")

# --- CONFIGURAÇÃO DE ESTILO CSS AVANÇADO ---
st.markdown(
    """
    <style>
    /* Gradient Text & Hero Section */
    .hero-title {
        background: linear-gradient(90deg, #00b4d8, #90e0ef);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 10px;
    }
    
    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.4rem;
        text-align: center;
        max-width: 800px;
        margin: 0 auto 50px auto;
        line-height: 1.6;
    }

    /* Manifesto Section */
    .manifesto-box {
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.8));
        border: 1px solid rgba(0, 180, 216, 0.3);
        border-radius: 24px;
        padding: 50px;
        margin-bottom: 60px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5);
    }

    /* CARDS IGUALADOS (MESMO TAMANHO) */
    .feature-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 40px 25px;
        text-align: center;
        height: 320px; 
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
        transition: all 0.3s ease;
        margin-bottom: 20px;
    }

    .feature-card:hover {
        background: rgba(0, 180, 216, 0.05);
        border-color: #00b4d8;
        transform: translateY(-10px);
    }

    .feature-icon {
        background: linear-gradient(135deg, #00b4d8, #0077b6);
        width: 70px;
        height: 70px;
        border-radius: 18px;
        font-size: 30px;
        margin-bottom: 25px;
        display: flex;
        justify-content: center;
        align-items: center;
        box-shadow: 0 10px 20px rgba(0, 180, 216, 0.2);
    }

    /* CTA WhatsApp - SEM O FUNDO (APENAS BOTÃO) */
    .cta-button-only-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin: 50px 0;
    }

    .btn-whatsapp-premium {
        background: #25d366;
        color: white !important;
        padding: 20px 45px;
        border-radius: 15px;
        text-decoration: none;
        font-size: 1.3rem;
        font-weight: bold;
        display: inline-flex;
        align-items: center;
        gap: 15px;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(37, 211, 102, 0.3);
    }

    .btn-whatsapp-premium:hover {
        background: #20ba5a;
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(37, 211, 102, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CONTEÚDO ---
st.markdown('<h1 class="hero-title">Treinamento & Consultoria High-End</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-subtitle">Transformamos sua operação de dados em uma vantagem competitiva real.</p>', unsafe_allow_html=True)

# Manifesto
st.markdown("""
    <div class="manifesto-box">
        <h2 style='color: white; font-size: 2rem; margin-bottom: 25px;'>Sua empresa está gerando inteligência ou apenas acumulando planilhas?</h2>
        <p style='color: #cbd5e1; font-size: 1.2rem; line-height: 1.8;'>
            Nossa abordagem conecta <b>Python, BI e Processos de Negócio</b> para criar um fluxo automatizado.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- GRID DE BENEFÍCIOS IGUALADOS ---
st.markdown("<h3 style='text-align: center; margin-bottom: 40px;'>Pilares da Transformação</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

features = [
    {"icon": "⚡", "title": "Automação", "text": "Elimine o trabalho braçal e foque na estratégia do negócio."},
    {"icon": "🎯", "title": "Precisão", "text": "Dados integrados diretamente da fonte, eliminando erros humanos."},
    {"icon": "📈", "title": "Scalability", "text": "Estruturas prontas para crescer com seu volume de dados."},
    {"icon": "🎓", "title": "Data Culture", "text": "Capacite seu time com a mentalidade de BI moderna e eficiente."}
]

cols = [col1, col2, col3, col4]
for i, f in enumerate(features):
    with cols[i]:
        st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{f['icon']}</div>
                <h4 style="color: #00b4d8; margin-bottom: 15px; min-height: 50px;">{f['title']}</h4>
                <p style="color: #94a3b8; font-size: 0.95rem;">{f['text']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- WHATSAPP (APENAS BOTÃO CENTRALIZADO) ---
telefone = "5511977019335"
# Mensagem personalizada preservando o objetivo de contato direto
mensagem_url = urllib.parse.quote("Olá Rodrigo, gostaria de agendar uma consultoria estratégica.")
link_whatsapp = f"https://wa.me/{telefone}?text={mensagem_url}"

st.markdown(f"""
    <div class="cta-button-only-container">
        <a href="{link_whatsapp}" target="_blank" class="btn-whatsapp-premium">
            <span>🚀 Agendar Consultoria via WhatsApp</span>
        </a>
    </div>
""", unsafe_allow_html=True)

exibir_rodape()
