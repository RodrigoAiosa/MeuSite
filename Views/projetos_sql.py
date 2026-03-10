import streamlit as st
import pandas as pd
import sqlite3
import json
import time
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="SQL - Melhores Práticas Pro | Rodrigo Aiosa",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
        "📖 Todas as Práticas",
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
# 1️⃣ ANTES & DEPOIS - COMPARAÇÃO VISUAL
# ============================================================================
if menu == "⚡ Antes & Depois":
    st.markdown('<h2 class="section-header">⚡ Comparação: Antes & Depois</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #cbd5e1; margin-bottom: 30px;">Veja o impacto real de aplicar boas práticas SQL em tempo real.</p>', unsafe_allow_html=True)
    
    # Exemplos de comparação
    comparisons = [
        {
            "title": "SELECT * vs SELECT Colunas",
            "bad_query": "SELECT * FROM vendas WHERE ano = 2024 LIMIT 100;",
            "good_query": "SELECT id, valor, status FROM vendas WHERE ano = 2024 LIMIT 100;",
            "explanation": "Especificar colunas reduz o volume de dados trafegado e melhora o uso de índices."
        },
        {
            "title": "NULL em Agregações",
            "bad_query": "SELECT SUM(desconto) FROM vendas;",
            "good_query": "SELECT SUM(COALESCE(desconto, 0)) FROM vendas;",
            "explanation": "COALESCE evita que NULL propague pela agregação, retornando 0 em vez de NULL."
        },
        {
            "title": "JOIN sem WHERE vs com WHERE",
            "bad_query": "SELECT * FROM usuarios u JOIN vendas v ON u.id = v.usuario_id;",
            "good_query": "SELECT u.id, u.nome, SUM(v.valor) FROM usuarios u JOIN vendas v ON u.id = v.usuario_id WHERE v.status = 'pago' GROUP BY u.id;",
            "explanation": "Filtrar antes de aggregar reduz número de linhas processadas."
        }
    ]
    
    selected_comparison = st.selectbox("Escolha uma comparação:", [c["title"] for c in comparisons])
    comparison = comparisons[[c["title"] for c in comparisons].index(selected_comparison)]
    
    st.markdown(f"<h3 style='color: var(--accent); margin-top: 30px;'>{comparison['title']}</h3>", unsafe_allow_html=True)
    
    col_bad, col_good = st.columns(2)
    
    with col_bad:
        st.markdown("""
        <div class="comparison-box bad">
            <h4 style="color: var(--danger);">❌ EVITAR</h4>
        </div>
        """, unsafe_allow_html=True)
        st.code(comparison["bad_query"], language="sql")
        
        # Executar query ruim
        df_bad, msg_bad, time_bad = execute_query(comparison["bad_query"], return_timing=True)
        
        if df_bad is not None:
            st.markdown(f"""
            <div class="metric">
                <span>⏱️ Tempo</span>
                <span class="metric-value">{time_bad:.3f}s</span>
            </div>
            <div class="metric">
                <span>📊 Registros</span>
                <span class="metric-value">{len(df_bad)}</span>
            </div>
            <div class="metric">
                <span>💾 Memória Est.</span>
                <span class="metric-value">{len(df_bad) * len(df_bad.columns) * 20} bytes</span>
            </div>
            """, unsafe_allow_html=True)
    
    with col_good:
        st.markdown("""
        <div class="comparison-box good">
            <h4 style="color: var(--success);">✅ FAZER</h4>
        </div>
        """, unsafe_allow_html=True)
        st.code(comparison["good_query"], language="sql")
        
        # Executar query boa
        df_good, msg_good, time_good = execute_query(comparison["good_query"], return_timing=True)
        
        if df_good is not None:
            improvement_time = ((time_bad - time_good) / time_bad * 100) if time_bad > 0 else 0
            improvement_memory = ((len(df_bad) * len(df_bad.columns) - len(df_good) * len(df_good.columns)) / (len(df_bad) * len(df_bad.columns)) * 100) if len(df_bad) * len(df_bad.columns) > 0 else 0
            
            st.markdown(f"""
            <div class="metric">
                <span>⏱️ Tempo</span>
                <span class="metric-value">{time_good:.3f}s</span>
            </div>
            <div class="metric">
                <span>📊 Registros</span>
                <span class="metric-value">{len(df_good)}</span>
            </div>
            <div class="metric">
                <span>💾 Memória Est.</span>
                <span class="metric-value">{len(df_good) * len(df_good.columns) * 20} bytes</span>
            </div>
            """, unsafe_allow_html=True)
            
            if improvement_time > 0:
                st.markdown(f"""
                <div class="improvement-badge">
                    ⚡ {improvement_time:.1f}% mais rápido
                </div>
                """, unsafe_allow_html=True)
    
    st.divider()
    st.info(f"💡 **Explicação**: {comparison['explanation']}")
    
    # Gráfico de comparação
    st.markdown("<h4 style='margin-top: 30px;'>📊 Comparação Visual de Performance</h4>", unsafe_allow_html=True)
    
    if df_bad is not None and df_good is not None:
        comparison_data = {
            'Métrica': ['Tempo (s)', 'Registros', 'Colunas'],
            'Antes': [time_bad, len(df_bad), len(df_bad.columns)],
            'Depois': [time_good, len(df_good), len(df_good.columns)]
        }
        
        fig = go.Figure(data=[
            go.Bar(name='❌ Antes', x=['Tempo (s)', 'Registros', 'Colunas'], y=[time_bad, len(df_bad), len(df_bad.columns)], marker_color='#ef4444'),
            go.Bar(name='✅ Depois', x=['Tempo (s)', 'Registros', 'Colunas'], y=[time_good, len(df_good), len(df_good.columns)], marker_color='#22c55e')
        ])
        fig.update_layout(
            title="Performance: Antes vs Depois",
            barmode='group',
            template='plotly_dark',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(15,23,42,0.3)',
            font=dict(color='#E2E8F0')
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# 2️⃣ QUERY BUILDER - CONSTRUTOR GUIADO
# ============================================================================
elif menu == "🤖 Query Builder":
    st.markdown('<h2 class="section-header">🤖 Query Builder Inteligente</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #cbd5e1; margin-bottom: 30px;">Construa queries SQL sem precisar saber a sintaxe. O builder gera o SQL automaticamente!</p>', unsafe_allow_html=True)
    
    # Passo 1: Selecionar Tabela
    st.markdown('<div class="builder-step active"><h4>📊 Passo 1: Escolha a Tabela</h4>', unsafe_allow_html=True)
    selected_table = st.selectbox("Tabela:", ["usuarios", "vendas", "produtos"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Passo 2: Selecionar Colunas
    st.markdown('<div class="builder-step"><h4>📋 Passo 2: Selecione Colunas</h4>', unsafe_allow_html=True)
    
    table_columns = {
        "usuarios": ["id", "nome", "email", "ativo", "created_at", "categoria"],
        "vendas": ["id", "usuario_id", "valor", "status", "data"],
        "produtos": ["id", "nome", "categoria", "preco"]
    }
    
    selected_columns = st.multiselect(
        "Colunas:",
        table_columns[selected_table],
        default=[table_columns[selected_table][0]],
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Passo 3: Adicionar Filtros
    st.markdown('<div class="builder-step"><h4>🔍 Passo 3: Filtros (Opcional)</h4>', unsafe_allow_html=True)
    
    add_filter = st.checkbox("Adicionar filtro WHERE")
    filters = []
    
    if add_filter:
        col1, col2, col3 = st.columns(3)
        with col1:
            filter_column = st.selectbox("Coluna:", table_columns[selected_table], key="filter_col", label_visibility="collapsed")
        with col2:
            filter_op = st.selectbox("Operador:", ["=", ">", "<", ">=", "<=", "!=", "LIKE"], key="filter_op", label_visibility="collapsed")
        with col3:
            filter_value = st.text_input("Valor:", key="filter_val", label_visibility="collapsed")
        
        if filter_value:
            filters.append((filter_column, filter_op, filter_value))
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Passo 4: Ordenação & Limite
    st.markdown('<div class="builder-step"><h4>⬇️ Passo 4: Ordenação & Limite</h4>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        order_column = st.selectbox("Ordenar por:", ["Nenhum"] + table_columns[selected_table], key="order_col", label_visibility="collapsed")
    with col2:
        order_direction = st.selectbox("Direção:", ["ASC", "DESC"], key="order_dir", label_visibility="collapsed")
    with col3:
        limit_value = st.number_input("Limite:", min_value=1, max_value=1000, value=10, key="limit_val", label_visibility="collapsed")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Gerar Query
    query_parts = []
    query_parts.append(f"SELECT {', '.join(selected_columns)}")
    query_parts.append(f"FROM {selected_table}")
    
    if filters:
        where_clause = " AND ".join([f"{col} {op} '{val}'" if op == "LIKE" else f"{col} {op} '{val}'" for col, op, val in filters])
        query_parts.append(f"WHERE {where_clause}")
    
    if order_column != "Nenhum":
        query_parts.append(f"ORDER BY {order_column} {order_direction}")
    
    query_parts.append(f"LIMIT {limit_value};")
    generated_query = "\n".join(query_parts)
    
    st.divider()
    st.markdown('<h4 style="color: var(--accent); margin-top: 30px;">📝 Query Gerada:</h4>', unsafe_allow_html=True)
    st.code(generated_query, language="sql")
    
    # Executar Query
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Executar Query", use_container_width=True):
            df, message = execute_query(generated_query)
            if df is not None:
                st.success(message)
                st.dataframe(df, use_container_width=True)
            else:
                st.error(message)
    
    with col2:
        if st.button("📋 Copiar Query", use_container_width=True):
            st.success("Query copiada para clipboard!")
            st.code(generated_query, language="sql")

# ============================================================================
# 3️⃣ DATA EXPLORER - EXPLORAÇÃO VISUAL
# ============================================================================
elif menu == "🔍 Data Explorer":
    st.markdown('<h2 class="section-header">🔍 Data Explorer - Explore Visualmente</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #cbd5e1; margin-bottom: 30px;">Explore os dados visualmente antes de escrever SQL.</p>', unsafe_allow_html=True)
    
    col_table, col_stats = st.columns(2)
    
    with col_table:
        st.markdown('<h4>📊 Tabelas Disponíveis</h4>', unsafe_allow_html=True)
        selected_explore_table = st.radio("", ["usuarios", "vendas", "produtos"], label_visibility="collapsed")
    
    with col_stats:
        st.markdown('<h4>📈 Estatísticas</h4>', unsafe_allow_html=True)
        df_explore, _ = execute_query(f"SELECT * FROM {selected_explore_table}")
        if df_explore is not None:
            st.metric("Total de Registros", len(df_explore))
    
    st.divider()
    
    # Mostrar dados
    st.markdown(f'<h4>📋 Dados de {selected_explore_table.upper()}</h4>', unsafe_allow_html=True)
    df_explore, _ = execute_query(f"SELECT * FROM {selected_explore_table}")
    
    if df_explore is not None:
        st.dataframe(df_explore, use_container_width=True)
        
        # Análise por coluna
        st.markdown('<h4 style="margin-top: 30px;">📊 Análise por Coluna</h4>', unsafe_allow_html=True)
        
        for col in df_explore.columns:
            if df_explore[col].dtype == 'object':
                # Coluna texto
                value_counts = df_explore[col].value_counts()
                fig = px.pie(values=value_counts.values, names=value_counts.index, title=f"Distribuição: {col}")
                fig.update_layout(template='plotly_dark', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(15,23,42,0.3)', font=dict(color='#E2E8F0'))
                st.plotly_chart(fig, use_container_width=True)
            elif df_explore[col].dtype in ['int64', 'float64']:
                # Coluna numérica
                fig = px.histogram(df_explore, x=col, nbins=10, title=f"Distribuição: {col}")
                fig.update_layout(template='plotly_dark', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(15,23,42,0.3)', font=dict(color='#E2E8F0'))
                st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# 4️⃣ QUERY DEBUGGER - EXECUÇÃO PASSO A PASSO
# ============================================================================
elif menu == "🐛 Query Debugger":
    st.markdown('<h2 class="section-header">🐛 Query Debugger - Execute Passo a Passo</h2>', unsafe_allow_html=True)
    st.markdown('<p style="color: #cbd5e1; margin-bottom: 30px;">Veja o resultado intermediário de cada parte da query.</p>', unsafe_allow_html=True)
    
    example_queries = {
        "SELECT Simples": "SELECT id, nome FROM usuarios LIMIT 5;",
        "WHERE Filter": "SELECT id, nome FROM usuarios WHERE ativo = true;",
        "JOIN": "SELECT u.nome, v.valor FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id LIMIT 5;",
        "GROUP BY": "SELECT usuario_id, COUNT(*) as total FROM vendas GROUP BY usuario_id;"
    }
    
    selected_example = st.selectbox("Escolha um exemplo ou escreva sua query:", list(example_queries.keys()))
    
    if selected_example in example_queries:
        debug_query = example_queries[selected_example]
    else:
        debug_query = st.text_area("Sua Query SQL:", height=150)
    
    if st.button("🔍 Analisar Query"):
        # Análise da query
        st.markdown('<h4 style="margin-top: 30px; color: var(--accent);">📊 Resultado</h4>', unsafe_allow_html=True)
        
        df_debug, msg_debug = execute_query(debug_query)
        
        if df_debug is not None:
            st.success(msg_debug)
            
            # Mostrar resultado
            st.markdown('<div class="debug-step"><h5>📈 Resultado Final</h5>', unsafe_allow_html=True)
            st.dataframe(df_debug, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Estatísticas
            st.markdown('<h5 style="color: var(--accent); margin-top: 20px;">📊 Estatísticas</h5>', unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Registros", len(df_debug))
            with col2:
                st.metric("Colunas", len(df_debug.columns))
            with col3:
                st.metric("Tipo de Dados", df_debug.dtypes.mode[0] if len(df_debug.dtypes.mode) > 0 else "Unknown")
        else:
            st.error(msg_debug)

# ============================================================================
# 5️⃣ DESAFIOS ADAPTATIVOS
# ============================================================================
elif menu == "🎯 Desafios Adaptativos":
    st.markdown('<h2 class="section-header">🎯 Desafios Adaptativos</h2>', unsafe_allow_html=True)
    st.markdown(f'<p style="color: #cbd5e1; margin-bottom: 30px;">Nível Atual: <span style="color: var(--accent); font-weight: 700;">{st.session_state.adaptive_level}</span>/10</p>', unsafe_allow_html=True)
    
    adaptive_challenges = [
        {
            "level": 1,
            "title": "Contar Usuários",
            "problem": "Quantos usuários estão ativos?",
            "answer": "SELECT COUNT(*) FROM usuarios WHERE ativo = true;",
            "points": 10,
            "context": "Você trabalha em uma startup. O CEO quer saber quantos usuários ativos temos hoje."
        },
        {
            "level": 2,
            "title": "Total de Vendas",
            "problem": "Qual é o valor total de vendas pagas?",
            "answer": "SELECT SUM(valor) FROM vendas WHERE status = 'pago';",
            "points": 15,
            "context": "O CFO precisa do total em receita paga até agora."
        },
        {
            "level": 3,
            "title": "Usuários com Mais Vendas",
            "problem": "Qual usuário tem mais vendas?",
            "answer": "SELECT usuario_id, COUNT(*) as total FROM vendas GROUP BY usuario_id ORDER BY total DESC LIMIT 1;",
            "points": 20,
            "context": "O time de vendas quer reconhecer o melhor cliente."
        }
    ]
    
    current_challenge = [c for c in adaptive_challenges if c["level"] == st.session_state.adaptive_level]
    
    if current_challenge:
        challenge = current_challenge[0]
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #1E293B 0%, #334155 100%); border: 2px solid var(--accent); border-radius: 12px; padding: 25px; margin-bottom: 20px;">
            <p style="color: var(--accent); font-weight: 600; font-size: 1.2rem; margin: 0;">📖 CONTEXTO</p>
            <p style="color: #cbd5e1; margin-top: 10px; font-size: 1rem; line-height: 1.6;">{challenge['context']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f'<h4 style="color: var(--accent); margin-top: 30px;">❓ Desafio</h4>', unsafe_allow_html=True)
        st.info(f"**{challenge['problem']}** | Pontos: {challenge['points']}")
        
        user_answer = st.text_area("Sua Query SQL:", placeholder="SELECT...", height=120)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("✅ Enviar Resposta", use_container_width=True):
                if user_answer.strip():
                    # Executar resposta do usuário
                    df_user, _ = execute_query(user_answer)
                    # Executar resposta correta
                    df_correct, _ = execute_query(challenge["answer"])
                    
                    if df_user is not None and df_correct is not None:
                        if len(df_user) == len(df_correct):
                            st.success(f"🎉 Correto! Você ganhou {challenge['points']} pontos!")
                            st.session_state.user_points += challenge['points']
                            st.session_state.adaptive_level = min(st.session_state.adaptive_level + 1, 10)
                            st.balloons()
                        else:
                            st.error("❌ Resultado diferente. Tente novamente!")
                    else:
                        st.error("❌ Erro na query.")
                else:
                    st.warning("Escreva uma query primeiro!")
        
        with col2:
            if st.button("💡 Dica (-5 pts)", use_container_width=True):
                st.info("Use GROUP BY e ORDER BY para encontrar o máximo.")
                st.session_state.user_points = max(0, st.session_state.user_points - 5)
        
        with col3:
            if st.button("🔍 Ver Solução (-10 pts)", use_container_width=True):
                st.code(challenge["answer"], language="sql")
                st.session_state.user_points = max(0, st.session_state.user_points - 10)

# ============================================================================
# 6️⃣ PROGRESSO
# ============================================================================
elif menu == "📊 Seu Progresso":
    st.markdown('<h2 class="section-header">📊 Seu Progresso e Estatísticas</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Pontos Totais", st.session_state.user_points)
    with col2:
        st.metric("Desafios Completos", len(st.session_state.challenges_completed))
    with col3:
        st.metric("Favoritos", len(st.session_state.favorites))
    with col4:
        st.metric("Nível Adaptativo", f"{st.session_state.adaptive_level}/10")
    
    st.divider()
    
    # Progresso de aprendizado
    st.markdown('<h4 style="color: var(--accent);">📈 Progresso de Aprendizado</h4>', unsafe_allow_html=True)
    
    progress_value = st.session_state.adaptive_level / 10
    st.progress(progress_value, text=f"Nível {st.session_state.adaptive_level}/10")
    
    # Timeline
    st.markdown('<h4 style="color: var(--accent); margin-top: 30px;">📅 Timeline de Aprendizado</h4>', unsafe_allow_html=True)
    
    timeline_events = [
        {"date": datetime.now().strftime("%Y-%m-%d"), "event": "Iniciou a plataforma", "icon": "🚀"},
        {"date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"), "event": "Completou primeiro desafio", "icon": "✅"},
        {"date": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"), "event": "Aprendeu sobre JOINs", "icon": "🔗"},
    ]
    
    for event in timeline_events:
        st.markdown(f"""
        <div class="timeline-item">
            <span style="font-size: 1.5rem;">{event['icon']}</span>
            <div>
                <p style="color: var(--accent); font-weight: 700; margin: 0;">{event['event']}</p>
                <p style="color: #94a3b8; margin: 0;">{event['date']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 40px 0; border-top: 1px solid var(--border); color: #cbd5e1; margin-top: 60px;">
    <p style="margin-bottom: 10px; font-size: 0.95rem;">
        <span style="color: var(--accent); font-weight: 600;">SQL - Melhores Práticas Pro</span> 
        • Criado por Rodrigo Aiosa
    </p>
    <p style="font-size: 0.85rem; color: #94a3b8;">
        Transforme seus dados em vantagem competitiva com SQL estratégico
    </p>
</div>
""", unsafe_allow_html=True)
