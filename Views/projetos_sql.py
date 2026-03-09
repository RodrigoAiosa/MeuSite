import streamlit as st
from utils import exibir_rodape, registrar_acesso

# --- CONFIGURAÇÃO DE PÁGINA ---
st.set_page_config(
    page_title="SQL - Melhores Práticas | Rodrigo Aiosa",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- REGISTRO DE ACESSO ---
registrar_acesso("SQL - Melhores Práticas")

# --- ESTILO CSS ---
st.markdown(
    """
    <style>
    .hero-container {
        background: linear-gradient(135deg, #111827 0%, #0f172a 100%);
        padding: 40px;
        border-radius: 20px;
        border-left: 5px solid #10b981;
        margin-bottom: 40px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 15px;
    }
    .hero-text {
        font-size: 1.1rem;
        color: #9ca3af;
        line-height: 1.6;
    }
    .hero-highlight {
        color: #10b981;
        font-weight: bold;
    }
    .practice-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .practice-card:hover {
        border-color: #10b981;
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.15);
    }
    .practice-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 15px;
        flex-wrap: wrap;
        gap: 10px;
    }
    .practice-icon {
        font-size: 2rem;
    }
    .practice-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #ffffff;
        flex-grow: 1;
    }
    .practice-difficulty {
        font-size: 0.75rem;
        font-weight: 900;
        padding: 4px 12px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .difficulty-iniciante {
        background-color: rgba(34, 197, 94, 0.2);
        color: #22c55e;
    }
    .difficulty-intermediario {
        background-color: rgba(245, 158, 11, 0.2);
        color: #f59e0b;
    }
    .difficulty-avancado {
        background-color: rgba(239, 68, 68, 0.2);
        color: #ef4444;
    }
    .practice-description {
        color: #9ca3af;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 15px;
    }
    .practice-category {
        display: inline-block;
        background-color: rgba(16, 185, 129, 0.15);
        color: #10b981;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 8px;
    }
    .code-block {
        background-color: #0f172a;
        border-left: 3px solid #10b981;
        padding: 15px;
        border-radius: 8px;
        margin-top: 15px;
        overflow-x: auto;
    }
    .code-text {
        color: #d1d5db;
        font-family: monospace;
        font-size: 0.9rem;
        line-height: 1.5;
        white-space: pre-wrap;
        word-break: break-word;
    }
    .practice-benefit {
        background-color: rgba(16, 185, 129, 0.08);
        border-left: 3px solid #10b981;
        padding: 12px;
        border-radius: 6px;
        margin-top: 15px;
        color: #d1d5db;
        font-size: 0.9rem;
    }
    .benefit-title {
        color: #10b981;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 15px;
        margin-bottom: 30px;
    }
    .stat-box {
        background-color: #111827;
        border: 1px solid #1f2937;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: 800;
        color: #10b981;
    }
    .stat-label {
        color: #9ca3af;
        font-size: 0.85rem;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- SEÇÃO ESTRATÉGICA ---
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">🗄️ SQL: A Fundação da Inteligência de Dados</div>
        <div class="hero-text">
            <p><strong>Dados bem estruturados geram insights poderosos:</strong></p>
            <ol>
                <li>Queries eficientes são a base de <span class="hero-highlight">dashboards que escalam</span>.</li>
                <li>Boas práticas em SQL reduzem tempo de processamento e <span class="hero-highlight">amplificam a precisão das análises</span>.</li>
                <li><strong>Logo,</strong> dominar SQL estratégico é <span class="hero-highlight">não negociável para analistas e gestores de dados</span>.</li>
            </ol>
            <p>Conhecimento é poder. Dados transformados em ação. 🚀</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- TITLE ---
st.markdown("<h1 style='text-align: center; font-size: 3rem;'>🗄️ SQL - Melhores Práticas</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 1.05rem;'>Estratégias avançadas para queries eficientes, escaláveis e precisas</p>", unsafe_allow_html=True)

st.write("")

# --- STATS ---
st.markdown(
    """
    <div class="stats-container">
        <div class="stat-box">
            <div class="stat-number">16</div>
            <div class="stat-label">Práticas Documentadas</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">3</div>
            <div class="stat-label">Níveis de Dificuldade</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">5</div>
            <div class="stat-label">Categorias</div>
        </div>
        <div class="stat-box">
            <div class="stat-number">∞</div>
            <div class="stat-label">Aplicações Reais</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

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

st.write("")

# --- FILTROS ---
st.markdown("<h3 style='color: #ffffff;'>🔎 Filtrar Práticas</h3>", unsafe_allow_html=True)

col_cat, col_dif = st.columns(2)

with col_cat:
    categorias = ["Todas"] + sorted(list(set([p["category"] for p in sql_practices])))
    selected_category = st.selectbox("Categoria", categorias, key="category_filter")

with col_dif:
    dificuldades = ["Todas", "Iniciante", "Intermediário", "Avançado"]
    selected_difficulty = st.selectbox("Nível de Dificuldade", dificuldades, key="difficulty_filter")

# --- APLICAR FILTROS ---
filtered_practices = sql_practices

if selected_category != "Todas":
    filtered_practices = [p for p in filtered_practices if p["category"] == selected_category]

if selected_difficulty != "Todas":
    filtered_practices = [p for p in filtered_practices if p["difficulty"] == selected_difficulty]

# --- RENDERIZAR CARDS ---
st.write("")
st.markdown(f"<p style='color: #9ca3af;'>📌 Mostrando <span style='color: #10b981; font-weight: bold;'>{len(filtered_practices)}</span> de {len(sql_practices)} práticas</p>", unsafe_allow_html=True)
st.write("")

for practice in filtered_practices:
    difficulty_class = "difficulty-iniciante" if practice["difficulty"] == "Iniciante" else \
                       "difficulty-intermediario" if practice["difficulty"] == "Intermediário" else \
                       "difficulty-avancado"
    
    st.markdown(
        f"""
        <div class="practice-card">
            <div class="practice-header">
                <div class="practice-icon">{practice['icon']}</div>
                <div class="practice-title">{practice['title']}</div>
                <div class="practice-difficulty {difficulty_class}">{practice['difficulty']}</div>
            </div>
            
            <div class="practice-category">{practice['category']}</div>
            
            <div class="practice-description">{practice['description']}</div>
            
            <div style="background-color: #0f172a; padding: 15px; border-radius: 8px; margin-top: 15px;">
                <div style="color: #9ca3af; font-size: 0.85rem; margin-bottom: 10px; font-weight: 600;">CONTEXTO:</div>
                <div style="color: #d1d5db; font-size: 0.9rem; line-height: 1.5;">{practice['context']}</div>
            </div>
            
            <div style="color: #10b981; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-top: 15px; margin-bottom: 10px;">Evitar:</div>
            <div class="code-block">
                <div class="code-text">{practice['bad_query']}</div>
            </div>
            
            <div style="color: #10b981; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-top: 15px; margin-bottom: 10px;">Fazer:</div>
            <div class="code-block">
                <div class="code-text">{practice['good_query']}</div>
            </div>
            
            <div class="practice-benefit">
                <div class="benefit-title">Beneficio:</div>
                <div>{practice['benefit']}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- SEÇÃO FINAL ---
st.write("")
st.markdown(
    """
    <div style='background-color: #111827; border: 1px solid #10b981; border-radius: 12px; padding: 25px; text-align: center;'>
        <div style='font-size: 1.3rem; font-weight: 700; color: #ffffff; margin-bottom: 10px;'>Quer Levar Suas Queries para o Proximo Nivel?</div>
        <div style='color: #9ca3af; font-size: 0.95rem; line-height: 1.6;'>
            Consultoria em SQL estrategico para transformar dados em vantagem competitiva.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

try:
    exibir_rodape()
except Exception as e:
    print(f"Erro ao exibir rodape: {e}")
