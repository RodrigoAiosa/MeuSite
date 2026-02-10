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

    .manifesto-box {
        background: rgba(15, 23, 42, 0.6);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 32px;
        padding: 60px;
        margin-bottom: 80px;
        text-align: center;
    }

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

    /* --- CARDS COM EFEITO OVERLAY DE TEXTO --- */
    .feature-card {
        background: rgba(30, 41, 59, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 40px 25px;
        text-align: center;
        height: 380px; 
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
    }

    .card-content {
        transition: opacity 0.3s ease;
    }

    .card-story {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: #00b4d8;
        color: white;
        padding: 30px 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9rem;
        font-weight: 500;
        line-height: 1.5;
        opacity: 0;
        transform: translateY(20px);
        transition: all 0.4s ease;
    }

    .feature-card:hover .card-content {
        opacity: 0;
    }

    .feature-card:hover .card-story {
        opacity: 1;
        transform: translateY(0);
    }

    .feature-icon {
        background: rgba(0, 180, 216, 0.1);
        width: 50px; height: 50px;
        border-radius: 12px;
        font-size: 24px;
        margin: 0 auto 20px auto;
        display: flex; justify-content: center; align-items: center;
        color: #00b4d8;
    }

    .cta-button-only-container {
        display: flex; justify-content: center; margin: 60px 0;
    }

    .btn-whatsapp-premium {
        background: #ffffff; color: #0f172a !important;
        padding: 18px 45px; border-radius: 100px;
        text-decoration: none; font-weight: 700;
        transition: all 0.3s ease;
    }

    .btn-whatsapp-premium:hover {
        background: #00b4d8; color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CONTEÚDO ---
st.markdown('<h1 class="hero-title">Consultoria Data-Driven</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="manifesto-box">
        <h2 style='color: white; font-size: 2.2rem; font-weight: 700; margin-bottom: 20px;'>Sua empresa gera inteligência ou apenas acumula planilhas?</h2>
        <p style='color: #94a3b8; font-size: 1.25rem; line-height: 1.8; max-width: 800px; margin: 0 auto;'>
            Nossa metodologia conecta <b>Python, BI e Processos de Negócio</b> para transformar dados brutos em decisões estratégicas automáticas.
        </p>
        <div style='margin-top: 30px; border-top: 1px solid rgba(255,255,255,0.1);'>
            <p style='color: #e2e8f0; font-size: 1.1rem; margin-top: 25px;'>
                Metodologia validada em grandes players do mercado, entregando um <b>ROI comprovado entre 35% e 42%</b>.
            </p>
            <div class="roi-badge">📈 Performance Garantida: ROI Mínimo de 35%</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- GRID DE BENEFÍCIOS COM STORIES ---
col1, col2, col3, col4 = st.columns(4)

features = [
    {
        "icon": "⚡", "title": "Automação", "desc": "Substitua processos manuais por fluxos inteligentes.",
        "story": "Eliminei 40h mensais de um time financeiro ao automatizar a conciliação de 5 bancos via Python. O erro humano caiu a zero e o fechamento que levava 5 dias agora acontece em 15 minutos."
    },
    {
        "icon": "🎯", "title": "Precisão", "desc": "Dados íntegros vindo direto da fonte de origem.",
        "story": "Em um grande varejista, unifiquei o estoque físico e digital que divergia em 18%. Ao criar uma 'Single Source of Truth', reduzimos rupturas de estoque e aumentamos as vendas em 12% no primeiro trimestre."
    },
    {
        "icon": "📈", "title": "Escalabilidade", "desc": "Arquiteturas robustas para suportar o crescimento.",
        "story": "Desenvolvi um Data Lake para uma Scale-up que crescia 200% ao ano. A infraestrutura permitiu processar milhões de linhas sem lentidão, sustentando a expansão para 3 novos países sem custos extras de TI."
    },
    {
        "icon": "🎓", "title": "Cultura", "desc": "Treinamentos in-company para mentalidade real.",
        "story": "Treinei 50 gestores que antes dependiam da TI para tudo. Em 3 meses, eles mesmos criaram seus Dashboards, liberando o time de dados para focar em IA e modelos preditivos. O ROI do treinamento foi de 300%."
    }
]

cols = [col1, col2, col3, col4]
for i, f in enumerate(features):
    with cols[i]:
        st.markdown(f"""
            <div class="feature-card">
                <div class="card-content">
                    <div class="feature-icon">{f['icon']}</div>
                    <h4 style="color: white; margin-bottom: 15px;">{f['title']}</h4>
                    <p style="color: #64748b; font-size: 0.9rem;">{f['desc']}</p>
                    <p style="color: #00b4d8; font-size: 0.8rem; margin-top: 20px; font-weight: bold;">[Passe o mouse]</p>
                </div>
                <div class="card-story">
                    "{f['story']}"
                </div>
            </div>
        """, unsafe_allow_html=True)

# --- WHATSAPP ---
link_whatsapp = "https://wa.me/5511977019335?text=Ol%C3%A1%20Rodrigo,%20gostaria%20de%20uma%20conversa%20estrat%C3%A9gica."
st.markdown(f'<div class="cta-button-only-container"><a href="{link_whatsapp}" target="_blank" class="btn-whatsapp-premium">Falar com um Especialista</a></div>', unsafe_allow_html=True)

exibir_rodape()
