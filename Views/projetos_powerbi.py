import streamlit as st
import urllib.parse

st.set_page_config(page_title="Projetos Power BI", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
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
    transition: transform 0.7s;
    transform-style: preserve-3d;
}

.flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
}

.flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 14px;
    backface-visibility: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 18px;
}

.flip-card-front {
    background: #111827;
    color: white;
}

.flip-card-back {
    background: #0f172a;
    color: white;
    transform: rotateY(180deg);
}

.btn {
    background: #00b4d8;
    padding: 8px 18px;
    border-radius: 8px;
    text-decoration: none;
    color: black !important;
    font-weight: bold;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Projetos Power BI")
st.markdown("---")

# ---------------- DADOS ----------------
projects = [
    {
        "icon": "💳",
        "title": "Relatório STONE",
        "desc": "Dashboard interativo de Faturamento B2B com KPIs e evolução mensal.",
        "url": "https://app.powerbi.com"
    },
    {
        "icon": "📦",
        "title": "Controle de Pedidos",
        "desc": "Gestão de pedidos, status e acompanhamento operacional.",
        "url": "https://app.powerbi.com"
    },
    {
        "icon": "🎯",
        "title": "Análise Estratégica",
        "desc": "Indicadores executivos e acompanhamento de metas.",
        "url": "https://app.powerbi.com"
    },
]

cols = st.columns(3)

for i, p in enumerate(projects):
    with cols[i]:
        html = f"""
        <div class="flip-card">
            <div class="flip-card-inner">

                <div class="flip-card-front">
                    <div style="font-size:55px;">{p['icon']}</div>
                    <div style="font-weight:bold; margin-top:10px;">
                        {p['title']}
                    </div>
                    <div style="margin-top:10px; font-size:0.85rem;">
                        Passe o mouse ↻
                    </div>
                </div>

                <div class="flip-card-back">
                    <div style="font-weight:bold;">DESCRIÇÃO</div>
                    <div style="margin:10px 0; font-size:0.9rem;">
                        {p['desc']}
                    </div>
                    <a href="{p['url']}" target="_blank" class="btn">
                        Abrir Dashboard
                    </a>
                </div>

            </div>
        </div>
        """
        st.markdown(html, unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026")
