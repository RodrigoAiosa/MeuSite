import streamlit as st
import urllib.parse
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---

# --- ESTILO LANDING PAGE ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .main, [data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
}

[data-testid="stAppViewContainer"] {
    background-color: #060912 !important;
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(0,180,216,0.10) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(0,100,180,0.06) 0%, transparent 50%);
}

[data-testid="stHeader"] { background: transparent !important; }

/* Fonte apenas no conteúdo principal */
.main h1, .main h2, .main h3, .main h4,
.main p, .main a, .main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}

/* Preserva ícones Material do Streamlit */
.material-symbols-rounded,
.material-icons,
[data-testid*="Collapse"] span,
[data-testid*="collapse"] span {
    font-family: 'Material Symbols Rounded', 'Material Icons' !important;
}

[data-testid="stMarkdownContainer"] { width: 100% !important; }
.block-container {
    max-width: 100% !important;
    padding-left: 4rem !important;
    padding-right: 4rem !important;
}

/* ── HERO TITLE ── */
.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2.6rem, 5vw, 4rem);
    font-weight: 800;
    text-align: center;
    letter-spacing: -1.5px;
    line-height: 1.1;
    margin-bottom: 16px;
    background: linear-gradient(135deg, #f0f4ff 40%, #00b4d8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ── MANIFESTO BOX ── */
.manifesto-box {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.25) 100%);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(0,180,216,0.15);
    border-radius: 24px;
    padding: 60px;
    margin-bottom: 80px;
    text-align: center;
    box-shadow: 0 20px 60px rgba(0,0,0,0.4), inset 0 1px 0 rgba(0,180,216,0.1);
    position: relative;
    overflow: hidden;
}

.manifesto-box::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.5), transparent);
}

.roi-badge {
    display: inline-block;
    background: rgba(0,180,216,0.1);
    color: #00b4d8;
    padding: 10px 28px;
    border-radius: 100px;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700;
    font-size: 0.85rem;
    margin-top: 25px;
    border: 1px solid rgba(0,180,216,0.35);
    text-transform: uppercase;
    letter-spacing: 2px;
}

/* ── FEATURE CARDS ── */
.feature-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.25) 100%);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 40px 25px;
    text-align: center;
    height: 400px;
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.feature-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.4), transparent);
    opacity: 0;
    transition: opacity 0.35s ease;
}

.feature-card:hover {
    transform: translateY(-4px);
    border-color: rgba(0,180,216,0.2);
    box-shadow: 0 20px 40px rgba(0,0,0,0.4), 0 0 0 1px rgba(0,180,216,0.1);
}

.feature-card:hover::before { opacity: 1; }

.card-story {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(135deg, rgba(0,180,216,0.15) 0%, rgba(0,100,180,0.2) 100%);
    border: 1px solid rgba(0,180,216,0.3);
    border-radius: 20px;
    color: #e2e8f0;
    padding: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.95rem;
    font-weight: 400;
    line-height: 1.7;
    opacity: 0;
    transform: scale(0.95);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    backdrop-filter: blur(8px);
}

.feature-card:hover .card-story {
    opacity: 1;
    transform: scale(1);
}

.feature-icon {
    background: rgba(0,180,216,0.08);
    width: 60px; height: 60px;
    border-radius: 16px;
    font-size: 26px;
    margin: 0 auto 20px auto;
    display: flex; justify-content: center; align-items: center;
    border: 1px solid rgba(0,180,216,0.2);
}

/* ── CORPORATE SECTION ── */
.corporate-section {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 24px;
    padding: 50px;
    margin-top: 80px;
    position: relative;
    overflow: hidden;
}

.corporate-section::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,180,216,0.4), transparent);
}

.pilar-item {
    display: flex;
    gap: 20px;
    margin-bottom: 28px;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid transparent;
    transition: all 0.3s ease;
}

.pilar-item:hover {
    background: rgba(0,180,216,0.04);
    border-color: rgba(0,180,216,0.1);
}

.pilar-icon {
    color: #00b4d8;
    font-size: 1.3rem;
    flex-shrink: 0;
    margin-top: 3px;
}

.pilar-title {
    font-family: 'Syne', sans-serif !important;
    color: #e2e8f0;
    font-weight: 700;
    font-size: 1rem;
    margin-bottom: 6px;
    letter-spacing: -0.2px;
}

.pilar-text {
    color: #4a5568;
    font-size: 0.9rem;
    line-height: 1.65;
    font-weight: 300;
}

/* ── CTA BUTTON ── */
.cta-button-only-container {
    display: flex;
    justify-content: center;
    margin: 60px 0;
}

.btn-whatsapp-premium {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: linear-gradient(135deg, #10b981, #059669);
    color: white !important;
    padding: 20px 56px;
    border-radius: 100px;
    text-decoration: none !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 1rem;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 24px rgba(16,185,129,0.2);
    border: 1px solid rgba(16,185,129,0.3);
}

.btn-whatsapp-premium:hover {
    transform: translateY(-3px);
    box-shadow: 0 20px 40px rgba(16,185,129,0.35);
    background: linear-gradient(135deg, #059669, #047857);
}

.footer-spacer { height: 60px; }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #060912; }
::-webkit-scrollbar-thumb { background: rgba(0,180,216,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0,180,216,0.4); }

</style>
""", unsafe_allow_html=True)

# --- CONTEÚDO ---
st.markdown('<h1 class="hero-title">Consultoria e Treinamento Data-Driven</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="manifesto-box">
        <h2 style='font-family:"Syne",sans-serif; color: #f0f4ff; font-size: 2.2rem; font-weight: 800; margin-bottom: 20px; letter-spacing:-1px; line-height:1.2;'>Sua empresa gera inteligência ou apenas acumula planilhas?</h2>
        <p style='color: #7b8ba8; font-size: 1.15rem; line-height: 1.85; max-width: 820px; margin: 0 auto; font-weight:300;'>
            Conectamos <b style="color:#e2e8f0; font-weight:600;">Python, BI e Processos</b> para transformar dados brutos em decisões que geram lucro imediato.
        </p>
        <div style='margin-top: 35px; border-top: 1px solid rgba(255,255,255,0.05); padding-top:28px;'>
            <p style='color: #7b8ba8; font-size: 1rem; margin-bottom: 20px; font-weight:300;'>
                Metodologia aplicada em gigantes do setor com <b style="color:#e2e8f0; font-weight:600;">ROI auditado de até 42%</b>.
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
    {"icon": "🎓", "title": "Cultura", "desc": "Independência total para seus gestores.", "story": "Treinei +250 líderes para serem donos dos seus dados. O time de TI parou de apagar incêndio e passou a focar em estratégia."}
]

cols = [col1, col2, col3, col4]
for i, f in enumerate(features):
    with cols[i]:
        st.markdown(f"""
            <div class="feature-card">
                <div class="card-content">
                    <div class="feature-icon">{f['icon']}</div>
                    <h4 style="font-family:'Syne',sans-serif; color: #e2e8f0; font-weight: 700; letter-spacing:-0.3px;">{f['title']}</h4>
                    <p style="color: #4a5568; font-size: 0.9rem; font-weight:300; line-height:1.6;">{f['desc']}</p>
                    <p style="color: #00b4d8; font-size: 0.75rem; margin-top: 40px; font-family:'Syne',sans-serif; font-weight: 800; letter-spacing:2px; text-transform:uppercase;">VER RESULTADO REAL</p>
                </div>
                <div class="card-story">"{f['story']}"</div>
            </div>
        """, unsafe_allow_html=True)

# --- NOVA SEÇÃO: PILARES DO TREINAMENTO ---
st.markdown("""
    <div class="corporate-section">
        <h3 style="font-family:'Syne',sans-serif; color: #f0f4ff; text-align: center; margin-bottom: 40px; font-size: 1.7rem; font-weight:800; letter-spacing:-0.5px;">
            Diferenciais do Treinamento Corporativo<br>
            <span style="font-family:'Syne',sans-serif; color: #00b4d8; font-size: 1rem; font-weight:600; letter-spacing:1px;">POWER BI &nbsp;•&nbsp; EXCEL &nbsp;•&nbsp; SQL &nbsp;•&nbsp; PYTHON</span>
        </h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
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

st.markdown('<div class="footer-spacer"></div>', unsafe_allow_html=True)

exibir_rodape()
