import streamlit as st
import urllib.parse
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Treinamento Corporativo")

# --- CONFIGURAÇÃO DE ESTILO CSS AVANÇADO ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hero Section */
    .hero-title {
        background: linear-gradient(135deg, #ffffff 30%, #00b4d8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 15px;
        letter-spacing: -2px;
        line-height: 1.1;
    }
    
    /* CENTRALIZAÇÃO DO SUBTÍTULO */
    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.3rem;
        text-align: center;
        max-width: 850px;
        margin: 0 auto 60px auto;
        line-height: 1.6;
        font-weight: 300;
        display: block;
    }

    /* Manifesto Section com Efeito Glass */
    .manifesto-box {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 32px;
        padding: 60px;
        margin-bottom: 80px;
        text-align: center;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
    }

    /* Badge de ROI */
    .roi-badge {
        display: inline-block;
        background: rgba(0, 180, 216, 0.15);
        color: #00b4d8;
        padding: 8px 20px;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.9rem;
        margin-top: 25px;
        border: 1px solid rgba(0, 180, 216, 0.3);
    }

    /* CARDS REFINADOS */
    .feature-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 45px 30px;
        text-align: center;
        height: 350px; 
        display: flex;
        flex-direction: column;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .feature-card:hover {
        border-color: rgba(0, 180, 216, 0.5);
        transform: translateY(-12px);
        background: rgba(30, 41, 59, 0.7);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }

    .feature-icon {
        background: linear-gradient(135deg, rgba(0, 180, 216, 0.1), rgba(0, 119, 182, 0.2));
        width: 60px;
        height: 60px;
        border-radius: 16px;
        font-size: 28px;
        margin: 0 auto 25px auto;
        display: flex;
        justify-content: center;
        align-items: center;
        color: #00b4d8;
        border: 1px solid rgba(0, 180, 216, 0.2);
    }

    /* Botão Minimalista */
    .cta-button-only-container {
        display: flex;
        justify-content: center;
        margin: 80px 0;
    }

    .btn-whatsapp-premium {
        background: #ffffff;
        color: #0f172a !important;
        padding: 22px 50px;
        border-radius: 100px;
        text-decoration: none;
        font-size: 1.1rem;
        font-weight: 700;
        display: inline-flex;
        align-items: center;
        gap: 12px;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .btn-whatsapp-premium:hover {
        background: #00b4d8;
        color: white !important;
        transform: scale(1.02);
        box-shadow: 0 20px 40px rgba(0, 180, 216, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CONTEÚDO ---
st.markdown('<h1 class="hero-title">Consultoria Data-Driven</h1>', unsafe_allow_html=True)

# Manifesto com destaque de ROI e Treinamento
st.markdown("""
    <div class="manifesto-box">
        <h2 style='color: white; font-size: 2.2rem; font-weight: 700; margin-bottom: 20px; letter-spacing: -1px;'>Sua empresa gera inteligência ou apenas acumula planilhas?</h2>
        <p style='color: #94a3b8; font-size: 1.25rem; line-height: 1.8; max-width: 800px; margin: 0 auto;'>
            Nossa metodologia conecta <b>Python, BI e Processos de Negócio</b> para transformar dados brutos em decisões estratégicas automáticas.
        </p>
        <div style='margin-top: 30px; border-top: 1px solid rgba(255,255,255,0.1); pt-20px;'>
            <p style='color: #e2e8f0; font-size: 1.1rem; margin-top: 25px;'>
                Metodologia validada em grandes players do mercado, entregando um <b>ROI comprovado entre 35% e 42%</b> em projetos de capacitação e automação.
            </p>
            <div class="roi-badge">📈 Performance Garantida: ROI Mínimo de 35%</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- GRID DE BENEFÍCIOS ---
st.markdown("<h3 style='text-align: center; color: white; margin-bottom: 50px; font-weight: 400; letter-spacing: 2px; text-transform: uppercase; font-size: 0.9rem;'>Pilares de Atuação</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

features = [
    {"icon": "⚡", "title": "Automação", "text": "Substitua processos manuais por fluxos inteligentes e ganhe tempo estratégico."},
    {"icon": "🎯", "title": "Precisão", "text": "Single source of truth: dados íntegros vindos direto da fonte de origem."},
    {"icon": "📈", "title": "Escalabilidade", "text": "Arquiteturas robustas projetadas para suportar o crescimento do seu negócio."},
    {"icon": "🎓", "title": "Cultura", "text": "Treinamentos in-company para instaurar uma mentalidade Data-Driven real."}
]

cols = [col1, col2, col3, col4]
for i, f in enumerate(features):
    with cols[i]:
        st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{f['icon']}</div>
                <h4 style="color: white; margin-bottom: 15px; font-weight: 600;">{f['title']}</h4>
                <p style="color: #64748b; font-size: 0.95rem; line-height: 1.5;">{f['text']}</p>
            </div>
        """, unsafe_allow_html=True)

# --- WHATSAPP ---
telefone = "5511977019335"
mensagem_url = urllib.parse.quote("Olá Rodrigo, vi sua página de consultoria e gostaria de agendar uma conversa estratégica.")
link_whatsapp = f"https://wa.me/{telefone}?text={mensagem_url}"

st.markdown(f"""
    <div class="cta-button-only-container">
        <a href="{link_whatsapp}" target="_blank" class="btn-whatsapp-premium">
            <span>Falar com um Especialista</span>
        </a>
    </div>
""", unsafe_allow_html=True)

exibir_rodape()
