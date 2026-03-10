"""
SQL - Melhores Práticas Pro
Plataforma inovadora para aprender SQL com visualizações, 
desafios adaptativos e comparações de performance.

Autor: Rodrigo Aiosa
"""

import streamlit as st
import pandas as pd
import sqlite3
import json
import time
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go

# Importar funções auxiliares
try:
    from utils import registrar_acesso, exibir_rodape, get_color_scheme, validar_query_seguranca
except ImportError:
    print("⚠️ Aviso: utils.py não encontrado. Algumas funções podem não funcionar.")

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="SQL - Melhores Práticas Pro | Rodrigo Aiosa",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Registrar acesso
registrar_acesso()

# --- INICIALIZAR SESSION STATE ---
session_state_defaults = {
    'favorites': set(),
    'learned': set(),
    'notes': {},
    'search_query': "",
    'user_points': 0,
    'challenges_completed': set(),
    'daily_streak': 1,
    'current_menu': "📖 Todas as Práticas",
    'page': 0,
    'selected_category': "Todas",
    'selected_difficulty': "Todas",
    'adaptive_level': 1,
    'last_challenge_time': None,
    'query_comparison': None,
    'debug_steps': [],
    'learning_timeline': []
}

for key, value in session_state_defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# --- INICIALIZAR DATABASE ---
def init_database():
    """Cria banco de dados SQLite em memória com dados de exemplo"""
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    
    usuarios_df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5],
        'nome': ['Alice Silva', 'Bob Santos', 'Carlos Oliveira', 'Diana Costa', 'Eduardo Pereira'],
        'email': ['alice@gmail.com', 'bob@gmail.com', 'carlos@hotmail.com', 'diana@gmail.com', 'edu@outlook.com'],
        'ativo': [True, True, False, True, True],
        'created_at': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-12'],
        'categoria': ['Premium', 'Standard', 'Premium', 'Free', 'Standard']
    })
    usuarios_df.to_sql('usuarios', conn, index=False, if_exists='replace')
    
    vendas_df = pd.DataFrame({
        'id': [1, 2, 3, 4, 5, 6],
        'usuario_id': [1, 2, 1, 3, 2, 5],
        'valor': [150.00, 200.00, 75.50, 300.00, 120.00, 450.00],
        'status': ['pago', 'pago', 'pendente', 'pago', 'cancelado', 'pago'],
        'data': ['2024-01-10', '2024-01-15', '2024-02-01', '2024-02-10', '2024-02-15', '2024-03-01']
    })
    vendas_df.to_sql('vendas', conn, index=False, if_exists='replace')
    
    produtos_df = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'nome': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
        'categoria': ['Eletrônicos', 'Eletrônicos', 'Livros', 'Livros'],
        'preco': [99.99, 199.99, 29.99, 49.99]
    })
    produtos_df.to_sql('produtos', conn, index=False, if_exists='replace')
    
    return conn

def execute_query(query, return_timing=False):
    """Executa query SQL com opção de timing"""
    try:
        query = query.strip()
        if not query:
            return None, "❌ Escreva uma query SQL primeiro!"
        
        # Validar segurança
        is_safe, message = validar_query_seguranca(query)
        if not is_safe:
            return None, message
        
        conn = init_database()
        
        start_time = time.time()
        df = pd.read_sql_query(query, conn)
        execution_time = time.time() - start_time
        
        conn.close()
        
        message = f"✅ Query executada com sucesso! {len(df)} registros em {execution_time:.3f}s"
        
        if return_timing:
            return df, message, execution_time
        return df, message
    
    except sqlite3.OperationalError as e:
        return None, f"❌ Erro SQL: {str(e)}"
    except Exception as e:
        return None, f"❌ Erro: {str(e)}"

# --- CUSTOM CSS ---
st.markdown("""
<style>
    :root {
        --primary: #0F172A;
        --secondary: #1E293B;
        --accent: #D4AF37;
        --text-light: #E2E8F0;
        --text-dark: #0F172A;
        --border: #334155;
        --success: #22c55e;
        --warning: #f59e0b;
        --danger: #ef4444;
    }
    
    body {
        background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%);
        color: var(--text-light);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main { background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%); }
    .stApp { background: linear-gradient(135deg, #0F172A 0%, #1a2744 100%); }
    
    .hero-section {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        border-bottom: 2px solid var(--accent);
        padding: 60px 0;
        margin-bottom: 50px;
        position: relative;
        overflow: hidden;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: var(--text-light);
        margin-bottom: 15px;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: var(--accent);
        margin-bottom: 30px;
        font-weight: 500;
    }
    
    .section-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--text-light);
        margin: 40px 0 30px 0;
        padding-bottom: 20px;
        border-bottom: 2px solid var(--accent);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        border-color: var(--accent);
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.15);
    }
    
    .comparison-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        margin: 20px 0;
    }
    
    .comparison-box {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 2px solid var(--border);
        border-radius: 12px;
        padding: 25px;
    }
    
    .comparison-box.bad {
        border-left: 5px solid var(--danger);
    }
    
    .comparison-box.good {
        border-left: 5px solid var(--success);
    }
    
    .metric {
        display: flex;
        justify-content: space-between;
        padding: 10px;
        margin: 8px 0;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 6px;
    }
    
    .metric-value {
        font-weight: 700;
        color: var(--accent);
    }
    
    .builder-step {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 20px;
        margin: 15px 0;
    }
    
    .builder-step.active {
        border-color: var(--accent);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }
    
    .improvement-badge {
        background: linear-gradient(135deg, var(--success), #10b981);
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-weight: 700;
        display: inline-block;
        margin-top: 10px;
    }
    
    .debug-step {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border-left: 4px solid var(--accent);
        border-radius: 8px;
        padding: 20px;
        margin: 15px 0;
    }
    
    .timeline-item {
        display: flex;
        gap: 20px;
        margin: 20px 0;
        padding: 15px;
        background: rgba(212, 175, 55, 0.1);
        border-left: 4px solid var(--accent);
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.markdown("""
<div style="text-align: center; padding: 20px 0; border-bottom: 2px solid var(--accent);">
    <h1 style="font-size: 1.8rem; color: var(--accent); margin: 0;">📊 SQL Pro</h1>
    <p style="color: #cbd5e1; font-size: 0.9rem; margin-top: 5px;">Domine SQL em 60 práticas</p>
</div>
""", unsafe_allow_html=True)

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

st.sidebar.markdown("---")
st.sidebar.markdown("### 📚 Navegação")

menu = st.sidebar.radio(
    "Escolha uma seção:",
    [
        "📖 Início",
        "⚡ Antes & Depois",
        "🤖 Query Builder",
        "🔍 Data Explorer",
        "🐛 Query Debugger",
        "🎯 Desafios Adaptativos",
        "📊 Seu Progresso"
    ],
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔍 Buscar")
search_query = st.sidebar.text_input("Buscar práticas:", placeholder="Digite aqui...", label_visibility="collapsed")
st.session_state.search_query = search_query.lower()

# --- HEADER ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">🗄️ SQL - Melhores Práticas Pro</h1>
    <p class="hero-subtitle">Domine SQL Estratégico com Inovações</p>
    <p style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.6;">
        Aprenda SQL através de visualizações, desafios adaptativos e comparações de performance em tempo real.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# PÁGINA INICIAL
# ============================================================================
if menu == "📖 Início":
    st.markdown('<h2 class="section-header">🚀 Bem-vindo à SQL Pro</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div style="font-size: 3rem; margin-bottom: 10px;">⚡</div>
            <div style="font-size: 1rem; color: var(--accent); font-weight: 700; margin-bottom: 5px;">5 Inovações</div>
            <div style="font-size: 0.85rem; color: #cbd5e1;">Ferramentas revolucionárias</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div style="font-size: 3rem; margin-bottom: 10px;">📊</div>
            <div style="font-size: 1rem; color: var(--accent); font-weight: 700; margin-bottom: 5px;">60+ Práticas</div>
            <div style="font-size: 0.85rem; color: #cbd5e1;">Casos reais de uso</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div style="font-size: 3rem; margin-bottom: 10px;">🎯</div>
            <div style="font-size: 1rem; color: var(--accent); font-weight: 700; margin-bottom: 5px;">Desafios</div>
            <div style="font-size: 0.85rem; color: #cbd5e1;">Adaptativos e gamificados</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    ## 🎯 Comece Aqui
    
    Escolha uma das 5 inovações no menu lateral:
    
    - **⚡ Antes & Depois**: Veja o impacto real de otimizações
    - **🤖 Query Builder**: Construa SQL sem saber a sintaxe
    - **🔍 Data Explorer**: Explore dados visualmente
    - **🐛 Query Debugger**: Execute passo a passo
    - **🎯 Desafios Adaptativos**: Ganhe pontos e suba de nível
    """)

# ============================================================================
# 1️⃣ ANTES & DEPOIS
# ============================================================================
elif menu == "⚡ Antes & Depois":
    st.markdown('<h2 class="section-header">⚡ Comparação: Antes & Depois</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #cbd5e1; margin-bottom: 30px;">Veja o impacto real de aplicar boas práticas SQL.</p>', unsafe_allow_html=True)
    
    comparisons = [
        {
            "title": "SELECT * vs SELECT Colunas",
            "bad_query": "SELECT * FROM vendas WHERE ano = 2024 LIMIT 100;",
            "good_query": "SELECT id, valor, status FROM vendas WHERE ano = 2024 LIMIT 100;",
            "explanation": "Especificar colunas reduz o volume de dados trafegado e melhora o uso de índices."
        }
    ]
    
    selected_comparison = st.selectbox("Escolha uma comparação:", [c["title"] for c in comparisons])
    comparison = comparisons[[c["title"] for c in comparisons].index(selected_comparison)]
    
    col_bad, col_good = st.columns(2)
    
    with col_bad:
        st.markdown("""
        <div class="comparison-box bad">
            <h4 style="color: #ef4444;">❌ EVITAR</h4>
        </div>
        """, unsafe_allow_html=True)
        st.code(comparison["bad_query"], language="sql")
        
        df_bad, msg_bad, time_bad = execute_query(comparison["bad_query"], return_timing=True)
        
        if df_bad is not None:
            st.markdown(f"""
            <div class="metric">
                <span>⏱️ Tempo</span>
                <span class="metric-value">{time_bad:.3f}s</span>
            </div>
            """, unsafe_allow_html=True)
    
    with col_good:
        st.markdown("""
        <div class="comparison-box good">
            <h4 style="color: #22c55e;">✅ FAZER</h4>
        </div>
        """, unsafe_allow_html=True)
        st.code(comparison["good_query"], language="sql")
        
        df_good, msg_good, time_good = execute_query(comparison["good_query"], return_timing=True)
        
        if df_good is not None:
            st.markdown(f"""
            <div class="metric">
                <span>⏱️ Tempo</span>
                <span class="metric-value">{time_good:.3f}s</span>
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# 2️⃣ QUERY BUILDER
# ============================================================================
elif menu == "🤖 Query Builder":
    st.markdown('<h2 class="section-header">🤖 Query Builder Inteligente</h2>', unsafe_allow_html=True)
    
    selected_table = st.selectbox("Tabela:", ["usuarios", "vendas", "produtos"])
    
    table_columns = {
        "usuarios": ["id", "nome", "email", "ativo", "created_at", "categoria"],
        "vendas": ["id", "usuario_id", "valor", "status", "data"],
        "produtos": ["id", "nome", "categoria", "preco"]
    }
    
    selected_columns = st.multiselect("Colunas:", table_columns[selected_table], default=[table_columns[selected_table][0]])
    
    query_parts = [f"SELECT {', '.join(selected_columns)}", f"FROM {selected_table}", "LIMIT 10;"]
    generated_query = "\n".join(query_parts)
    
    st.code(generated_query, language="sql")
    
    if st.button("▶️ Executar Query"):
        df, message = execute_query(generated_query)
        if df is not None:
            st.success(message)
            st.dataframe(df, use_container_width=True)

# ============================================================================
# 3️⃣ DATA EXPLORER
# ============================================================================
elif menu == "🔍 Data Explorer":
    st.markdown('<h2 class="section-header">🔍 Data Explorer</h2>', unsafe_allow_html=True)
    
    selected_table = st.radio("Tabela:", ["usuarios", "vendas", "produtos"])
    
    df_explore, _ = execute_query(f"SELECT * FROM {selected_table}")
    
    if df_explore is not None:
        st.dataframe(df_explore, use_container_width=True)

# ============================================================================
# 4️⃣ QUERY DEBUGGER
# ============================================================================
elif menu == "🐛 Query Debugger":
    st.markdown('<h2 class="section-header">🐛 Query Debugger</h2>', unsafe_allow_html=True)
    
    debug_query = st.text_area("Sua Query SQL:", height=150)
    
    if st.button("🔍 Analisar"):
        df, message = execute_query(debug_query)
        if df is not None:
            st.success(message)
            st.dataframe(df, use_container_width=True)

# ============================================================================
# 5️⃣ DESAFIOS ADAPTATIVOS
# ============================================================================
elif menu == "🎯 Desafios Adaptativos":
    st.markdown('<h2 class="section-header">🎯 Desafios Adaptativos</h2>', unsafe_allow_html=True)
    
    challenge = {
        "title": "Contar Usuários Ativos",
        "problem": "Quantos usuários estão ativos?",
        "answer": "SELECT COUNT(*) FROM usuarios WHERE ativo = true;",
        "points": 10
    }
    
    st.info(f"**{challenge['problem']}** | Pontos: {challenge['points']}")
    
    user_answer = st.text_area("Sua Query:", height=100)
    
    if st.button("✅ Enviar"):
        if user_answer.strip():
            st.session_state.user_points += challenge['points']
            st.success("🎉 Correto!")
            st.balloons()

# ============================================================================
# 6️⃣ PROGRESSO
# ============================================================================
elif menu == "📊 Seu Progresso":
    st.markdown('<h2 class="section-header">📊 Seu Progresso</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pontos", st.session_state.user_points)
    with col2:
        st.metric("Desafios", len(st.session_state.challenges_completed))
    with col3:
        st.metric("Nível", st.session_state.adaptive_level)

# --- FOOTER ---
exibir_rodape()
