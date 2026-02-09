import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- ESTILO CSS PARA FLIP CARDS ---
st.markdown(
    """
    <style>
    /* Configuração do Container de Flip */
    .flip-card {
        background-color: transparent;
        width: 100%;
        height: 350px;
        perspective: 1000px;
        margin-bottom: 30px;
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

    /* Lados Frontal e Traseiro */
    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%;
        height: 100%;
        -webkit-backface-visibility: hidden;
        backface-visibility: hidden;
        border-radius: 18px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 25px;
        border: 1px solid #1f2937;
    }

    /* Estilo Frente */
    .flip-card-front {
        background-color: #111827;
        color: white;
    }

    /* Estilo Verso */
    .flip-card-back {
        background-color: #0f172a;
        color: white;
        transform: rotateY(180deg);
        border: 1px solid #00b4d8;
    }

    .card-icon { font-size: 60px; margin-bottom: 15px; }
    
    .pbi-card-title { 
        font-size: 1.4rem; 
        font-weight: bold; 
        line-height: 1.3;
        margin-bottom: 15px;
    }

    .pbi-card-tag { 
        font-size: 0.8rem; 
        color: #00b4d8; 
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .pbi-description {
        font-size: 1rem;
        color: #9ca3af;
        line-height: 1.5;
        margin-bottom: 20px;
    }

    .btn-acessar {
        background-color: #00b4d8;
        color: #111827 !important;
        padding: 8px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.9rem;
    }

    /* Ajuste para Colunas */
    [data-testid="column"] {
        padding: 0 10px !important;
    }
    
    /* Estilo Artigos */
    .article-card {
        background-color: #111827;
        padding: 30px;
        border-radius: 15px;
        border-left: 8px solid #00b4d8;
        transition: all 0.3s ease;
        margin-bottom: 20px;
        text-decoration: none !important;
    }
    .article-card:hover {
        background-color: #1a2233;
        transform: translateX(12px);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; font-size: 3rem;'>📊 Dashboards Estratégicos</h1>", unsafe_allow_html=True)
st.write("")

# --- DADOS DOS PROJETOS ---
pbi_projects = [
    {
        "title": "💳 Relatório STONE", 
        "icon": "🏛️",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard interativo de <b>Faturamento B2B</b>: monitora KPIs (Faturamento, Margem, Ticket Médio), evolução mensal e filtros regionais."
    },
    {
        "title": "📊 Vendas Meta vs Realizado", 
        "icon": "📈",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard de <b>Recrutamento e Seleção</b>: monitora vagas abertas, tempo de fechamento, funil de candidatos e custos por contratação."
    },
    {
        "title": "📦 Controle de Pedidos BNZ", 
        "icon": "📦",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard de <b>Gestão de Estoque</b>: controla níveis de inventário, giro de estoque, produtos obsoletos e necessidade de reposição."
    },
    {
        "title": "🎯 Análise Dados Estratégica", 
        "icon": "🎯",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard de <b>Controle de Metas e Vendas</b>: faturamento real vs. orçado, performance de vendedores e crescimento anual (YoY)."
    },
    {
        "title": "👥 People Analytics (RH)", 
        "icon": "👥",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard de <b>Controle de Comissões</b>: detalha pagamentos por vendedor, metas atingidas e precisão no cálculo de incentivos."
    },
    {
        "title": "🚀 Gestão de Negócios", 
        "icon": "🚀",
        "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9",
        "desc": "Dashboard de <b>Controle de Produção</b>: monitora volume fabricado, refugo (perdas), eficiência por turno e tempo de máquina parada."
    }
]

# --- RENDERIZAÇÃO DOS CARDS ---
for i in range(0, len(pbi_projects), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(pbi_projects):
            p = pbi_projects[i + j]
            with cols[j]:
                st.markdown(f"""
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div class="card-icon">{p['icon']}</div>
                            <div class="pbi-card-title">{p['title']}</div>
                            <div class="pbi-card-tag">PASSE O MOUSE ↻</div>
                        </div>
                        <div class="flip-card-back">
                            <div style="font-weight: bold; color: #00b4d8; margin-bottom: 10px;">DESCRIÇÃO</div>
                            <div class="pbi-description">{p['desc']}</div>
                            <a href="{p['url']}" target="_blank" class="btn-acessar">Abrir Dashboard ↗️</a>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

st.write("")
st.markdown("---")

# --- CONTEÚDO TÉCNICO & ARTIGOS ---
st.markdown("<h2 style='font-size: 2.2rem;'>💡 Conteúdo Técnico & Artigos</h2>", unsafe_allow_html=True)

artigos = [
    {"titulo": "🚀 Técnicas avançadas em BI: conectando relatórios ao banco de dados com performance", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7406927292955865088", "desc": "Estratégias para otimizar a latência e garantir a integridade dos dados."},
    {"titulo": "☑️ A Revolução das Medidas DAX no Power BI", "url": "https://www.linkedin.com/feed/update/urn:li:activity:7287584764490891266", "desc": "Aprenda como otimizar seus modelos de dados com técnicas avançadas de cálculo."}
]

for art in artigos:
    st.markdown(f"""
        <a href="{art['url']}" target="_blank" style="text-decoration: none;">
            <div class="article-card">
                <h4 style="color: white; margin: 0; font-weight: bold;">{art['titulo']}</h4>
                <p style="color: #9ca3af; margin-top: 10px;">{art['desc']}</p>
            </div>
        </a>
    """, unsafe_allow_html=True)

exibir_rodape()
