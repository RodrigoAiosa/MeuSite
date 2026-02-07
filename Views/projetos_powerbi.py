import streamlit as st

# --- ESTILO CSS PARA PADRONIZAÇÃO ---
st.markdown(
    """
    <style>
    .pbi-button {
        display: inline-block;
        background-color: #262730;
        color: #00b4d8 !important;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 15px 25px;
        margin-bottom: 10px;
        border-radius: 10px;
        text-decoration: none;
        transition: transform 0.3s, box-shadow 0.3s;
        border: 2px solid rgba(0, 180, 216, 0.2);
        width: 100%;
        max-width: 800px;
        cursor: pointer;
        text-align: left;
    }
    .pbi-button:hover {
        transform: scale(1.01);
        box-shadow: 0 8px 16px rgba(0, 180, 216, 0.3);
        border-color: #00b4d8;
    }
    .iframe-container {
        border: 2px solid #31333F;
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 60px;
        background-color: #0e1117;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Projetos Power BI")
st.write("Interaja com os dashboards abaixo ou clique nos botões para expandir.")
st.markdown("---")

# --- FUNÇÃO PARA RENDERIZAR PROJETOS ---
def render_pbi_project(title, url):
    st.markdown(f'<a href="{url}" target="_blank" class="pbi-button">{title} ↗️</a>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="iframe-container">
            <iframe 
                title="{title}" 
                width="100%" 
                height="600" 
                src="{url}" 
                frameborder="0" 
                allowFullScreen="true">
            </iframe>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- PROJETO 1: RELATÓRIO STONE (NOVO) ---
render_pbi_project(
    "💳 Relatório STONE", 
    "https://app.powerbi.com/view?r=eyJrIjoiMmViN2ZlMWMtY2Q4My00NmNmLTg0NzAtZjEzMzliNzcwMWMyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9&pageName=4a370a609e531d73a467"
)

# --- PROJETO 2: VENDAS META VS REALIZADO ---
render_pbi_project(
    "📊 Relatório de Vendas Meta vs Realizado", 
    "https://app.powerbi.com/view?r=eyJrIjoiYTg4OTdkZDUtNmIwZS00NGE1LTk2MDktMzc1YjM3ZjViN2Q5IiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9&pageName=ReportSection"
)

# --- PROJETO 3: CONTROLE DE PEDIDOS BNZ ---
render_pbi_project(
    "📦 Controle de Pedidos BNZ", 
    "https://app.powerbi.com/view?r=eyJrIjoiODE4YmZkNDItNWQ0OC00YmUyLThiZTktOTlmN2E0NWM3NTljIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9&pageName=1056dd4fdf3bfcd02dca"
)

# --- PROJETO 4: ANÁLISE DE DADOS ESTRATÉGICA ---
render_pbi_project(
    "📈 Dashboard Interativo - Análise de Dados Estratégica", 
    "https://app.powerbi.com/view?r=eyJrIjoiM2ZhYjQ5YzItNTliMS00M2QxLWFhMmItN2QzMjVhNThjY2QxIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9&pageName=afc80464d8ec000ee2b5"
)

# --- PROJETO 5: RH ---
render_pbi_project(
    "✅ A Importância de Relatórios de RH para as Empresas", 
    "https://app.powerbi.com/view?r=eyJrIjoiYmE2OGE3ODktZTUzMi00YTU2LTlkYmItYzUzY2UzNmJkMjAyIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9"
)

# --- PROJETO 6: NEGÓCIOS ---
render_pbi_project(
    "✅ A Importância de Ter um Relatório para o Seu Negócio com Power BI", 
    "https://app.powerbi.com/view?r=eyJrIjoiYzNhNDFkNzEtZmVkNy00ODZkLTgyZDYtMWIzMDQ3YWU2ZjFiIiwidCI6ImVlMmMzMDc0LTIyZDQtNGI3MC05MTdjLTJiYmFhZjUwZGQ4MyJ9"
)

# --- CONTEÚDO TÉCNICO ---
st.subheader("💡 Conteúdo Técnico")
st.markdown(
    '<a href="https://www.linkedin.com/feed/update/urn:li:activity:7287584764490891266" target="_blank" class="pbi-button">'
    '☑️ A Revolução das Medidas DAX no Power BI (Artigo no LinkedIn)'
    '</a>', 
    unsafe_allow_html=True
)

st.markdown("---")