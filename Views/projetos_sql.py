import streamlit as st
import json
from datetime import datetime, timedelta
import pandas as pd
import sqlite3
from io import StringIO

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="SQL - Melhores Práticas Pro | Rodrigo Aiosa",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- INICIALIZAR SESSION STATE ---
if 'favorites' not in st.session_state:
    st.session_state.favorites = set()
if 'learned' not in st.session_state:
    st.session_state.learned = set()
if 'notes' not in st.session_state:
    st.session_state.notes = {}
if 'search_query' not in st.session_state:
    st.session_state.search_query = ""
if 'user_points' not in st.session_state:
    st.session_state.user_points = 0
if 'challenges_completed' not in st.session_state:
    st.session_state.challenges_completed = set()
if 'daily_streak' not in st.session_state:
    st.session_state.daily_streak = 1
if 'current_menu' not in st.session_state:
    st.session_state.current_menu = "📖 Todas as Práticas"
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "Todas"
if 'selected_difficulty' not in st.session_state:
    st.session_state.selected_difficulty = "Todas"

# --- INICIALIZAR DATABASE EM MEMÓRIA ---
@st.cache_resource
def init_database():
    """Inicializa banco de dados SQLite em memória com dados de exemplo"""
    conn = sqlite3.connect(':memory:')
    
    # Criar tabela usuarios
    usuarios_df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'nome': ['Alice Silva', 'Bob Santos', 'Carlos Oliveira', 'Diana Costa', 'Eduardo Pereira'],
        'email': ['alice@gmail.com', 'bob@gmail.com', 'carlos@hotmail.com', 'diana@gmail.com', 'edu@outlook.com'],
        'ativo': [True, True, False, True, True],
        'created_at': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-12'],
        'categoria': ['Premium', 'Standard', 'Premium', 'Free', 'Standard']
    })
    usuarios_df.to_sql('usuarios', conn, index=False, if_exists='replace')
    
    # Criar tabela vendas
    vendas_df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5, 6],
        'usuario_id': [1, 2, 1, 3, 2, 5],
        'valor': [150.00, 200.00, 75.50, 300.00, 120.00, 450.00],
        'status': ['pago', 'pago', 'pendente', 'pago', 'cancelado', 'pago'],
        'data': ['2024-01-10', '2024-01-15', '2024-02-01', '2024-02-10', '2024-02-15', '2024-03-01']
    })
    vendas_df.to_sql('vendas', conn, index=False, if_exists='replace')
    
    # Criar tabela produtos
    produtos_df = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
        'categoria': ['Eletrônicos', 'Eletrônicos', 'Livros', 'Livros'],
        'preco': [99.99, 199.99, 29.99, 49.99]
    })
    produtos_df.to_sql('produtos', conn, index=False, if_exists='replace')
    
    return conn

def execute_query(query, conn):
    """Executa query SQL e retorna resultado como DataFrame"""
    try:
        # Limpar a query
        query = query.strip()
        if not query:
            return None, "❌ Escreva uma query SQL primeiro!"
        
        # Executar query
        df = pd.read_sql_query(query, conn)
        return df, f"✅ Query executada com sucesso! {len(df)} registros retornados."
    
    except sqlite3.OperationalError as e:
        return None, f"❌ Erro SQL: {str(e)}"
    except Exception as e:
        return None, f"❌ Erro: {str(e)}"

# --- CUSTOM CSS - Design Profissional com Autoridade ---
st.markdown("""
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    :root {
        --primary: #0F172A;
        --secondary: #1E293B;
        --accent: #D4AF37;
        --text-light: #E2E8F0;
        --text-dark: #0F172A;
        --border: #334155;
    }
    
    body {
        background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%);
        color: var(--text-light);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%);
    }
    
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%);
    }
    
    /* Header Hero */
    .hero-section {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-bottom: 2px solid var(--accent);
        padding: 60px 0;
        margin-bottom: 50px;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -10%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(212, 175, 55, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: var(--text-light);
        margin-bottom: 15px;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: var(--accent);
        margin-bottom: 30px;
        font-weight: 500;
        position: relative;
        z-index: 1;
    }
    
    .hero-description {
        font-size: 1.1rem;
        color: #cbd5e1;
        line-height: 1.6;
        max-width: 600px;
        position: relative;
        z-index: 1;
    }
    
    /* Stats Cards */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 25px;
        margin: 60px 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 40px;
        text-align: center;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        border-color: var(--accent);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.15);
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--accent), transparent);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .stat-card:hover::before {
        opacity: 1;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        color: var(--accent);
        margin-bottom: 10px;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #cbd5e1;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stat-sublabel {
        font-size: 0.85rem;
        color: #94a3b8;
        margin-top: 8px;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--text-light);
        margin: 60px 0 40px 0;
        padding-bottom: 20px;
        border-bottom: 2px solid var(--accent);
        position: relative;
    }
    
    .section-header::before {
        content: '';
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 60px;
        height: 3px;
        background: var(--accent);
    }
    
    /* Expander Cards */
    .stExpander {
        background-color: #1E293B !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
    }
    
    .stExpander > div {
        border-color: var(--border) !important;
    }
    
    .stExpander [data-testid="stExpanderToggleButton"] {
        color: var(--accent) !important;
        font-weight: 600;
    }
    
    /* Code Blocks */
    .stCode {
        background-color: #0F172A !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
    }
    
    code {
        color: #60a5fa !important;
        background: transparent !important;
    }
    
    /* Info/Warning Boxes */
    .stInfo {
        background-color: rgba(212, 175, 55, 0.1) !important;
        border: 1px solid var(--accent) !important;
        border-radius: 8px !important;
        padding: 20px !important;
    }
    
    .stSuccess {
        background-color: rgba(34, 197, 94, 0.1) !important;
        border: 1px solid #22c55e !important;
        border-radius: 8px !important;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid #ef4444 !important;
        border-radius: 8px !important;
    }
    
    /* Divider */
    hr {
        border-color: var(--border) !important;
        margin: 50px 0 !important;
    }
    
    /* Selectbox & Input */
    .stSelectbox > div > div {
        background-color: #1E293B !important;
        border: 1px solid var(--border) !important;
        color: var(--text-light) !important;
    }
    
    .stTextArea > div > div {
        background-color: #1E293B !important;
        border: 1px solid var(--border) !important;
        color: var(--text-light) !important;
    }
    
    /* Filter Section */
    .filter-section {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 30px;
        margin: 40px 0;
    }
    
    /* Editor Section */
    .editor-section {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 30px;
        margin: 40px 0;
    }
    
    .editor-title {
        font-size: 1.5rem;
        color: var(--accent);
        font-weight: 600;
        margin-bottom: 20px;
    }
    
    /* Challenges Section */
    .challenges-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        margin: 40px 0;
    }
    
    /* Metrics */
    .metric-box {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 20px;
        text-align: center;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--accent);
    }
    
    .metric-label {
        color: #cbd5e1;
        font-weight: 600;
        margin-top: 10px;
    }
    
    /* Hover Effects */
    a {
        color: var(--accent) !important;
        transition: all 0.3s ease;
    }
    
    a:hover {
        text-decoration: underline;
        filter: brightness(1.2);
    }
    
    /* Footer */
    footer {
        border-top: 1px solid var(--border);
        padding-top: 40px;
        margin-top: 60px;
    }
    
    /* Favorites & Notes */
    .favorite-btn {
        display: inline-block;
        cursor: pointer;
        font-size: 1.2rem;
        transition: all 0.2s;
    }
    
    .favorite-btn:hover {
        transform: scale(1.2);
    }
    
    /* Search Box */
    .search-container {
        margin-bottom: 20px;
    }
    
    /* Progress Bar */
    .progress-container {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 20px;
        margin: 20px 0;
    }
    
    .progress-bar {
        width: 100%;
        height: 10px;
        background: var(--border);
        border-radius: 5px;
        overflow: hidden;
        margin: 10px 0;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--accent), #60a5fa);
        transition: width 0.3s ease;
    }
    
    /* Gamification */
    .points-badge {
        background: linear-gradient(135deg, var(--accent), #fbbf24);
        color: var(--text-dark);
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        display: inline-block;
        margin: 5px;
    }
    
    .streak-badge {
        background: linear-gradient(135deg, #ef4444, #dc2626);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        display: inline-block;
        margin: 5px;
    }
    
    /* Notes */
    .notes-container {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        border-left: 4px solid var(--accent);
    }
    
    /* Badges */
    .badge {
        display: inline-block;
        background: var(--accent);
        color: var(--text-dark);
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 3px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("""
<div style="text-align: center; padding: 20px 0; border-bottom: 2px solid var(--accent);">
    <h1 style="font-size: 1.8rem; color: var(--accent); margin: 0;">📊 SQL Pro</h1>
    <p style="color: #cbd5e1; font-size: 0.9rem; margin-top: 5px;">Domine SQL em 60 práticas</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR STATS ---
col1, col2 = st.sidebar.columns(2)
with col1:
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 8px; padding: 15px; text-align: center;">
        <p style="color: var(--accent); font-weight: 700; font-size: 1.5rem; margin: 0;">⭐ {st.session_state.user_points}</p>
        <p style="color: #cbd5e1; font-size: 0.8rem; margin: 5px 0;">Pontos</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 8px; padding: 15px; text-align: center;">
        <p style="color: var(--accent); font-weight: 700; font-size: 1.5rem; margin: 0;">🔥 {st.session_state.daily_streak}</p>
        <p style="color: #cbd5e1; font-size: 0.8rem; margin: 5px 0;">Streak</p>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR MENU ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Navegação")

menu = st.sidebar.radio(
    "Escolha uma seção:",
    ["📖 Todas as Práticas", "⭐ Meus Favoritos", "✅ Já Aprendi", "🏆 Progresso", "🎯 Desafios"],
    label_visibility="collapsed"
)

# --- SEARCH FUNCTIONALITY ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Buscar")
search_query = st.sidebar.text_input(
    "Buscar práticas:",
    placeholder="Digite aqui...",
    label_visibility="collapsed"
)
st.session_state.search_query = search_query.lower()

# --- ARMAZENAR MENU SELECIONADO ---
st.session_state.current_menu = menu

st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">🗄️ SQL - Melhores Práticas</h1>
    <p class="hero-subtitle">Domine SQL Estratégico</p>
    <p class="hero-description">
        Estratégias avançadas para queries eficientes, escaláveis e precisas. 
        Transforme seus dados em vantagem competitiva com 60+ práticas documentadas.
    </p>
</div>
""", unsafe_allow_html=True)

# --- PROGRESSO VISUAL (SEMPRE VISÍVEL) ---
total_practices = 60
learned_count = len(st.session_state.learned)
progress_percent = (learned_count / total_practices) * 100

st.markdown(f"""
<div class="progress-container">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
        <p style="color: #cbd5e1; font-weight: 600; margin: 0;">🎓 Seu Progresso</p>
        <p style="color: var(--accent); font-weight: 700; margin: 0;">{learned_count}/{total_practices}</p>
    </div>
    <div class="progress-bar">
        <div class="progress-fill" style="width: {progress_percent}%"></div>
    </div>
    <p style="color: #94a3b8; font-size: 0.85rem; margin: 10px 0;">
        {'🏆 Parabéns! Você completou todas as práticas!' if learned_count == total_practices else f'Continue! Faltam {total_practices - learned_count} práticas'}
    </p>
</div>
""", unsafe_allow_html=True)

# --- STATS SECTION ---
st.markdown('<h2 class="section-header">📊 Números que Falam</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">60+</div>
        <div class="stat-label">Práticas SQL</div>
        <div class="stat-sublabel">Documentadas e Testadas</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">5</div>
        <div class="stat-label">Categorias</div>
        <div class="stat-sublabel">De Conhecimento Essencial</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">3</div>
        <div class="stat-label">Níveis</div>
        <div class="stat-sublabel">Iniciante, Intermediário, Avançado</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<p style="text-align: center; color: #cbd5e1; margin: 40px 0; font-size: 1.1rem; line-height: 1.8;">
    Queries eficientes são a base de dashboards que escalam. 
    Boas práticas em SQL reduzem tempo de processamento e amplificam a precisão das análises.
    <br><br>
    <span style="color: var(--accent); font-weight: 600;">
    Este é um guia completo para transformar você em um especialista SQL.
    </span>
</p>
""", unsafe_allow_html=True)

st.divider()

# --- DATABASE DE PRÁTICAS SQL ---
sql_practices = [
    # INICIANTE (20+)
    {
        "icon": "🔍",
        "title": "Evitar SELECT *",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Selecione apenas as colunas necessárias.",
        "bad_query": "SELECT * FROM vendas WHERE ano = 2024;",
        "good_query": "SELECT\n    id,\n    produto,\n    valor,\n    data_venda\nFROM vendas\nWHERE ano = 2024;",
        "benefit": "Reduz bandwidth de rede, acelera processamento.",
        "context": "Impacto exponencial em sistemas com muitos dados.",
        "explanation": "Especificar colunas reduz o volume de dados trafegado pela rede e melhora o índice utilizado pelo banco de dados."
    },
    {
        "icon": "✅",
        "title": "Tratar NULL Explicitamente",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "NULL não é zero nem string vazia.",
        "bad_query": "SELECT SUM(comissao) FROM vendas WHERE status = 'concluida';",
        "good_query": "SELECT\n    SUM(COALESCE(comissao, 0)) AS total_comissao\nFROM vendas\nWHERE status = 'concluida'\n    AND comissao IS NOT NULL;",
        "benefit": "Evita resultados inesperados.",
        "context": "Crítico em cálculos financeiros.",
        "explanation": "COALESCE substitui NULLs por um valor padrão, evitando que a soma resulte em NULL quando há valores nulos na coluna."
    },
    {
        "icon": "🔐",
        "title": "Prepared Statements",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Parameterize queries contra SQL Injection.",
        "bad_query": "query = f\"SELECT * FROM usuarios WHERE email = '{user_email}'\"",
        "good_query": "query = (\n    \"SELECT *\"\n    \"FROM usuarios\"\n    \"WHERE email = %s\"\n)\ncursor.execute(query, (user_email,))",
        "benefit": "Impede ataques de segurança.",
        "context": "Obrigatório em produção.",
        "explanation": "Usar placeholders (%) em vez de concatenação protege contra SQL Injection, pois os parâmetros são tratados como dados, não como código SQL."
    },
    {
        "icon": "📋",
        "title": "Documentar Queries",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Comente queries complexas.",
        "bad_query": "SELECT u.id, COUNT(DISTINCT v.id) FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id GROUP BY u.id;",
        "good_query": "-- Query: Contagem de vendas por usuário\n-- Propósito: Dashboard de Engagement\nSELECT\n    u.id,\n    u.nome,\n    COUNT(DISTINCT v.id) AS total_vendas\nFROM usuarios u\nLEFT JOIN vendas v\n    ON u.id = v.usuario_id\nGROUP BY u.id, u.nome;",
        "benefit": "Fácil handoff e manutenção.",
        "context": "Um comentário economiza horas.",
        "explanation": "Comentários explicam o objetivo da query e facilitam manutenção futura, especialmente em equipes com múltiplos desenvolvedores."
    },
    {
        "icon": "🎓",
        "title": "Usar LIMIT em Development",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Sempre limitar resultados em queries de teste.",
        "bad_query": "SELECT * FROM usuarios;",
        "good_query": "SELECT *\nFROM usuarios\nLIMIT 100;",
        "benefit": "Evita lentidão ao testar em prod.",
        "context": "Development vs Production.",
        "explanation": "LIMIT reduz o tempo de execução durante testes e evita carregar dados desnecessários em memória, protegendo também a produção de queries descontroladas."
    },
]

# --- FILTROS SECTION ---
st.markdown('<h2 class="section-header">🔎 Filtrar Práticas</h2>', unsafe_allow_html=True)

st.markdown('<div class="filter-section">', unsafe_allow_html=True)

col1, col2, col_space = st.columns([1.5, 1.5, 1])

with col1:
    categorias = ["Todas"] + sorted(list(set([p["category"] for p in sql_practices])))
    selected_category = st.selectbox("📂 Categoria", categorias, key="category_filter")

with col2:
    dificuldades = ["Todas", "Iniciante", "Intermediário", "Avançado"]
    selected_difficulty = st.selectbox("📈 Nível de Dificuldade", dificuldades, key="difficulty_filter")

st.markdown('</div>', unsafe_allow_html=True)

# --- SEÇÃO EDITOR SQL COM BANCO REAL ---
st.markdown('<h2 class="section-header">✏️ Editor SQL Interativo</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #cbd5e1; margin-bottom: 30px;">Teste suas queries SQL em tempo real. O banco contém as tabelas: usuarios, vendas e produtos.</p>', unsafe_allow_html=True)

# Inicializar conexão
conn = init_database()

# --- EXEMPLOS PRÉ-DEFINIDOS ---
sql_templates = {
    "SELECT Básico": "SELECT * FROM produtos LIMIT 10;",
    "WHERE Filtro": "SELECT id, nome, categoria FROM produtos WHERE categoria = 'Livros';",
    "COUNT Agregação": "SELECT COUNT(*) AS total_produtos FROM produtos;",
    "GROUP BY": "SELECT categoria, COUNT(*) AS total FROM produtos GROUP BY categoria;",
    "JOIN Tabelas": "SELECT u.nome, v.valor FROM usuarios u INNER JOIN vendas v ON u.id = v.usuario_id LIMIT 5;",
    "ORDER BY": "SELECT id, nome FROM usuarios ORDER BY nome ASC;",
    "SUM com Agregação": "SELECT usuario_id, SUM(valor) AS total_valor FROM vendas GROUP BY usuario_id;",
    "LEFT JOIN": "SELECT u.id, u.nome, COUNT(v.id) AS total_vendas FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id GROUP BY u.id, u.nome;",
    "DISTINCT": "SELECT DISTINCT categoria FROM produtos ORDER BY categoria;",
    "BETWEEN": "SELECT * FROM vendas WHERE valor BETWEEN 100 AND 300;",
    "IN Clause": "SELECT * FROM usuarios WHERE id IN (1, 2, 3, 4, 5);",
    "LIKE Pattern": "SELECT * FROM usuarios WHERE nome LIKE '%Silva%';",
}

st.markdown('<div class="editor-section">', unsafe_allow_html=True)

# --- LAYOUT ---
col_template, col_editor = st.columns([1, 2], gap="large")

with col_template:
    st.markdown('<p class="editor-title">📚 Templates</p>', unsafe_allow_html=True)
    selected_template = st.selectbox(
        "Escolha um exemplo:",
        ["Escrever Manual"] + list(sql_templates.keys()),
        key="template_select",
        label_visibility="collapsed"
    )
    
    if selected_template != "Escrever Manual":
        template_query = sql_templates[selected_template]
    else:
        template_query = ""

with col_editor:
    st.markdown('<p class="editor-title">📝 Seu SQL</p>', unsafe_allow_html=True)
    user_query = st.text_area(
        "Escreva sua query SQL:",
        value=template_query,
        height=150,
        key="sql_editor",
        placeholder="SELECT * FROM produtos;",
        label_visibility="collapsed"
    )

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- SEÇÃO DE RESULTADO COM EXECUTOR REAL ---
st.markdown('<h2 class="section-header">📊 Resultado da Query</h2>', unsafe_allow_html=True)

col_result, col_info = st.columns([2, 1], gap="large")

with col_result:
    st.markdown('<div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 8px; padding: 20px;">', unsafe_allow_html=True)
    
    if user_query.strip():
        # Executar query com banco real
        result_df, message = execute_query(user_query, conn)
        
        # Exibir mensagem de status
        if "✅" in message:
            st.success(message)
            if result_df is not None and len(result_df) > 0:
                st.dataframe(result_df, use_container_width=True)
            else:
                st.info("Query executada, mas nenhum resultado foi retornado.")
        else:
            st.error(message)
    else:
        st.markdown("""
        <div style="text-align: center; padding: 40px; color: #94a3b8;">
            <p style="font-size: 1rem;">📝 Escreva uma query SQL no editor para ver o resultado</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col_info:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 1px solid var(--border); border-radius: 8px; padding: 20px;">
        <p style="color: var(--accent); font-weight: 600; margin-bottom: 15px; font-size: 1rem;">ℹ️ Tabelas & Dicas</p>
        <p style="color: #cbd5e1; font-size: 0.85rem; line-height: 1.6; margin-bottom: 15px;">
            <strong>usuarios:</strong> id, nome, email, ativo, created_at, categoria
            <br><br>
            <strong>vendas:</strong> id, usuario_id, valor, status, data
            <br><br>
            <strong>produtos:</strong> id, nome, categoria, preco
        </p>
        <p style="color: #cbd5e1; font-size: 0.85rem; font-style: italic; border-top: 1px solid var(--border); padding-top: 15px;">
            💡 Teste SELECT, WHERE, JOIN, GROUP BY, LIMIT e mais!
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 40px 0; border-top: 1px solid var(--border); color: #cbd5e1;">
    <p style="margin-bottom: 10px; font-size: 0.95rem;">
        <span style="color: var(--accent); font-weight: 600;">SQL - Melhores Práticas</span> 
        • Criado por Rodrigo Aiosa
    </p>
    <p style="font-size: 0.85rem; color: #94a3b8;">
        Transforme seus dados em vantagem competitiva com SQL estratégico
    </p>
</div>
""", unsafe_allow_html=True)
