import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="SQL - Melhores Práticas | Rodrigo Aiosa",
    page_icon="🗄️",
    layout="wide"
)

# --- REGISTRO DE ACESSO ---
registrar_acesso("SQL - Melhores Práticas")

# --- TÍTULO ---
st.title("🗄️ SQL - Melhores Práticas")
st.markdown("Estratégias avançadas para queries eficientes, escaláveis e precisas")

st.divider()

# --- INTRODUÇÃO ---
st.header("💡 Por que SQL estratégico importa?")
col1, col2, col3 = st.columns(3)
col1.metric("Práticas", "16", "documentadas")
col2.metric("Categorias", "5", "de conhecimento")
col3.metric("Impacto", "∞", "aplicações reais")

st.markdown("""
Queries eficientes são a base de dashboards que escalam. Boas práticas em SQL reduzem tempo de processamento e amplificam a precisão das análises.
""")

st.divider()

# --- DATABASE DE PRÁTICAS SQL ---
sql_practices = [
    {
        "icon": "⚡",
        "title": "Usar INDEXES Estrategicamente",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "Índices aceleram buscas, mas desaceleram inserts/updates.",
        "bad_query": "SELECT * FROM usuarios WHERE email = 'test@mail.com';",
        "good_query": "CREATE INDEX idx_usuarios_email ON usuarios(email);\nSELECT id, nome FROM usuarios WHERE email = 'test@mail.com';",
        "benefit": "Reduz tempo de busca O(n) para O(log n).",
        "context": "Use em WHERE clauses, JOINs e ORDER BY."
    },
    {
        "icon": "🔍",
        "title": "Evitar SELECT *",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Selecione apenas as colunas necessárias.",
        "bad_query": "SELECT * FROM vendas WHERE ano = 2024;",
        "good_query": "SELECT id, produto, valor, data_venda FROM vendas WHERE ano = 2024;",
        "benefit": "Reduz bandwidth de rede, acelera processamento.",
        "context": "Impacto exponencial em sistemas com muitos dados."
    },
    {
        "icon": "📊",
        "title": "Usar JOINs em vez de Subconsultas",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "JOINs são geralmente mais rápidos.",
        "bad_query": "SELECT id, nome FROM usuarios WHERE id IN (SELECT usuario_id FROM vendas WHERE ano = 2024);",
        "good_query": "SELECT DISTINCT u.id, u.nome FROM usuarios u INNER JOIN vendas v ON u.id = v.usuario_id WHERE v.ano = 2024;",
        "benefit": "JOINs usam índices melhor.",
        "context": "Crítico com muitos registros."
    },
    {
        "icon": "🚀",
        "title": "Particionar Grandes Tabelas",
        "category": "Performance",
        "difficulty": "Avançado",
        "description": "Divida tabelas por critério (data, região).",
        "bad_query": "SELECT * FROM eventos WHERE data >= '2024-01-01';",
        "good_query": "CREATE TABLE eventos_202401 PARTITION OF eventos FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');",
        "benefit": "Melhora performance em 10x+.",
        "context": "Use com tabelas maiores que 100GB."
    },
    {
        "icon": "✅",
        "title": "Tratar NULL Explicitamente",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "NULL não é zero nem string vazia.",
        "bad_query": "SELECT SUM(comissao) FROM vendas WHERE status = 'concluida';",
        "good_query": "SELECT SUM(COALESCE(comissao, 0)) FROM vendas WHERE status = 'concluida' AND comissao IS NOT NULL;",
        "benefit": "Evita resultados inesperados.",
        "context": "Crítico em cálculos financeiros."
    },
    {
        "icon": "🎯",
        "title": "Window Functions para Ranking",
        "category": "Lógica & Precisão",
        "difficulty": "Avançado",
        "description": "Calcule rank, running total sem subconsultas.",
        "bad_query": "SELECT id, nome, (SELECT COUNT(*) FROM usuarios WHERE created_at < u.created_at) AS rank FROM usuarios u;",
        "good_query": "SELECT id, nome, ROW_NUMBER() OVER (ORDER BY created_at) AS rank FROM usuarios;",
        "benefit": "Código legível, performance superior.",
        "context": "Ótimo para ranking e moving averages."
    },
    {
        "icon": "🔗",
        "title": "Validar com Constraints",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Use PRIMARY KEY, FOREIGN KEY, CHECK.",
        "bad_query": "CREATE TABLE vendas (id INT, valor FLOAT, usuario_id INT);",
        "good_query": "CREATE TABLE vendas (id INT PRIMARY KEY, valor FLOAT CHECK (valor > 0), usuario_id INT NOT NULL REFERENCES usuarios(id));",
        "benefit": "Previne dados inválidos na origem.",
        "context": "Essencial em sistemas críticos."
    },
    {
        "icon": "🧹",
        "title": "Normalizar em ETL",
        "category": "Dados & Limpeza",
        "difficulty": "Intermediário",
        "description": "Padronize formatos, remova duplicatas.",
        "bad_query": "SELECT TRIM(nome), COUNT(*) FROM usuarios WHERE email != '' GROUP BY TRIM(nome);",
        "good_query": "WITH clean_users AS (SELECT DISTINCT TRIM(LOWER(nome)) AS nome FROM raw_usuarios WHERE email IS NOT NULL) SELECT nome, COUNT(*) FROM clean_users GROUP BY nome;",
        "benefit": "Queries mais rápidas, dados confiáveis.",
        "context": "Use CTEs para ETL."
    },
    {
        "icon": "📈",
        "title": "CTEs para Modularidade",
        "category": "Dados & Limpeza",
        "difficulty": "Intermediário",
        "description": "Quebre queries complexas em etapas.",
        "bad_query": "SELECT u.nome, SUM(CASE WHEN v.status='concluida' THEN v.valor ELSE 0 END) FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id WHERE u.created_at > '2024-01-01' GROUP BY u.id;",
        "good_query": "WITH usuarios_recentes AS (SELECT id, nome FROM usuarios WHERE created_at > '2024-01-01') SELECT u.nome FROM usuarios_recentes u;",
        "benefit": "Código legível, fácil testabilidade.",
        "context": "Padrão ouro em análise de dados."
    },
    {
        "icon": "⚙️",
        "title": "Desnormalizar para OLAP",
        "category": "Dados & Limpeza",
        "difficulty": "Avançado",
        "description": "Duplicar dados para análise acelera queries.",
        "bad_query": "SELECT v.id, u.nome, p.nome, c.nome, v.valor FROM vendas v JOIN usuarios u ON v.usuario_id = u.id JOIN produtos p ON v.produto_id = p.id JOIN categorias c ON p.categoria_id = c.id;",
        "good_query": "CREATE TABLE vendas_denorm AS SELECT v.id, u.nome, p.nome, c.nome, v.valor FROM vendas v JOIN usuarios u ON v.usuario_id = u.id JOIN produtos p ON v.produto_id = p.id;",
        "benefit": "Queries muito mais rápidas.",
        "context": "OLTP normalizado, OLAP desnormalizado."
    },
    {
        "icon": "🔐",
        "title": "Prepared Statements",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Parameterize queries contra SQL Injection.",
        "bad_query": "query = f\"SELECT * FROM usuarios WHERE email = '{user_email}'\"",
        "good_query": "query = \"SELECT * FROM usuarios WHERE email = %s\"\ncursor.execute(query, (user_email,))",
        "benefit": "Impede ataques de segurança.",
        "context": "Obrigatório em produção."
    },
    {
        "icon": "📋",
        "title": "Documentar Queries",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Comente queries complexas.",
        "bad_query": "SELECT u.id, COUNT(DISTINCT v.id) FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id GROUP BY u.id;",
        "good_query": "-- Query: Contagem de vendas por usuário\n-- Propósito: Dashboard de Engagement\nSELECT u.id, u.nome, COUNT(DISTINCT v.id) AS total_vendas FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id GROUP BY u.id;",
        "benefit": "Fácil handoff e manutenção.",
        "context": "Um comentário economiza horas."
    },
    {
        "icon": "🛡️",
        "title": "Transactions (ACID)",
        "category": "Segurança & Manutenção",
        "difficulty": "Intermediário",
        "description": "Agrupe operações em transações.",
        "bad_query": "UPDATE contas SET saldo = saldo - 100 WHERE id = 1;\nUPDATE contas SET saldo = saldo + 100 WHERE id = 2;",
        "good_query": "BEGIN TRANSACTION;\nUPDATE contas SET saldo = saldo - 100 WHERE id = 1;\nUPDATE contas SET saldo = saldo + 100 WHERE id = 2;\nCOMMIT;",
        "benefit": "Impede data corruption.",
        "context": "Essencial em operações financeiras."
    },
    {
        "icon": "📊",
        "title": "EXPLAIN/ANALYZE",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Inspecione o plano de execução.",
        "bad_query": "SELECT * FROM vendas WHERE usuario_id = 123;",
        "good_query": "EXPLAIN ANALYZE\nSELECT * FROM vendas WHERE usuario_id = 123;",
        "benefit": "Identifica se usa índices.",
        "context": "Ferramenta imprescindível."
    },
    {
        "icon": "🎯",
        "title": "Pivotear com CASE WHEN",
        "category": "Análise de Dados",
        "difficulty": "Intermediário",
        "description": "Transforme linhas em colunas.",
        "bad_query": "SELECT mes, categoria, SUM(vendas) FROM vendas_agrupadas GROUP BY mes, categoria;",
        "good_query": "SELECT mes,\n  SUM(CASE WHEN categoria = 'A' THEN vendas ELSE 0 END) AS categ_a,\n  SUM(CASE WHEN categoria = 'B' THEN vendas ELSE 0 END) AS categ_b\nFROM vendas_agrupadas\nGROUP BY mes;",
        "benefit": "Facilita comparações.",
        "context": "Ideal para Excel/BI."
    },
    {
        "icon": "🔄",
        "title": "Recursion para Hierarquias",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Navegue estruturas hierárquicas.",
        "bad_query": "SELECT * FROM categorias WHERE categoria_pai_id IS NULL;",
        "good_query": "WITH RECURSIVE categoria_tree AS (\n  SELECT id, nome, categoria_pai_id, 0 AS nivel FROM categorias WHERE categoria_pai_id IS NULL\n  UNION ALL\n  SELECT c.id, c.nome, c.categoria_pai_id, ct.nivel + 1 FROM categorias c JOIN categoria_tree ct ON c.categoria_pai_id = ct.id\n)\nSELECT * FROM categoria_tree ORDER BY nivel;",
        "benefit": "Simplifica navegação.",
        "context": "Para organograma e estruturas."
    }
]

# --- FILTROS ---
st.header("🔎 Filtrar Práticas")

col1, col2 = st.columns(2)

with col1:
    categorias = ["Todas"] + sorted(list(set([p["category"] for p in sql_practices])))
    selected_category = st.selectbox("Categoria", categorias, key="category_filter")

with col2:
    dificuldades = ["Todas", "Iniciante", "Intermediário", "Avançado"]
    selected_difficulty = st.selectbox("Nível de Dificuldade", dificuldades, key="difficulty_filter")

# --- APLICAR FILTROS ---
filtered_practices = sql_practices

if selected_category != "Todas":
    filtered_practices = [p for p in filtered_practices if p["category"] == selected_category]

if selected_difficulty != "Todas":
    filtered_practices = [p for p in filtered_practices if p["difficulty"] == selected_difficulty]

# --- RENDERIZAR PRÁTICAS ---
st.divider()
st.write(f"📌 Mostrando **{len(filtered_practices)}** de **{len(sql_practices)}** práticas")
st.divider()

for idx, practice in enumerate(filtered_practices, 1):
    with st.expander(f"{practice['icon']} {practice['title']} — {practice['difficulty']}", expanded=False):
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.write(f"**Categoria:** {practice['category']}")
            st.write(f"**Descrição:** {practice['description']}")
            st.write(f"**Contexto:** {practice['context']}")
        
        with col2:
            st.write(f"**Benefício:** {practice['benefit']}")
        
        st.divider()
        
        st.write("❌ **EVITAR:**")
        st.code(practice['bad_query'], language='sql')
        
        st.write("✅ **FAZER:**")
        st.code(practice['good_query'], language='sql')

st.divider()

st.info("💡 **Essas práticas são apenas o começo.** Consultoria em SQL estratégico para transformar seus dados em vantagem competitiva.")

exibir_rodape()
