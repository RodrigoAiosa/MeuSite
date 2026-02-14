import streamlit as st
from utils import exibir_rodape, registrar_acesso
import urllib.parse

# --- REGISTRO DE ACESSO ---
registrar_acesso("Projetos Power BI")

# --- ESTILO CSS ---
st.markdown(
    """
    <style>
    /* Configuração do Container de Flip */
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
        z-index: 2;
        border: 1px solid #1f2937;
    }

    .flip-card-front::before {
        content: '';
        position: absolute;
        inset: 0;
        margin: auto;
        width: 102%;
        height: 102%;
        border-radius: 20px;
        background: linear-gradient(-45deg, #e81cff 0%, #00b4d8 100% );
        z-index: -10;
        pointer-events: none;
        transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .flip-card-front::after {
        content: "";
        z-index: -1;
        position: absolute;
        inset: 0;
        background: linear-gradient(-45deg, #fc00ff 0%, #00dbde 100% );
        transform: translate3d(0, 0, 0) scale(0.95);
        filter: blur(20px);
        opacity: 0.5;
        transition: all 0.6s;
    }

    .flip-card:hover .flip-card-front::after { filter: blur(30px); opacity: 0.8; }
    .flip-card:hover .flip-card-front::before { transform: rotate(-90deg) scaleX(1.34) scaleY(0.77); }

    .card-icon { font-size: 60px; margin-bottom: 15px; z-index: 2; }
    
    .pbi-card-title { 
        font-size: 1.4rem; 
        font-weight: bold; 
        line-height: 1.3;
        margin-bottom: 15px;
        z-index: 2;
    }

    .pbi-card-tag { 
        font-size: 0.8rem; 
        color: #000000; 
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        z-index: 2;
        background: rgba(255, 255, 255, 0.2);
        padding: 4px 12px;
        border-radius: 20px;
    }

    .flip-card-back {
        background-color: #0f172a;
        color: white;
        transform: rotateY(180deg);
        border: 2px solid #00b4d8;
    }

    .pbi-description {
        font-size: 0.95rem;
        color: #9ca3af;
        line-height: 1.4;
        margin-bottom: 15px;
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

    .share-container {
        display: flex;
        gap: 15px;
        margin-top: 10px;
        align-items: center;
    }
    
    .share-icon {
        color: #9ca3af;
        font-size: 1.4rem;
        transition: 0.3s;
        text-decoration: none;
    }
    
    .share-icon:hover { transform: scale(1.2); }
    .icon-li:hover { color: #0077b5; }
    .icon-wa:hover { color: #25d366; }

    [data-testid="column"] {
        padding: 0 10px !important;
    }
    
    div[data-testid="stHorizontalBlock"] {
        gap: 20px !important;
    }

    .delay-1 { animation-delay: 0.1s; }
    .delay-2 { animation-delay: 0.2s; }
    .delay-3 { animation-delay: 0.3s; }
    .delay-4 { animation-delay: 0.4s; }
    .delay-5 { animation-delay: 0.5s; }
    .delay-6 { animation-delay: 0.6s; }
    </style>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center; font-size: 3rem;'>📊 Dashboards Estratégicos</h1>", unsafe_allow_html=True)
st.write("")

# --- DADOS DOS PROJETOS ---
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
            
            clean_desc = p['desc'].replace("<b>", "").replace("</b>", "")
            
            # --- WHATSAPP: URL individual do painel ---
            wa_text = f"🚀 *{p['title']}*\n\n💡 {clean_desc}\n\n🔗 Confira o painel aqui: {p['url']}"
            wa_link = f"https://api.whatsapp.com/send?text={urllib.parse.quote(wa_text)}"
            
            # --- LINKEDIN: URL individual do painel ---
            li_text = f"📊 Confira este Dashboard Estratégico: {p['title']}\n\n{clean_desc}\n\nLink direto:\n"
            # O link do painel é concatenado após o texto para o LinkedIn puxar o preview
            li_link = f"https://www.linkedin.com/feed/?shareActive=true&text={urllib.parse.quote(li_text)}%20{urllib.parse.quote(p['url'])}"
            
            with cols[j]:
                st.markdown(f"""
                <div class="flip-card delay-{idx+1}">
                    <div class="flip-card-inner">
                        <div class="flip-card-front">
                            <div class="card-icon">{p['icon']}</div>
                            <div class="pbi-card-title">{p['title']}</div>
                            <div class="pbi-card-tag">PASSE O MOUSE ↻</div>
                        </div>
                        <div class="flip-card-back">
                            <div style="font-weight: bold; color: #00b4d8; margin-bottom: 8px;">PROJETO</div>
                            <div class="pbi-description">{p['desc']}</div>
                            <a href="{p['url']}" target="_blank" class="btn-acessar">Abrir Dashboard ↗️</a>
                            <div style="font-size: 0.8rem; color: #9ca3af; margin-top: 5px;">Compartilhar:</div>
                            <div class="share-container">
                                <a href="{li_link}" target="_blank" class="share-icon icon-li"><i class="fab fa-linkedin"></i></a>
                                <a href="{wa_link}" target="_blank" class="share-icon icon-wa"><i class="fab fa-whatsapp"></i></a>
                            </div>
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
            <div class="article-card" style="background-color: #111827; padding: 30px; border-radius: 15px; border-left: 8px solid #00b4d8; transition: all 0.3s ease; margin-bottom: 20px;">
                <h4 style="color: white; margin: 0; font-weight: bold;">{art['titulo']}</h4>
                <p style="color: #9ca3af; margin-top: 10px;">{art['desc']}</p>
            </div>
        </a>
    """, unsafe_allow_html=True)

exibir_rodape()
