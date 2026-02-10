import streamlit as st
import urllib.parse
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Treinamento Corporativo")

# --- CONFIGURAÇÃO DE ESTILO PSICOLOGIA DAS CORES ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #020617;
    }

    /* Hero Title */
    .hero-title {
        background: linear-gradient(135deg, #ffffff 40%, #fbbf24 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 15px;
        letter-spacing: -2px;
    }

    /* Manifesto Box */
    .manifesto-box {
        background: rgba(30, 41, 59, 0.5);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(251, 191, 36, 0.2);
        border-radius: 32px;
        padding: 60px;
        margin-bottom: 80px;
        text-align: center;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
    }

    .roi-badge {
        display: inline-block;
        background: linear-gradient(90deg, rgba(251, 191, 36, 0.2), rgba(245, 158, 11, 0.2));
        color: #fbbf24;
        padding: 10px 25px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1rem;
        margin-top: 25px;
        border: 1px solid #fbbf24;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Cards de Benefício */
    .feature-card {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 40px 25px;
        text-align: center;
        height: 400px; 
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
    }

    .card-story {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
        color: white;
        padding: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1rem;
        font-weight: 600;
        opacity: 0;
        transform: scale(0.9);
        transition: all 0.4s ease;
    }

    .feature-card:hover .card-story {
        opacity: 1;
        transform: scale(1);
    }

    .feature-icon {
        background: rgba(251, 191, 36, 0.1);
        width: 60px; height: 60px;
        border-radius: 16px;
        font-size: 28px;
        margin: 0 auto 20px auto;
        display: flex; justify-content: center; align-items: center;
        color: #fbbf24;
        border: 1px solid rgba(251, 191, 36, 0.3);
    }

    /* --- NOVA SEÇÃO: DIFERENCIAIS CORPORATIVOS --- */
    .corporate-section {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0) 0%, rgba(30, 41, 59, 0.4) 100%);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 32px;
        padding: 50px;
        margin-top: 80px;
    }

    .pilar-item {
        display: flex;
        gap: 20px;
        margin-bottom: 30px;
        padding: 20px;
        border-radius: 16px;
        transition: background 0.3s ease;
    }

    .pilar-item:hover {
        background: rgba(255, 255, 255, 0.03);
    }

    .pilar-icon {
        color: #fbbf24;
        font-size: 1.5rem;
        flex-shrink: 0;
        margin-top: 5px;
    }

    .pilar-title {
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
        margin-bottom: 5px;
    }

    .pilar-text {
        color: #94a3b8;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* Botão de Conversão */
    .cta-button-only-container {
        display: flex; justify-content: center; margin: 60px 0;
    }

    .btn-whatsapp-premium {
        background: #10b981;
        color: white !important;
        padding: 24px 60px;
        border-radius: 100px;
        text-decoration: none;
        font-size: 1.2rem;
        font-weight: 800;
        transition: all 0.3s ease;
        text-transform: uppercase;
    }

    .btn-whatsapp-premium:hover {
        background: #059669;
        transform: translateY(-3px);
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CONTEÚDO ---
st.markdown('<h1 class="hero-title">Consultoria e Treinamento Data-Driven</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="manifesto-box">
        <h2 style='color: white; font-size: 2.3rem; font-weight: 700; margin-bottom: 20px;'>Sua empresa gera inteligência ou apenas acumula planilhas?</h2>
        <p style='color: #cbd5e1; font-size: 1.3rem; line-height: 1.8; max-width: 850px; margin: 0 auto;'>
            Conectamos <b>Python, BI e Processos</b> para transformar dados brutos em decisões que geram lucro imediato.
        </p>
        <div style='margin-top: 35px; border-top: 1px solid rgba(255,255,255,0.1);'>
            <p style='color: #ffffff; font-size: 1.1rem; margin-top: 25px; opacity: 0.9;'>
                Metodologia aplicada em gigantes do setor com <b>ROI auditado de até 42%</b>.
            </p>
            <div class="roi-badge">💎 Resultado Garantido: ROI de 35% a 42%</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- GRID DE BENEFÍCIOS ---
col1, col2, col3, col4 = st.columns(4)

features = [
    {"icon": "⚡", "title": "Automação", "desc": "Libere seu time do operacional repetitivo.", "story": "Economizei 40h/mês de um time financeiro. O que levava 5 dias de planilha hoje acontece em 5 segundos."},
    {"icon": "🎯", "title": "Precisão", "desc": "Decisões baseadas em fatos, não em palpites.", "story": "Reduzi em 28% a divergência de estoque de um grande varejista. Menos ruptura, mais dinheiro no caixa."},
    {"icon": "📈", "title": "Escalabilidade", "desc": "Estrutura pronta para dobrar de tamanho.", "story": "Criei o Data Lake de uma Scale-up que triplicou de tamanho em um ano sem precisar contratar mais analistas."},
    {"icon": "🎓", "title": "Cultura", "desc": "Independência total para seus gestores.", "story": "Treinei 50 líderes para serem donos dos seus dados. O time de TI parou de apagar incêndio e passou a focar em estratégia."}
]

cols = [col1, col2, col3, col4]
for i, f in enumerate(features):
    with cols[i]:
        st.markdown(f"""
            <div class="feature-card">
                <div class="card-content">
                    <div class="feature-icon">{f['icon']}</div>
                    <h4 style="color: white; font-weight: 700;">{f['title']}</h4>
                    <p style="color: #94a3b8; font-size: 0.95rem;">{f['desc']}</p>
                    <p style="color: #fbbf24; font-size: 0.8rem; margin-top: 40px; font-weight: 800;">VER RESULTADO REAL</p>
                </div>
                <div class="card-story">"{f['story']}"</div>
            </div>
        """, unsafe_allow_html=True)

# --- NOVA SEÇÃO: PILARES DO TREINAMENTO ---
st.markdown("""
    <div class="corporate-section">
        <h3 style="color: white; text-align: center; margin-bottom: 40px; font-size: 1.8rem;">
            Diferenciais do Treinamento Corporativo <br>
            <span style="color: #fbbf24; font-size: 1.2rem;">(Power BI • Excel • SQL • Python)</span>
        </h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div class="pilar-item">
                <div class="pilar-icon">✅</div>
                <div>
                    <div class="pilar-title">Treinamento 100% Personalizado</div>
                    <div class="pilar-text">Conteúdo totalmente direcionado às necessidades reais da empresa, focado em solucionar problemas práticos e otimizar processos internos.</div>
                </div>
            </div>
            <div class="pilar-item">
                <div class="pilar-icon">✅</div>
                <div>
                    <div class="pilar-title">Levantamento Prévio de Necessidades</div>
                    <div class="pilar-text">Realizamos um diagnóstico das demandas antes do início, garantindo que o aprendizado seja relevante e aplicável imediatamente.</div>
                </div>
            </div>
            <div class="pilar-item">
                <div class="pilar-icon">✅</div>
                <div>
                    <div class="pilar-title">Material Completo & Vitalício</div>
                    <div class="pilar-text">Aulas gravadas e disponibilizadas para a empresa, permitindo consultas futuras, treinamento de novos colaboradores ou reciclagem.</div>
                </div>
            </div>
            <div class="pilar-item">
                <div class="pilar-icon">✅</div>
                <div>
                    <div class="pilar-title">Suporte Pós-Treinamento (WhatsApp)</div>
                    <div class="pilar-text">Grupo exclusivo para suporte prático e esclarecimento de dúvidas, garantindo que o conhecimento se transforme em execução.</div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- WHATSAPP ---
link_whatsapp = "https://wa.me/5511977019335?text=Olá Rodrigo, gostaria de agendar uma conversa sobre os treinamentos corporativos."
st.markdown(f'<div class="cta-button-only-container"><a href="{link_whatsapp}" target="_blank" class="btn-whatsapp-premium">Agendar Reunião Estratégica</a></div>', unsafe_allow_html=True)

exibir_rodape()


