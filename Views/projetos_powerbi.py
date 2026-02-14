import streamlit as st
import urllib.parse

# ---------------- CONFIGURAÇÃO DA PÁGINA ----------------
st.set_page_config(
    page_title="Projetos Power BI",
    page_icon="📊",
    layout="wide"
)

# ---------------- CSS GLOBAL ----------------
st.markdown("""
<style>

/* Remove padding padrão */
.block-container {
    padding-top: 2rem;
}

/* FLIP CARD */
.flip-card {
    background-color: transparent;
    width: 100%;
    height: 320px;
    perspective: 1000px;
    margin-bottom: 25px;
}

.flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.8s;
    transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 16px;
    backface-visibility: hidden;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
}

/* Frente */
.flip-card-front {
    background: linear-gradient(135deg, #111827, #1f2937);
    color: white;
}

/* Verso */
.flip-card-back {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
    transform: rotateY(180deg);
    text-align: center;
}

/* Botão principal */
.btn-acessar {
    background: linear-gradient(90deg, #00b4d8, #0077b6);
    padding: 10px 20px;
    border-radius: 10px;
    color: white !important;
    text-decoration: none;
    font-weight: bold;
    margin: 10px 0;
    transition: 0.3s;
}

.btn-acessar:hover {
    transform: scale(1.05);
}

/* Botões compartilhar */
.share-btn {
    border: none;
    padding: 8px 12px;
    border-radius: 8px;
    margin: 5px;
    cursor: pointer;
    font-weight: bold;
    background: #1f2937;
    color: white;
    transition: 0.3s;
}

.share-btn:hover {
    background: #00b4d8;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# ---------------- LISTA DE PROJETOS ----------------
pbi_projects = [
    {
        "icon": "📈",
        "title": "Dashboard Comercial",
        "desc": "Análise completa de vendas, metas e performance comercial.",
        "url": "https://app.powerbi.com/view?r=SEU_LINK_AQUI"
    },
    {
        "icon": "🏭",
        "title": "Indicadores Industriais",
        "desc": "Monitoramento de produção, eficiência e perdas operacionais.",
        "url": "https://app.powerbi.com/view?r=SEU_LINK_AQUI"
    },
    {
        "icon": "💰",
        "title": "Controle Financeiro",
        "desc": "Fluxo de caixa, DRE e análise financeira estratégica.",
        "url": "https://app.powerbi.com/view?r=SEU_LINK_AQUI"
    }
]

# ---------------- TÍTULO ----------------
st.title("📊 Projetos Power BI")
st.markdown("---")

# ---------------- GRID 3 COLUNAS ----------------
cols = st.columns(3)

for i, p in enumerate(pbi_projects):

    col = cols[i % 3]

    texto_share = f"Confira este projeto: {p['title']} - {p['url']}"
    texto_encoded = urllib.parse.quote(texto_share)

    li_link = f"https://www.linkedin.com/sharing/share-offsite/?url={p['url']}"
    wa_link = f"https://wa.me/?text={texto_encoded}"

    with col:
        st.markdown(f"""
        <div class="flip-card">
            <div class="flip-card-inner">

                <div class="flip-card-front">
                    <div style="font-size:60px;">{p['icon']}</div>
                    <div style="font-size:1.3rem; font-weight:bold; margin-top:10px;">
                        {p['title']}
                    </div>
                    <div style="margin-top:15px; font-size:0.9rem; opacity:0.7;">
                        Passe o mouse ↻
                    </div>
                </div>

                <div class="flip-card-back">
                    <div style="font-weight:bold; font-size:1.1rem; color:#00b4d8;">
                        DESCRIÇÃO
                    </div>

                    <div style="margin:15px 0; font-size:0.9rem; opacity:0.8;">
                        {p['desc']}
                    </div>

                    <a href="{p['url']}" target="_blank" class="btn-acessar">
                        Abrir Dashboard ↗️
                    </a>

                    <div style="margin-top:10px;">Compartilhar:</div>

                    <button class="share-btn"
                        onclick="window.open('{li_link}','popup','width=600,height=600')">
                        🔗 LinkedIn
                    </button>

                    <button class="share-btn"
                        onclick="window.open('{wa_link}','popup','width=600,height=600')">
                        🟢 WhatsApp
                    </button>

                </div>

            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------------- RODAPÉ ----------------
st.markdown("---")
st.caption("© 2026 - Portfólio Profissional")
