import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- ESTILO CSS ---
st.markdown(
    """
    <style>
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 420px;
        perspective: 1000px;
        margin-bottom: 20px;
        animation: fadeInUp 0.8s ease-out forwards;
        opacity: 0;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
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
        border-radius: 18px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 25px;
        backface-visibility: hidden;
    }

    .flip-card-front {
        background-color: #111827;
        color: white;
        border: 1px solid #1f2937;
    }

    .flip-card-back {
        background-color: #0f172a;
        color: white;
        transform: rotateY(180deg);
        border: 2px solid #00b4d8;
    }

    .btn-acessar {
        background-color: #00b4d8;
        color: #111827 !important;
        padding: 8px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
        margin-bottom: 15px;
        display: inline-block;
    }

    .share-btn {
        background: transparent;
        border: none;
        font-size: 22px;
        cursor: pointer;
        color: #9ca3af;
        transition: 0.3s;
        margin: 0 8px;
    }

    .share-btn:hover {
        transform: scale(1.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>📊 Dashboards Estratégicos</h1>", unsafe_allow_html=True)
st.write("")

# --- DADOS DOS PROJETOS ---
pbi_projects = [
    {"title": "💳 Relatório STONE", "icon": "🏛️", "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
     "desc": "Dashboard interativo de Faturamento B2B: monitora KPIs (Faturamento, Margem, Ticket Médio), evolução mensal e filtros regionais."},

    {"title": "📊 Vendas Meta vs Realizado", "icon": "📈", "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
     "desc": "Dashboard de Recrutamento e Seleção: monitora vagas abertas, tempo de fechamento, funil de candidatos e custos por contratação."},

    {"title": "📦 Controle de Pedidos BNZ", "icon": "📦", "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
     "desc": "Dashboard de Gestão de Estoque: controla níveis de inventário, giro de estoque, produtos obsoletos e necessidade de reposição."},

    {"title": "🎯 Análise Dados Estratégica", "icon": "🎯", "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
     "desc": "Dashboard de Controle de Metas e Vendas: faturamento real vs. orçado, performance de vendedores e crescimento anual (YoY)."},

    {"title": "👥 People Analytics (RH)", "icon": "👥", "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
     "desc": "Dashboard de Controle de Comissões: detalha pagamentos por vendedor, metas atingidas e precisão no cálculo de incentivos."},

    {"title": "🚀 Gestão de Negócios", "icon": "🚀", "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
     "desc": "Dashboard de Controle de Produção: monitora volume fabricado, refugo (perdas), eficiência por turno e tempo de máquina parada."}
]

# --- RENDERIZAÇÃO EM 3 COLUNAS ---
for i in range(0, len(pbi_projects), 3):
    cols = st.columns(3)

    for j in range(3):
        idx = i + j
        if idx < len(pbi_projects):
            p = pbi_projects[idx]

            # LINKEDIN FORMATADO
            li_text = (
                f"🚀 {p['title']}%0A%0A"
                f"💡 {p['desc']}%0A%0A"
                f"🔗 Confira o painel aqui:%0A"
                f"{p['url']}"
            )

            li_link = f"https://www.linkedin.com/feed/?shareActive=true&text={li_text}"

            # WHATSAPP
            wa_text = f"🚀 {p['title']}\n\n💡 {p['desc']}\n\n🔗 Confira o painel aqui:\n{p['url']}"
            wa_link = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_text)}"

            with cols[j]:
                st.markdown(f"""
                <div class="flip-card">
                    <div class="flip-card-inner">

                        <div class="flip-card-front">
                            <div style="font-size:60px;">{p['icon']}</div>
                            <div style="font-weight:bold; font-size:1.2rem;">
                                {p['title']}
                            </div>
                            <div>PASSE O MOUSE ↻</div>
                        </div>

                        <div class="flip-card-back">
                            <div style="font-weight:bold; color:#00b4d8;">PROJETO</div>

                            <div style="margin:10px 0; color:#9ca3af;">
                                {p['desc']}
                            </div>

                            <a href="{p['url']}" target="_blank" class="btn-acessar">
                                Abrir Dashboard ↗️
                            </a>

                            <div>Compartilhar:</div>

                            <button class="share-btn"
                                onclick="window.open('{li_link}','popup','width=600,height=600')">
                                🔗 in
                            </button>

                            <button class="share-btn"
                                onclick="window.open('{wa_link}','popup','width=600,height=600')">
                                🟢 wa
                            </button>

                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
exibir_rodape()
