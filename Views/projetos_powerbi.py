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
    }
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        text-align: center;
        transition: transform 0.8s;
        transform-style: preserve-3d;
    }
    .flip-card:hover .flip-card-inner { transform: rotateY(180deg); }
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
    .pbi-description { font-size: 0.95rem; color: #9ca3af; line-height: 1.4; margin-bottom: 15px; }
    .btn-acessar {
        background-color: #00b4d8;
        color: #111827 !important;
        padding: 8px 20px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .share-container { display: flex; gap: 15px; margin-top: 10px; }
    .share-icon { color: #9ca3af; font-size: 1.4rem; transition: 0.3s; text-decoration: none; }
    .share-icon:hover { transform: scale(1.2); }
    .icon-li:hover { color: #0077b5; }
    .icon-wa:hover { color: #25d366; }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>📊 Dashboards Estratégicos</h1>", unsafe_allow_html=True)

# --- DADOS DOS PROJETOS (USANDO SEUS LINKS REAIS) ---
pbi_projects = [
    {"title": "💳 Relatório STONE", "icon": "🏛️", "url": "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Dashboard interativo de Faturamento B2B: monitora KPIs (Faturamento, Margem, Ticket Médio), evolução mensal e filtros regionais."},
    {"title": "📊 Vendas Meta vs Realizado", "icon": "📈", "url": "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Dashboard de Recrutamento e Seleção: monitora vagas abertas, tempo de fechamento, funil de candidatos e custos por contratação."},
    {"title": "📦 Controle de Pedidos BNZ", "icon": "📦", "url": "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Dashboard de Gestão de Estoque: controla níveis de inventário, giro de estoque, produtos obsoletos e necessidade de reposição."},
    {"title": "🎯 Análise Dados Estratégica", "icon": "🎯", "url": "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Dashboard de Controle de Metas e Vendas: faturamento real vs. orçado, performance de vendedores e crescimento anual (YoY)."},
    {"title": "👥 People Analytics (RH)", "icon": "👥", "url": "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Dashboard de Controle de Comissões: detalha pagamentos por vendedor, metas atingidas e precisão no cálculo de incentivos."},
    {"title": "🚀 Gestão de Negócios", "icon": "🚀", "url": "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9", "desc": "Dashboard de Controle de Produção: monitora volume fabricado, refugo (perdas), eficiência por turno e tempo de máquina parada."}
]

# --- RENDERIZAÇÃO ---
for i in range(0, len(pbi_projects), 3):
    cols = st.columns(3)
    for j in range(3):
        idx = i + j
        if idx < len(pbi_projects):
            p = pbi_projects[idx]
            
            # Texto para compartilhamento com Título, Descrição e Link REAL
            share_text = f"📊 *{p['title']}*\n\n{p['desc']}\n\nLink do painel: {p['url']}"
            
            # Links de compartilhamento dinâmicos
            wa_link = f"https://api.whatsapp.com/send?text={urllib.parse.quote(share_text)}"
            li_link = f"https://www.linkedin.com/feed/?shareActive=true&text={urllib.parse.quote(share_text)}"
            
            with cols[j]:
                st.markdown(f"""
                <div class="flip-card">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div style="font-size: 50px;">{p['icon']}</div>
                            <h3>{p['title']}</h3>
                        </div>
                        <div class="flip-card-back">
                            <div class="pbi-description">{p['desc']}</div>
                            <a href="{p['url']}" target="_blank" class="btn-acessar">Abrir Painel ↗️</a>
                            <div class="share-container">
                                <a href="{li_link}" target="_blank" class="share-icon icon-li"><i class="fab fa-linkedin"></i></a>
                                <a href="{wa_link}" target="_blank" class="share-icon icon-wa"><i class="fab fa-whatsapp"></i></a>
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")
exibir_rodape()
