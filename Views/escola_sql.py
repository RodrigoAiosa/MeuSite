import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="SQL Server - Melhores Práticas Pro",
    page_icon="🖥️",
    layout="wide"
)

# --- INICIALIZAR SESSION STATE ---
if 'sqlserver_favorites' not in st.session_state:
    st.session_state.sqlserver_favorites = set()
if 'sqlserver_learned' not in st.session_state:
    st.session_state.sqlserver_learned = set()
if 'sqlserver_points' not in st.session_state:
    st.session_state.sqlserver_points = 0
if 'sqlserver_xp' not in st.session_state:
    st.session_state.sqlserver_xp = 0
if 'sqlserver_badges' not in st.session_state:
    st.session_state.sqlserver_badges = set()
if 'sqlserver_challenges_completed' not in st.session_state:
    st.session_state.sqlserver_challenges_completed = set()
if 'sqlserver_streak' not in st.session_state:
    st.session_state.sqlserver_streak = 0
if 'sqlserver_editor_runs' not in st.session_state:
    st.session_state.sqlserver_editor_runs = 0

MASTERY_LEVELS = {
    1: {"title": "🥉 T-SQL Padawan", "icon": "🥉", "xp_required": 0},
    2: {"title": "🥈 Query Tuner", "icon": "🥈", "xp_required": 250},
    3: {"title": "🥇 SQL Server Master", "icon": "🥇", "xp_required": 750},
    4: {"title": "💎 DBA Arquiteto", "icon": "💎", "xp_required": 1500},
    5: {"title": "🏆 SQL Server Elite", "icon": "🏆", "xp_required": 2500},
}

BADGES = {
    "first_steps": {"icon": "👣", "title": "Primeiros Passos", "description": "Completou a 1ª prática", "condition": lambda p: p >= 1},
    "ten_practices": {"icon": "🔟", "title": "Persistência", "description": "Completou 10 práticas", "condition": lambda p: p >= 10},
    "twenty_practices": {"icon": "2️⃣0️⃣", "title": "Veterano", "description": "Completou 20 práticas", "condition": lambda p: p >= 20},
    "favorite_collector": {"icon": "⭐", "title": "Colecionador", "description": "Favoritou 10 práticas", "condition": lambda p: p >= 10},
    "query_runner": {"icon": "⚡", "title": "Query Runner", "description": "Executou 20 queries no editor", "condition": lambda p: p >= 20},
    "index_master": {"icon": "🗂️", "title": "Mestre dos Índices", "description": "Completou práticas de indexação", "condition": lambda p: p >= 1},
    "code_master": {"icon": "👑", "title": "Rei do T-SQL", "description": "1000+ pontos conquistados", "condition": lambda p: p >= 1000},
}

CHALLENGES = [
    {"id": "challenge_1", "title": "Mestre da Indexação", "difficulty": "Intermediário", "xp_reward": 100, "description": "Complete 3 práticas sobre índices e SARGability"},
    {"id": "challenge_2", "title": "Domador de Transações", "difficulty": "Avançado", "xp_reward": 150, "description": "Complete 2 práticas sobre transações e concorrência"},
    {"id": "challenge_3", "title": "Editor Speedrunner", "difficulty": "Iniciante", "xp_reward": 50, "description": "Execute 20 queries no editor interativo"},
    {"id": "challenge_4", "title": "Colecionador de Estrelas", "difficulty": "Iniciante", "xp_reward": 75, "description": "Favoritou 5 práticas"},
    {"id": "challenge_5", "title": "Analista de Planos", "difficulty": "Avançado", "xp_reward": 200, "description": "Complete todas as práticas sobre Execution Plans e Query Store"},
]

# ── DESIGN (mesma paleta SQL/Python Pro) ──
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .main, [data-testid="stAppViewContainer"] { background-color: #0a0e27 !important; }
[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(139,92,246,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 40% 30% at 80% 60%, rgba(59,130,246,0.08) 0%, transparent 50%);
}
[data-testid="stHeader"] { background: transparent !important; }
.main h1, .main h2, .main h3, .main h4, .main p, .main a, .main li,
[data-testid="stAppViewContainer"] div:not([data-testid="stSidebar"]) {
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stMarkdownContainer"] { width: 100% !important; }
.block-container { max-width: 100% !important; padding-left: 4rem !important; padding-right: 4rem !important; }

.hero-wrapper { text-align: center; padding: 80px 20px 50px; width: 100%; display: flex; flex-direction: column; align-items: center; }
.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2.4rem, 5vw, 4rem);
    font-weight: 800; line-height: 1.1; letter-spacing: -1.5px;
    color: #f0f4ff; margin: 0 auto 20px; max-width: 760px; text-align: center;
}
.hero-title .accent {
    background: linear-gradient(135deg, #a78bfa 0%, #7c3aed 50%, #c4b5fd 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
}
.hero-subtitle { font-size: 1.05rem; font-weight: 300; color: #7b8ba8; max-width: 560px; margin: 0 auto 48px; line-height: 1.7; text-align: center; }
.hero-stats { display: flex; justify-content: center; gap: 48px; flex-wrap: wrap; margin-bottom: 60px; }
.hero-stat { text-align: center; }
.hero-stat-number { font-family: 'Syne', sans-serif !important; font-size: 2rem; font-weight: 800; color: #a78bfa; display: block; line-height: 1; }
.hero-stat-label { font-size: 0.78rem; color: #4a5568; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 6px; display: block; }
.hero-divider { width: 100%; max-width: 900px; margin: 0 auto 60px; height: 1px; background: linear-gradient(90deg, transparent, rgba(167,139,250,0.3), transparent); }

.section-header {
    font-family: 'Syne', sans-serif !important; font-size: 1.5rem; font-weight: 800; color: #f0f4ff;
    margin: 50px 0 28px; padding-bottom: 16px; border-bottom: 1px solid rgba(167,139,250,0.2);
    letter-spacing: -0.5px; position: relative;
}
.section-header::after { content: ''; position: absolute; bottom: -1px; left: 0; width: 48px; height: 2px; background: #a78bfa; }

.filter-section, .editor-section {
    background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%);
    border: 1px solid rgba(167,139,250,0.2); border-radius: 20px; padding: 30px 32px; margin: 20px 0 32px;
}
.editor-title {
    font-family: 'Syne', sans-serif !important; font-size: 0.9rem; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase; color: #a78bfa; margin-bottom: 14px;
}

.badge { background: linear-gradient(145deg, rgba(255,255,255,0.05) 0%, rgba(0,0,0,0.3) 100%); border: 1px solid rgba(167,139,250,0.2); border-radius: 10px; padding: 10px 15px; text-align: center; font-size: 2rem; cursor: pointer; transition: all 0.3s ease; }
.badge:hover { transform: scale(1.1); border-color: #a78bfa; box-shadow: 0 0 15px rgba(167,139,250,0.3); }
.badge-locked { opacity: 0.3; }

.challenge-box { background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(167,139,250,0.2); border-radius: 12px; padding: 15px; margin: 10px 0; }
.challenge-completed { border-color: #22c55e; background: linear-gradient(145deg, rgba(34,197,94,0.1) 0%, rgba(0,0,0,0.2) 100%); }

.streak-fire { font-size: 2rem; animation: bounce 1s infinite; }
@keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }

.success-box { background: linear-gradient(145deg, rgba(34,197,94,0.1) 0%, rgba(34,197,94,0.05) 100%); border: 1px solid rgba(34,197,94,0.3); border-radius: 12px; padding: 15px; margin-top: 15px; font-family: 'Courier New', monospace; color: #22c55e; white-space: pre-wrap; word-wrap: break-word; }
.error-box { background: linear-gradient(145deg, rgba(239,68,68,0.1) 0%, rgba(239,68,68,0.05) 100%); border: 1px solid rgba(239,68,68,0.3); border-radius: 12px; padding: 15px; margin-top: 15px; font-family: 'Courier New', monospace; color: #ff6b6b; white-space: pre-wrap; word-wrap: break-word; }
.achievement-pop { animation: slideIn 0.5s ease-out; }
@keyframes slideIn { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }

.info-panel { background: linear-gradient(145deg, rgba(255,255,255,0.03) 0%, rgba(0,0,0,0.2) 100%); border: 1px solid rgba(167,139,250,0.2); border-radius: 16px; padding: 24px; }
.info-panel-title { font-family: 'Syne', sans-serif !important; color: #a78bfa; font-weight: 700; font-size: 0.8rem; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 16px; }

.stSelectbox > div > div { background: rgba(255,255,255,0.03) !important; border: 1px solid rgba(167,139,250,0.2) !important; color: #e2e8f0 !important; border-radius: 12px !important; }
.stTextArea > div > div { background: rgba(255,255,255,0.03) !important; border: 1px solid rgba(167,139,250,0.2) !important; color: #e2e8f0 !important; border-radius: 12px !important; }
div[data-testid="stTextInput"] input { background-color: rgba(255,255,255,0.03) !important; color: #e2e8f0 !important; border: 1px solid rgba(167,139,250,0.25) !important; border-radius: 14px !important; padding: 14px 22px !important; font-size: 0.95rem !important; }
hr { border: none !important; border-top: 1px solid rgba(167,139,250,0.1) !important; margin: 40px 0 !important; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0a0e27; }
::-webkit-scrollbar-thumb { background: rgba(167,139,250,0.2); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(167,139,250,0.4); }
</style>
""", unsafe_allow_html=True)

# ── HERO ──
st.markdown("""
<div class="hero-wrapper">
    <h1 class="hero-title">
        Melhores Práticas SQL Server para <span class="accent">queries de produção</span>
    </h1>
    <p class="hero-subtitle">
        T-SQL, indexação, transações e tuning de performance — o que separa uma query
        que funciona de uma query pronta para escala.
    </p>
    <div class="hero-stats">
        <div class="hero-stat"><span class="hero-stat-number">30+</span><span class="hero-stat-label">Práticas</span></div>
        <div class="hero-stat"><span class="hero-stat-number">5</span><span class="hero-stat-label">Categorias</span></div>
        <div class="hero-stat"><span class="hero-stat-number">3</span><span class="hero-stat-label">Níveis</span></div>
    </div>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)


# --- FUNÇÕES AUXILIARES ---
def get_current_level(xp):
    for level in sorted(MASTERY_LEVELS.keys(), reverse=True):
        if xp >= MASTERY_LEVELS[level]["xp_required"]:
            return level
    return 1

def get_xp_for_next_level(current_level):
    if current_level >= 5:
        return MASTERY_LEVELS[5]["xp_required"] + 1000
    return MASTERY_LEVELS[current_level + 1]["xp_required"]

def check_badges(learned_count, favorites_count, editor_runs, points):
    new_badges = set()
    if learned_count >= 1: new_badges.add("first_steps")
    if learned_count >= 10: new_badges.add("ten_practices")
    if learned_count >= 20: new_badges.add("twenty_practices")
    if favorites_count >= 10: new_badges.add("favorite_collector")
    if editor_runs >= 20: new_badges.add("query_runner")
    if points >= 1000: new_badges.add("code_master")
    return new_badges


# --- HEADER PONTOS + STREAK ---
col1, col2, col3 = st.columns([2, 3, 2])
with col2:
    st.markdown('<h3 style="text-align: center; color: #7c3aed;">Jornada de Maestria SQL Server</h3>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<h1 style="text-align: center; font-size: 2rem;">⭐ {st.session_state.sqlserver_points} pontos</h1>', unsafe_allow_html=True)

current_level = get_current_level(st.session_state.sqlserver_xp)

if st.session_state.sqlserver_streak > 0:
    st.markdown(f'<p style="text-align: center; font-size: 1.3rem;"><span class="streak-fire">🔥</span> {st.session_state.sqlserver_streak} dias em sequência!</p>', unsafe_allow_html=True)

# --- TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📚 Práticas", "✏️ Editor", "🎯 Desafios", "🏆 Badges", "📊 Perfil"])

# ============================================================================
# TAB 1: PRÁTICAS
# ============================================================================
with tab1:
    st.markdown('<h3 class="section-header">🔎 Filtrar Práticas</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        selected_difficulty = st.selectbox("📈 Nível de Dificuldade", ["Todas", "Iniciante", "Intermediário", "Avançado"], key="sqlserver_difficulty")
    with col2:
        search = st.text_input("🔍 Buscar prática", key="sqlserver_search")

    sqlserver_practices = [
        # ── INICIANTE ──
        {"icon": "🔇", "title": "Usar SET NOCOUNT ON", "category": "Performance", "difficulty": "Iniciante",
         "description": "Evite o tráfego extra da mensagem 'rows affected' em procedures.",
         "bad_code": "CREATE PROCEDURE dbo.ObterVendas\nAS\nBEGIN\n    SELECT * FROM Vendas;\nEND;",
         "good_code": "CREATE PROCEDURE dbo.ObterVendas\nAS\nBEGIN\n    SET NOCOUNT ON;\n    SELECT * FROM Vendas;\nEND;",
         "benefit": "Reduz tráfego de rede e melhora performance.",
         "explanation": "Sem SET NOCOUNT ON, o SQL Server envia uma mensagem de contagem de linhas após cada instrução, gerando overhead desnecessário em procedures chamadas com frequência."},
        {"icon": "🔍", "title": "Evitar SELECT *", "category": "Performance", "difficulty": "Iniciante",
         "description": "Selecione apenas as colunas necessárias.",
         "bad_code": "SELECT * FROM Pedidos WHERE Ano = 2024;",
         "good_code": "SELECT PedidoID, ClienteID, ValorTotal, DataPedido\nFROM Pedidos\nWHERE Ano = 2024;",
         "benefit": "Reduz I/O e permite index seeks cobertos.",
         "explanation": "Especificar colunas permite ao otimizador usar índices de cobertura (covering indexes) e reduz dados trafegados pela rede."},
        {"icon": "🛡️", "title": "Usar Parâmetros em vez de SQL Dinâmico Concatenado", "category": "Segurança", "difficulty": "Iniciante",
         "description": "Proteja-se contra SQL Injection com sp_executesql.",
         "bad_code": "DECLARE @sql NVARCHAR(MAX);\nSET @sql = 'SELECT * FROM Usuarios WHERE Email = ''' + @email + '''';\nEXEC(@sql);",
         "good_code": "EXEC sp_executesql\n    N'SELECT * FROM Usuarios WHERE Email = @Email',\n    N'@Email NVARCHAR(100)',\n    @Email = @email;",
         "benefit": "Elimina risco de SQL Injection.",
         "explanation": "sp_executesql trata @Email como parâmetro tipado, não como texto SQL concatenado — impossibilitando injeção de código malicioso."},
        {"icon": "🔝", "title": "Usar TOP para Limitar Resultados", "category": "Performance", "difficulty": "Iniciante",
         "description": "Sempre limite resultados em queries exploratórias.",
         "bad_code": "SELECT * FROM LogAuditoria ORDER BY DataHora DESC;",
         "good_code": "SELECT TOP 100 *\nFROM LogAuditoria\nORDER BY DataHora DESC;",
         "benefit": "Evita retornar milhões de linhas sem necessidade.",
         "explanation": "TOP limita o volume de dados retornado, essencial em tabelas grandes como logs de auditoria."},
        {"icon": "🈳", "title": "Tratar NULL com ISNULL/COALESCE", "category": "Lógica & Precisão", "difficulty": "Iniciante",
         "description": "NULL não é zero nem string vazia.",
         "bad_code": "SELECT SUM(Comissao) FROM Vendas WHERE Status = 'Concluida';",
         "good_code": "SELECT SUM(ISNULL(Comissao, 0)) AS TotalComissao\nFROM Vendas\nWHERE Status = 'Concluida';",
         "benefit": "Evita resultados NULL inesperados em agregações.",
         "explanation": "ISNULL substitui valores nulos por um padrão; COALESCE faz o mesmo e aceita múltiplos argumentos, útil com mais de uma alternativa."},
        {"icon": "📛", "title": "Usar Convenção schema.tabela", "category": "Qualidade & Manutenção", "difficulty": "Iniciante",
         "description": "Sempre qualifique objetos com o schema.",
         "bad_code": "SELECT * FROM Clientes;",
         "good_code": "SELECT * FROM dbo.Clientes;",
         "benefit": "Evita ambiguidade e melhora plano de cache.",
         "explanation": "Qualificar com o schema (dbo.Clientes) evita resolução de nome ambígua e permite ao SQL Server reutilizar planos de execução em cache com mais eficiência."},
        {"icon": "📏", "title": "Escolher Tipos de Dados Apropriados", "category": "Qualidade & Manutenção", "difficulty": "Iniciante",
         "description": "Evite NVARCHAR(MAX) ou tipos genéricos sem necessidade.",
         "bad_code": "CREATE TABLE Produtos (\n    Codigo NVARCHAR(MAX),\n    Preco NVARCHAR(MAX)\n);",
         "good_code": "CREATE TABLE Produtos (\n    Codigo VARCHAR(20),\n    Preco DECIMAL(10,2)\n);",
         "benefit": "Menos espaço em disco, índices mais eficientes.",
         "explanation": "Tipos genéricos como NVARCHAR(MAX) impedem certas otimizações de índice e consomem mais memória/disco do que o necessário."},
        {"icon": "📋", "title": "Documentar Procedures Complexas", "category": "Qualidade & Manutenção", "difficulty": "Iniciante",
         "description": "Comente a lógica de negócio, não o óbvio.",
         "bad_code": "CREATE PROCEDURE dbo.CalcularDesconto\nAS\nBEGIN\n    UPDATE Pedidos SET Desconto = 0.1 WHERE ValorTotal > 1000;\nEND;",
         "good_code": "-- Aplica 10% de desconto para pedidos acima de R$1000,\n-- conforme política comercial vigente desde 01/2026\nCREATE PROCEDURE dbo.CalcularDesconto\nAS\nBEGIN\n    SET NOCOUNT ON;\n    UPDATE Pedidos SET Desconto = 0.1 WHERE ValorTotal > 1000;\nEND;",
         "benefit": "Facilita manutenção futura.",
         "explanation": "Comentários que explicam a regra de negócio (o 'porquê') são mais valiosos do que descrever o que o código já mostra."},
        {"icon": "🛑", "title": "Usar TRY/CATCH para Tratamento de Erros", "category": "Qualidade & Manutenção", "difficulty": "Iniciante",
         "description": "Capture e trate erros explicitamente em T-SQL.",
         "bad_code": "UPDATE Contas SET Saldo = Saldo - 100 WHERE ContaID = 1;\nUPDATE Contas SET Saldo = Saldo + 100 WHERE ContaID = 2;",
         "good_code": "BEGIN TRY\n    BEGIN TRANSACTION;\n    UPDATE Contas SET Saldo = Saldo - 100 WHERE ContaID = 1;\n    UPDATE Contas SET Saldo = Saldo + 100 WHERE ContaID = 2;\n    COMMIT TRANSACTION;\nEND TRY\nBEGIN CATCH\n    ROLLBACK TRANSACTION;\n    THROW;\nEND CATCH;",
         "benefit": "Evita estados inconsistentes em caso de falha.",
         "explanation": "TRY/CATCH combinado com transações garante que, se uma etapa falhar, todas as alterações sejam desfeitas (ROLLBACK), mantendo a consistência dos dados."},
        {"icon": "🕐", "title": "GETDATE() vs SYSDATETIME()", "category": "Qualidade & Manutenção", "difficulty": "Iniciante",
         "description": "Escolha a função de data certa para a precisão necessária.",
         "bad_code": "INSERT INTO LogEventos (DataHora) VALUES (GETDATE());\n-- precisão de milissegundos pode não ser suficiente",
         "good_code": "INSERT INTO LogEventos (DataHora) VALUES (SYSDATETIME());\n-- precisão de 100 nanossegundos, ideal para ordenação fina de eventos",
         "benefit": "Precisão adequada para auditoria e ordenação.",
         "explanation": "GETDATE() tem precisão de ~3ms; SYSDATETIME() oferece precisão de 100ns, importante quando múltiplos eventos podem ocorrer no mesmo milissegundo."},

        # ── INTERMEDIÁRIO ──
        {"icon": "🗂️", "title": "Criar Índices em Colunas de JOIN/WHERE", "category": "Índices & Estatísticas", "difficulty": "Intermediário",
         "description": "Colunas usadas em filtros e junções precisam de índice.",
         "bad_code": "-- Tabela Pedidos sem índice em ClienteID, usada em milhares de JOINs\nSELECT * FROM Pedidos p JOIN Clientes c ON p.ClienteID = c.ClienteID;",
         "good_code": "CREATE NONCLUSTERED INDEX IX_Pedidos_ClienteID\nON Pedidos (ClienteID);",
         "benefit": "Transforma table scans em index seeks.",
         "explanation": "Sem índice na coluna de junção, o SQL Server precisa escanear a tabela inteira (table scan) a cada consulta, o que é caro em tabelas grandes."},
        {"icon": "🎯", "title": "Evitar Funções em Colunas Indexadas (SARGability)", "category": "Índices & Estatísticas", "difficulty": "Intermediário",
         "description": "Funções sobre a coluna impedem o uso do índice.",
         "bad_code": "SELECT * FROM Pedidos\nWHERE YEAR(DataPedido) = 2024;",
         "good_code": "SELECT * FROM Pedidos\nWHERE DataPedido >= '2024-01-01' AND DataPedido < '2025-01-01';",
         "benefit": "Permite index seek em vez de scan completo.",
         "explanation": "Aplicar YEAR() na coluna torna o predicado não-SARGable — o otimizador não consegue usar o índice de DataPedido e faz um scan completo."},
        {"icon": "🧩", "title": "CTEs em vez de Subqueries Aninhadas", "category": "T-SQL Moderno", "difficulty": "Intermediário",
         "description": "Common Table Expressions deixam queries complexas mais legíveis.",
         "bad_code": "SELECT * FROM (\n    SELECT ClienteID, SUM(ValorTotal) AS Total\n    FROM Pedidos\n    GROUP BY ClienteID\n) AS Sub\nWHERE Total > 1000;",
         "good_code": "WITH TotaisPorCliente AS (\n    SELECT ClienteID, SUM(ValorTotal) AS Total\n    FROM Pedidos\n    GROUP BY ClienteID\n)\nSELECT * FROM TotaisPorCliente\nWHERE Total > 1000;",
         "benefit": "Mais legível e reutilizável dentro da mesma query.",
         "explanation": "CTEs (WITH ... AS) nomeiam o resultado intermediário, facilitando leitura e permitindo reutilização em múltiplas partes da mesma consulta."},
        {"icon": "🏆", "title": "Usar Window Functions (ROW_NUMBER, RANK)", "category": "T-SQL Moderno", "difficulty": "Intermediário",
         "description": "Calcule rankings e numeração sem subqueries correlacionadas.",
         "bad_code": "-- Encontrar o pedido mais recente por cliente com subquery correlacionada\nSELECT * FROM Pedidos p\nWHERE DataPedido = (\n    SELECT MAX(DataPedido) FROM Pedidos WHERE ClienteID = p.ClienteID\n);",
         "good_code": "SELECT * FROM (\n    SELECT *,\n        ROW_NUMBER() OVER (PARTITION BY ClienteID ORDER BY DataPedido DESC) AS rn\n    FROM Pedidos\n) AS Numerado\nWHERE rn = 1;",
         "benefit": "Mais rápido e expressivo que subqueries correlacionadas.",
         "explanation": "ROW_NUMBER() OVER (PARTITION BY ...) calcula a numeração em uma única passada pelos dados, evitando reexecutar a subquery para cada linha."},
        {"icon": "🔀", "title": "Usar MERGE para Upsert", "category": "T-SQL Moderno", "difficulty": "Intermediário",
         "description": "Combine INSERT e UPDATE em uma única instrução atômica.",
         "bad_code": "IF EXISTS (SELECT 1 FROM Estoque WHERE ProdutoID = @id)\n    UPDATE Estoque SET Quantidade = @qtd WHERE ProdutoID = @id;\nELSE\n    INSERT INTO Estoque (ProdutoID, Quantidade) VALUES (@id, @qtd);",
         "good_code": "MERGE Estoque AS destino\nUSING (SELECT @id AS ProdutoID, @qtd AS Quantidade) AS origem\nON destino.ProdutoID = origem.ProdutoID\nWHEN MATCHED THEN\n    UPDATE SET Quantidade = origem.Quantidade\nWHEN NOT MATCHED THEN\n    INSERT (ProdutoID, Quantidade) VALUES (origem.ProdutoID, origem.Quantidade);",
         "benefit": "Operação atômica, evita condições de corrida.",
         "explanation": "MERGE executa a verificação e a ação (insert ou update) como uma única operação atômica, eliminando a janela de corrida entre o IF EXISTS e a ação subsequente."},
        {"icon": "📦", "title": "Temp Tables vs Table Variables", "category": "Performance", "difficulty": "Intermediário",
         "description": "Escolha a estrutura temporária certa para o volume de dados.",
         "bad_code": "-- Table variable usada para armazenar 500 mil linhas intermediárias\nDECLARE @Resultado TABLE (ID INT, Valor DECIMAL(10,2));",
         "good_code": "-- Temp table para grandes volumes: tem estatísticas e pode ser indexada\nCREATE TABLE #Resultado (ID INT, Valor DECIMAL(10,2));\nCREATE INDEX IX_Temp_ID ON #Resultado (ID);",
         "benefit": "Melhor plano de execução em grandes volumes.",
         "explanation": "Table variables não têm estatísticas atualizadas pelo otimizador, o que pode gerar planos de execução ruins em volumes grandes; temp tables (#) suportam índices e estatísticas."},
        {"icon": "🔐", "title": "Usar Transações Explícitas", "category": "Transações & Concorrência", "difficulty": "Intermediário",
         "description": "Agrupe operações relacionadas em uma transação.",
         "bad_code": "UPDATE Contas SET Saldo = Saldo - 100 WHERE ContaID = 1;\n-- se falhar aqui, a próxima linha não roda e o dinheiro \"some\"\nUPDATE Contas SET Saldo = Saldo + 100 WHERE ContaID = 2;",
         "good_code": "BEGIN TRANSACTION;\n    UPDATE Contas SET Saldo = Saldo - 100 WHERE ContaID = 1;\n    UPDATE Contas SET Saldo = Saldo + 100 WHERE ContaID = 2;\nCOMMIT TRANSACTION;",
         "benefit": "Garante atomicidade (tudo ou nada).",
         "explanation": "Sem uma transação explícita, cada instrução é confirmada (auto-commit) individualmente — uma falha no meio do processo deixa os dados inconsistentes."},
        {"icon": "🔒", "title": "Entender Níveis de Isolamento de Transação", "category": "Transações & Concorrência", "difficulty": "Intermediário",
         "description": "READ COMMITTED SNAPSHOT reduz bloqueios de leitura.",
         "bad_code": "-- Nível padrão READ COMMITTED: leituras podem bloquear escritas concorrentes",
         "good_code": "ALTER DATABASE MeuBanco SET READ_COMMITTED_SNAPSHOT ON;\n-- leituras usam versionamento de linha, sem bloquear escritas",
         "benefit": "Reduz contenção entre leitores e escritores.",
         "explanation": "READ_COMMITTED_SNAPSHOT usa versionamento de linhas (row versioning) em vez de locks compartilhados para leituras, reduzindo bloqueios em sistemas com alta concorrência."},
        {"icon": "🚫", "title": "Evitar Cursors — Preferir Operações Set-Based", "category": "Performance", "difficulty": "Intermediário",
         "description": "T-SQL é otimizado para operar em conjuntos, não linha a linha.",
         "bad_code": "DECLARE cur CURSOR FOR SELECT ProdutoID FROM Produtos;\nOPEN cur;\nFETCH NEXT FROM cur INTO @id;\nWHILE @@FETCH_STATUS = 0\nBEGIN\n    UPDATE Produtos SET Preco = Preco * 1.1 WHERE ProdutoID = @id;\n    FETCH NEXT FROM cur INTO @id;\nEND;",
         "good_code": "UPDATE Produtos SET Preco = Preco * 1.1;",
         "benefit": "Ordens de magnitude mais rápido.",
         "explanation": "Cursors processam linha a linha, com overhead de contexto a cada iteração; uma instrução UPDATE set-based aplica a mudança a todas as linhas de uma vez, usando o otimizador de consultas."},
        {"icon": "📤", "title": "Usar a Cláusula OUTPUT", "category": "T-SQL Moderno", "difficulty": "Intermediário",
         "description": "Capture linhas afetadas por INSERT/UPDATE/DELETE sem SELECT adicional.",
         "bad_code": "DELETE FROM Pedidos WHERE Status = 'Cancelado';\n-- precisa de outro SELECT para saber o que foi removido",
         "good_code": "DELETE FROM Pedidos\nOUTPUT DELETED.PedidoID, DELETED.ClienteID\nWHERE Status = 'Cancelado';",
         "benefit": "Evita uma consulta extra para auditoria.",
         "explanation": "OUTPUT retorna as linhas afetadas diretamente na mesma instrução, útil para auditoria, logging ou capturar IDs gerados em um INSERT."},
        {"icon": "❓", "title": "EXISTS vs IN para Performance", "category": "Performance", "difficulty": "Intermediário",
         "description": "EXISTS geralmente performa melhor com subqueries grandes.",
         "bad_code": "SELECT * FROM Clientes\nWHERE ClienteID IN (SELECT ClienteID FROM Pedidos);",
         "good_code": "SELECT * FROM Clientes c\nWHERE EXISTS (SELECT 1 FROM Pedidos p WHERE p.ClienteID = c.ClienteID);",
         "benefit": "Para no primeiro match, sem materializar toda a lista.",
         "explanation": "EXISTS interrompe a busca assim que encontra uma correspondência; IN pode precisar materializar toda a subquery antes de comparar, sendo mais lento em conjuntos grandes."},
        {"icon": "🔎", "title": "Usar Índices Filtrados", "category": "Índices & Estatísticas", "difficulty": "Intermediário",
         "description": "Indexe apenas o subconjunto de dados relevante.",
         "bad_code": "CREATE NONCLUSTERED INDEX IX_Pedidos_Status\nON Pedidos (Status);\n-- indexa TODOS os status, mesmo os raramente consultados",
         "good_code": "CREATE NONCLUSTERED INDEX IX_Pedidos_Pendentes\nON Pedidos (DataPedido)\nWHERE Status = 'Pendente';",
         "benefit": "Índice menor e mais rápido para consultas específicas.",
         "explanation": "Um índice filtrado (WHERE na definição do índice) cobre apenas o subconjunto de linhas relevante, reduzindo tamanho e melhorando a performance de consultas que filtram por esse critério."},
        {"icon": "📊", "title": "Manter Estatísticas Atualizadas", "category": "Índices & Estatísticas", "difficulty": "Intermediário",
         "description": "O otimizador depende de estatísticas precisas para bons planos.",
         "bad_code": "-- Estatísticas desatualizadas após grande carga de dados (bulk insert)\n-- nenhuma ação tomada",
         "good_code": "UPDATE STATISTICS dbo.Pedidos WITH FULLSCAN;",
         "benefit": "Planos de execução mais precisos.",
         "explanation": "Após grandes cargas ou mudanças no volume de dados, estatísticas desatualizadas levam o otimizador a escolher planos de execução ruins; UPDATE STATISTICS corrige isso."},

        # ── AVANÇADO ──
        {"icon": "🔬", "title": "Analisar Planos de Execução", "category": "Performance", "difficulty": "Avançado",
         "description": "Entenda onde o tempo é gasto antes de otimizar.",
         "bad_code": "-- Otimizar \"no escuro\", sem olhar o plano de execução real",
         "good_code": "SET STATISTICS IO ON;\nSET STATISTICS TIME ON;\n-- Habilitar \"Include Actual Execution Plan\" no SSMS antes de rodar a query",
         "benefit": "Identifica o gargalo real (scan, hash join custoso, etc.).",
         "explanation": "O plano de execução mostra exatamente quais operadores (scans, seeks, joins) consomem mais tempo/IO, permitindo otimizar o que de fato importa."},
        {"icon": "🗃️", "title": "Índices Columnstore para Data Warehousing", "category": "Índices & Estatísticas", "difficulty": "Avançado",
         "description": "Para cargas analíticas (OLAP), columnstore supera rowstore.",
         "bad_code": "-- Tabela de fatos com bilhões de linhas usando apenas índice rowstore tradicional",
         "good_code": "CREATE CLUSTERED COLUMNSTORE INDEX CCI_FatoVendas\nON FatoVendas;",
         "benefit": "Compressão alta e agregações muito mais rápidas.",
         "explanation": "Índices columnstore armazenam dados por coluna em vez de por linha, ideais para agregações (SUM, AVG) em tabelas de fatos de data warehouses."},
        {"icon": "🧱", "title": "Particionamento de Tabelas", "category": "Performance", "difficulty": "Avançado",
         "description": "Divida tabelas muito grandes por critério lógico (ex: data).",
         "bad_code": "-- Tabela de 500 milhões de linhas sem particionamento,\n-- todo DELETE de dados antigos é uma operação lenta e bloqueante",
         "good_code": "CREATE PARTITION FUNCTION PF_Data (DATE)\nAS RANGE RIGHT FOR VALUES ('2023-01-01', '2024-01-01', '2025-01-01');\n-- SWITCH PARTITION permite remover dados antigos quase instantaneamente",
         "benefit": "Manutenção e exclusão de dados antigos muito mais rápidas.",
         "explanation": "Com partição por data, remover dados antigos vira uma operação de metadados (SWITCH PARTITION) em vez de um DELETE linha a linha, que seria lento e geraria muito log de transação."},
        {"icon": "📈", "title": "Usar Query Store para Monitoramento", "category": "Performance", "difficulty": "Avançado",
         "description": "Monitore regressões de performance ao longo do tempo.",
         "bad_code": "-- Sem Query Store: perceber que uma query piorou só quando o usuário reclama",
         "good_code": "ALTER DATABASE MeuBanco SET QUERY_STORE = ON;\n-- Permite comparar planos de execução antes/depois de mudanças",
         "benefit": "Detecta regressões de plano de execução automaticamente.",
         "explanation": "Query Store grava histórico de planos de execução e métricas de performance, permitindo identificar quando e por que uma query piorou (plan regression) e até forçar um plano anterior."},
        {"icon": "🔏", "title": "Always Encrypted / Dynamic Data Masking", "category": "Segurança", "difficulty": "Avançado",
         "description": "Proteja dados sensíveis (CPF, cartão) em repouso e em uso.",
         "bad_code": "CREATE TABLE Clientes (\n    CPF CHAR(11),  -- armazenado e visível em texto puro para qualquer consulta\n    CartaoCredito VARCHAR(20)\n);",
         "good_code": "ALTER TABLE Clientes\nALTER COLUMN CPF CHAR(11)\nMASKED WITH (FUNCTION = 'partial(0,\"XXX.XXX.XXX-\",2)');\n-- Always Encrypted protege a coluna mesmo do DBA, cifrando no cliente",
         "benefit": "Reduz exposição de dados sensíveis mesmo para administradores.",
         "explanation": "Dynamic Data Masking oculta parte do valor para usuários sem permissão; Always Encrypted vai além, cifrando o dado no lado do cliente para que nem o SQL Server veja o valor em texto puro."},
        {"icon": "⚙️", "title": "Parametrização e Plan Cache", "category": "Performance", "difficulty": "Avançado",
         "description": "SQL dinâmico não parametrizado polui o plan cache.",
         "bad_code": "-- Cada valor de filtro gera uma string SQL diferente, sem reuso de plano\nEXEC('SELECT * FROM Pedidos WHERE ClienteID = ' + @id);",
         "good_code": "EXEC sp_executesql\n    N'SELECT * FROM Pedidos WHERE ClienteID = @ClienteID',\n    N'@ClienteID INT', @ClienteID = @id;",
         "benefit": "Reutiliza planos de execução compilados, menos overhead de compilação.",
         "explanation": "Queries parametrizadas geram um único plano reutilizável no cache; queries concatenadas com valores literais geram um plano novo a cada execução (plan cache bloat), desperdiçando memória e CPU."},
        {"icon": "🧮", "title": "Colunas Computadas Persistidas", "category": "T-SQL Moderno", "difficulty": "Avançado",
         "description": "Pré-calcule valores derivados e indexe-os.",
         "bad_code": "SELECT *, Quantidade * PrecoUnitario AS ValorTotal\nFROM ItensPedido;\n-- recalculado a cada consulta",
         "good_code": "ALTER TABLE ItensPedido\nADD ValorTotal AS (Quantidade * PrecoUnitario) PERSISTED;\nCREATE INDEX IX_ItensPedido_ValorTotal ON ItensPedido (ValorTotal);",
         "benefit": "Valor calculado uma vez e indexável.",
         "explanation": "PERSISTED armazena fisicamente o valor computado, permitindo criar índice sobre ele — algo impossível em uma coluna computada não persistida."},
    ]

    filtered = sqlserver_practices
    if selected_difficulty != "Todas":
        filtered = [p for p in filtered if p["difficulty"] == selected_difficulty]
    if search:
        filtered = [p for p in filtered if search.lower() in p["title"].lower()]

    st.markdown('<h3 class="section-header">📖 Melhores Práticas</h3>', unsafe_allow_html=True)
    st.markdown(f'**Mostrando {len(filtered)} de {len(sqlserver_practices)} práticas**')

    for idx, p in enumerate(filtered):
        is_learned = idx in st.session_state.sqlserver_learned
        is_favorite = idx in st.session_state.sqlserver_favorites

        with st.expander(f"{p['icon']} {p['title']} — {p['difficulty']}" + (" ✅" if is_learned else "") + (" ⭐" if is_favorite else ""), expanded=False):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**Descrição:** {p['description']}")
                st.markdown(f"**Benefício:** {p['benefit']}")
                st.markdown(f"**Categoria:** `{p['category']}`")
            with col2:
                if is_favorite:
                    if st.button("★ Favoritado", key=f"sqlserver_fav_{idx}"):
                        st.session_state.sqlserver_favorites.discard(idx)
                        st.session_state.sqlserver_points -= 5
                        st.session_state.sqlserver_xp -= 5
                        st.rerun()
                elif st.button("⭐ Favoritar", key=f"sqlserver_fav_{idx}"):
                    st.session_state.sqlserver_favorites.add(idx)
                    st.session_state.sqlserver_points += 5
                    st.session_state.sqlserver_xp += 5
                    st.rerun()
                if is_learned:
                    st.button("✅ Aprendida", key=f"sqlserver_learn_{idx}", disabled=True)
                elif st.button("✅ Aprendida", key=f"sqlserver_learn_{idx}"):
                    st.session_state.sqlserver_learned.add(idx)
                    st.session_state.sqlserver_points += 25
                    st.session_state.sqlserver_xp += 25
                    st.rerun()

            st.markdown("**❌ Evitar:**")
            st.code(p["bad_code"], language="sql")
            st.markdown("**✅ Preferir:**")
            st.code(p["good_code"], language="sql")
            st.markdown(f"**Explicação:** {p['explanation']}")

# ============================================================================
# TAB 2: EDITOR SQL SERVER (T-SQL) INTERATIVO
# ============================================================================
with tab2:
    st.markdown('<h2 class="section-header">✏️ Editor T-SQL Interativo</h2>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color: #7b8ba8; margin-bottom: 10px; font-weight:300;">'
        'Escreva e execute consultas SQL sobre um banco de exemplo em memória. '
        '<span style="color:#a78bfa;">Atenção:</span> o motor de execução aqui é SQLite, usado como '
        'aproximação didática — sintaxes exclusivas do T-SQL (<code>TOP</code> com parênteses, '
        '<code>GETDATE()</code>, <code>MERGE</code>, cursors, variáveis <code>@</code>, procedures) '
        'não executam de verdade neste sandbox, mas os conceitos das práticas acima valem para o SQL Server real.</p>',
        unsafe_allow_html=True,
    )

    @st.cache_resource
    def get_sqlserver_demo_connection():
        conn = sqlite3.connect(":memory:", check_same_thread=False)
        clientes_df = pd.DataFrame({
            "ClienteID": [1, 2, 3, 4, 5],
            "Nome": ["Alice Silva", "Bruno Santos", "Carla Oliveira", "Diego Costa", "Elaine Pereira"],
            "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador"],
            "Segmento": ["Varejo", "Corporate", "Varejo", "Private", "Varejo"],
        })
        clientes_df.to_sql("Clientes", conn, index=False, if_exists="replace")

        pedidos_df = pd.DataFrame({
            "PedidoID": [1, 2, 3, 4, 5, 6],
            "ClienteID": [1, 2, 1, 3, 2, 5],
            "ValorTotal": [150.00, 200.00, 75.50, 300.00, 120.00, 450.00],
            "Status": ["Concluido", "Concluido", "Pendente", "Concluido", "Cancelado", "Concluido"],
            "DataPedido": ["2024-01-10", "2024-01-15", "2024-02-01", "2024-02-10", "2024-02-15", "2024-03-01"],
        })
        pedidos_df.to_sql("Pedidos", conn, index=False, if_exists="replace")

        produtos_df = pd.DataFrame({
            "ProdutoID": [1, 2, 3, 4],
            "Nome": ["Notebook", "Monitor", "Teclado", "Mouse"],
            "Categoria": ["Eletrônicos", "Eletrônicos", "Periféricos", "Periféricos"],
            "Preco": [3500.00, 899.00, 199.00, 89.00],
        })
        produtos_df.to_sql("Produtos", conn, index=False, if_exists="replace")
        return conn

    def executar_query_sqlserver(query: str):
        try:
            query = query.strip()
            if not query:
                return None, "❌ Escreva uma query SQL primeiro!"
            conn = get_sqlserver_demo_connection()
            df = pd.read_sql_query(query, conn)
            return df, f"✅ Query executada com sucesso! {len(df)} registros retornados."
        except sqlite3.OperationalError as e:
            return None, f"❌ Erro SQL: {str(e)}"
        except Exception as e:
            return None, f"❌ Erro: {str(e)}"

    sqlserver_templates = {
        "SELECT Básico": "SELECT * FROM Produtos LIMIT 10;",
        "WHERE Filtro": "SELECT ProdutoID, Nome, Preco FROM Produtos WHERE Categoria = 'Periféricos';",
        "COUNT Agregação": "SELECT COUNT(*) AS TotalProdutos FROM Produtos;",
        "GROUP BY": "SELECT Categoria, COUNT(*) AS Total FROM Produtos GROUP BY Categoria;",
        "JOIN Tabelas": "SELECT c.Nome, p.ValorTotal FROM Clientes c INNER JOIN Pedidos p ON c.ClienteID = p.ClienteID LIMIT 5;",
        "ORDER BY": "SELECT ClienteID, Nome FROM Clientes ORDER BY Nome ASC;",
        "SUM com Agregação": "SELECT ClienteID, SUM(ValorTotal) AS TotalGasto FROM Pedidos GROUP BY ClienteID;",
        "LEFT JOIN": "SELECT c.ClienteID, c.Nome, COUNT(p.PedidoID) AS TotalPedidos FROM Clientes c LEFT JOIN Pedidos p ON c.ClienteID = p.ClienteID GROUP BY c.ClienteID, c.Nome;",
        "CTE (WITH)": "WITH TotaisPorCliente AS (\n    SELECT ClienteID, SUM(ValorTotal) AS Total\n    FROM Pedidos\n    GROUP BY ClienteID\n)\nSELECT * FROM TotaisPorCliente WHERE Total > 100;",
        "Window Function": "SELECT *,\n    ROW_NUMBER() OVER (PARTITION BY ClienteID ORDER BY DataPedido DESC) AS rn\nFROM Pedidos;",
        "EXISTS": "SELECT * FROM Clientes c WHERE EXISTS (SELECT 1 FROM Pedidos p WHERE p.ClienteID = c.ClienteID);",
        "BETWEEN": "SELECT * FROM Pedidos WHERE ValorTotal BETWEEN 100 AND 300;",
    }

    st.markdown('<div class="editor-section">', unsafe_allow_html=True)
    col_template, col_editor = st.columns([1, 2], gap="large")

    with col_template:
        st.markdown('<p class="editor-title">📚 Templates</p>', unsafe_allow_html=True)
        selected_template = st.selectbox(
            "Escolha um exemplo:",
            ["Escrever Manual"] + list(sqlserver_templates.keys()),
            key="sqlserver_template_select",
            label_visibility="collapsed",
        )
        template_query = sqlserver_templates.get(selected_template, "") if selected_template != "Escrever Manual" else ""

    with col_editor:
        st.markdown('<p class="editor-title">📝 Seu T-SQL</p>', unsafe_allow_html=True)
        user_query = st.text_area(
            "Escreva sua query:",
            value=template_query,
            height=160,
            key="sqlserver_editor",
            placeholder="SELECT * FROM Produtos;",
            label_visibility="collapsed",
        )
    st.markdown('</div>', unsafe_allow_html=True)

    run_button_sql = st.button("▶️ EXECUTAR", key="sqlserver_run")

    st.markdown('<h2 class="section-header">📊 Resultado da Query</h2>', unsafe_allow_html=True)
    col_result, col_info = st.columns([2, 1], gap="large")

    with col_result:
        if run_button_sql and user_query.strip():
            st.session_state.sqlserver_editor_runs += 1
            st.session_state.sqlserver_xp += 5
            st.session_state.sqlserver_points += 5
            result_df, message = executar_query_sqlserver(user_query)
            if "✅" in message:
                st.markdown(f'<div class="success-box achievement-pop">{message}</div>', unsafe_allow_html=True)
                if result_df is not None and len(result_df) > 0:
                    st.dataframe(result_df, use_container_width=True)
                else:
                    st.info("Query executada, mas nenhum resultado foi retornado.")
            else:
                st.markdown(f'<div class="error-box">{message}</div>', unsafe_allow_html=True)
        elif run_button_sql and not user_query.strip():
            st.markdown('<div class="error-box">❌ Digite uma query antes de executar!</div>', unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 40px; color: #2d3748;">
                <p style="font-size: 1rem;">📝 Escreva uma query no editor e clique em EXECUTAR para ver o resultado</p>
            </div>
            """, unsafe_allow_html=True)

    with col_info:
        st.markdown("""
        <div class="info-panel">
            <p class="info-panel-title">ℹ️ Tabelas & Dicas</p>
            <p style="color: #7b8ba8; font-size: 0.85rem; line-height: 1.8; margin-bottom: 16px; font-weight:300;">
                <span style="color:#e2e8f0; font-weight:600;">Clientes:</span> ClienteID, Nome, Cidade, Segmento
                <br><br>
                <span style="color:#e2e8f0; font-weight:600;">Pedidos:</span> PedidoID, ClienteID, ValorTotal, Status, DataPedido
                <br><br>
                <span style="color:#e2e8f0; font-weight:600;">Produtos:</span> ProdutoID, Nome, Categoria, Preco
            </p>
            <p style="color: #2d3748; font-size: 0.82rem; font-weight:300; border-top: 1px solid rgba(167,139,250,0.1); padding-top: 14px;">
                💡 Cada execução vale +5 XP. Teste SELECT, WITH (CTE), window functions, JOIN, GROUP BY e mais!
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# TAB 3: DESAFIOS
# ============================================================================
with tab3:
    st.markdown('<h3 class="section-header">🎯 Desafios Semanais</h3>', unsafe_allow_html=True)
    st.markdown("Complete desafios para ganhar XP e subir de nível!")

    for challenge in CHALLENGES:
        is_completed = challenge["id"] in st.session_state.sqlserver_challenges_completed
        col1, col2 = st.columns([4, 1])
        with col1:
            status = "✅ Completo" if is_completed else f"🎯 {challenge['difficulty']}"
            st.markdown(f"""
            <div class="challenge-box {'challenge-completed' if is_completed else ''}">
                <h4>{challenge['title']} {status}</h4>
                <p>{challenge['description']}</p>
                <p><strong>Recompensa:</strong> +{challenge['xp_reward']} XP</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if not is_completed:
                if st.button("Marcar ✓", key=f"sqlserver_challenge_{challenge['id']}"):
                    st.session_state.sqlserver_challenges_completed.add(challenge["id"])
                    st.session_state.sqlserver_xp += challenge["xp_reward"]
                    st.session_state.sqlserver_points += challenge["xp_reward"]
                    st.rerun()

# ============================================================================
# TAB 4: BADGES
# ============================================================================
with tab4:
    st.markdown('<h3 class="section-header">🏆 Suas Conquistas</h3>', unsafe_allow_html=True)

    learned_count = len(st.session_state.sqlserver_learned)
    favorites_count = len(st.session_state.sqlserver_favorites)
    current_badges = check_badges(learned_count, favorites_count, st.session_state.sqlserver_editor_runs, st.session_state.sqlserver_points)
    st.session_state.sqlserver_badges = current_badges

    st.markdown(f"""
    ### 📊 Estatísticas
    - **Práticas Aprendidas:** {learned_count}/30
    - **Práticas Favoritadas:** {favorites_count}
    - **Queries Executadas:** {st.session_state.sqlserver_editor_runs}
    - **Pontos Totais:** {st.session_state.sqlserver_points}
    - **XP Total:** {st.session_state.sqlserver_xp}
    """)

    unlocked = [(bid, bi) for bid, bi in BADGES.items() if bid in st.session_state.sqlserver_badges]
    locked = [(bid, bi) for bid, bi in BADGES.items() if bid not in st.session_state.sqlserver_badges]

    st.markdown("### 🎖️ Badges Desbloqueados")
    if unlocked:
        cols = st.columns(5)
        for idx, (badge_id, badge_info) in enumerate(unlocked):
            with cols[idx % 5]:
                st.markdown(f'<div class="badge">{badge_info["icon"]}<br><small><b>{badge_info["title"]}</b></small></div>', unsafe_allow_html=True)
    else:
        st.caption("Nenhum badge desbloqueado ainda — comece completando práticas!")

    st.markdown("### 🔒 Badges Bloqueados")
    if locked:
        cols = st.columns(5)
        for idx, (badge_id, badge_info) in enumerate(locked):
            with cols[idx % 5]:
                st.markdown(f'<div class="badge badge-locked">{badge_info["icon"]}<br><small>{badge_info["title"]}</small><br><span style="font-size: 0.7rem;">{badge_info["description"]}</span></div>', unsafe_allow_html=True)

# ============================================================================
# TAB 5: PERFIL
# ============================================================================
with tab5:
    st.markdown('<h3 class="section-header">📊 Seu Perfil</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        ### 🏆 Estatísticas Gerais
        - **Nível Atual:** {current_level}/{len(MASTERY_LEVELS)}
        - **Título:** {MASTERY_LEVELS[current_level]['title']}
        - **XP Total:** {st.session_state.sqlserver_xp}
        - **Pontos:** {st.session_state.sqlserver_points}
        - **Streak:** 🔥 {st.session_state.sqlserver_streak} dias
        """)
    with col2:
        learned_count = len(st.session_state.sqlserver_learned)
        st.markdown(f"""
        ### 📚 Progresso no Aprendizado
        - **Práticas Completadas:** {learned_count}/30
        - **Taxa de Conclusão:** {(learned_count/30)*100:.1f}%
        - **Favoritas:** {len(st.session_state.sqlserver_favorites)}
        - **Queries Testadas:** {st.session_state.sqlserver_editor_runs}
        - **Badges:** {len(st.session_state.sqlserver_badges)}/{len(BADGES)}
        """)

    st.divider()
    st.markdown("### 🎯 Próximas Metas")
    if current_level < 5:
        next_level_xp = get_xp_for_next_level(current_level)
        xp_needed = next_level_xp - st.session_state.sqlserver_xp
        next_title = MASTERY_LEVELS[current_level + 1]["title"]
        st.markdown(f"""
        ⬆️ **Próximo Nível:** {next_title}

        Você precisa de **{xp_needed} XP** para chegar ao próximo nível!
        """)
    else:
        st.markdown("🏆 **Você é um SQL Server Elite! Parabéns!**")

    st.divider()
    st.markdown("""
    ### 💪 Dicas para Evoluir Rápido
    1. **Complete Desafios:** +50-200 XP cada
    2. **Teste no Editor:** +5 XP por execução
    3. **Favoritize Práticas:** +5 XP cada
    4. **Marque Aprendidas:** +25 XP cada
    5. **Mantenha Streak:** Use a plataforma todos os dias!

    **Meta:** Chegue ao nível SQL Server Elite (🏆) em 30 dias!
    """)
