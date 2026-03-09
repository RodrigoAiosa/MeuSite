import streamlit as st
try:
    from utils import exibir_rodape, registrar_acesso
except ImportError:
    # Fallback se utils.py não estiver disponível
    def registrar_acesso(pagina):
        pass
    def exibir_rodape():
        st.markdown(
            """
            <hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'>
            <div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>
                SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
            </div>
            """, 
            unsafe_allow_html=True
        )

# --- REGISTRO DE ACESSO ---
try:
    registrar_acesso("SQL - Melhores Práticas")
except Exception as e:
    print(f"Aviso: Rastreamento desativado - {e}")

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
    
    /* Card de Prática SQL */
    .practice-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .practice-card:hover {
        border-color: #10b981;
        box-shadow: 0 8px 20px rgba(16, 185, 129, 0.15);
        transform: translateY(-2px);
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
    
    .code-header {
        color: #10b981;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 10px;
        letter-spacing: 0.5px;
    }
    
    .code-text {
        color: #d1d5db;
        font-family: 'Courier New', monospace;
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
    
    /* Stats Counter */
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
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """,
    unsafe_allow_html=True
)

# --- SEÇÃO ESTRATÉGICA ---
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-title">SQL: A Fundação da Inteligência de Dados</div>
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
    # PERFORMANCE
    {
        "id": 1,
        "icon": "⚡",
        "title": "Usar INDEXES Estrategicamente",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "Índices aceleram buscas, mas desaceleram inserts/updates. Use em colunas frequentemente filtradas.",
        "bad_query": "SELECT * FROM usuarios WHERE email = 'test@mail.com';",
        "good_query": "-- Criar índice\nCREATE INDEX idx_usuarios_email ON usuarios(email);\n\n-- Query otimizada\nSELECT id, nome FROM usuarios WHERE email = 'test@mail.com';",
        "benefit": "Reduz tempo de busca de O(n) para O(log n). Em tabelas com 1M+ registros, diferença é crítica.",
        "context": "Use em WHERE clauses, JOINs e ORDER BY frequentes. Evite colunas com alta cardinalidade baixa."
    },
    {
        "id": 2,
        "icon": "🔍",
        "title": "Evitar SELECT *",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Selecione apenas as colunas necessárias para reduzir transferência de dados.",
        "bad_query": "SELECT * FROM vendas WHERE ano = 2024;",
        "good_query": "SELECT id, produto, valor, data_venda \nFROM vendas \nWHERE ano = 2024;",
        "benefit": "Reduz bandwidth de rede, acelera processamento em memória, facilita índices cobertos (covered indexes).",
        "context": "Impacto exponencial em sistemas com muitas colunas ou dados volumosos. Standard em análise de dados."
    },
    {
        "id": 3,
        "icon": "📊",
        "title": "Usar JOINs em vez de Subconsultas",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "JOINs são geralmente mais rápidos. Subconsultas executam múltiplas vezes.",
        "bad_query": "SELECT id, nome FROM usuarios \nWHERE id IN (SELECT usuario_id FROM vendas WHERE ano = 2024);",
        "good_query": "SELECT DISTINCT u.id, u.nome \nFROM usuarios u\nINNER JOIN vendas v ON u.id = v.usuario_id\nWHERE v.ano = 2024;",
        "benefit": "JOINs usam índices. Subconsultas podem não ser otimizadas. Melhor plano de execução.",
        "context": "Especialmente crítico com muitos registros. Otimizadores modernos às vezes resolvem, mas melhor ser explícito."
    },
    {
        "id": 4,
        "icon": "🚀",
        "title": "Particionar Grandes Tabelas",
        "category": "Performance",
        "difficulty": "Avançado",
        "description": "Divida tabelas por critério (data, região) para queries mais rápidas e manutenção simplificada.",
        "bad_query": "-- Sem partição: scans 5 anos de dados\nSELECT * FROM eventos WHERE data >= '2024-01-01';",
        "good_query": "-- Particionar por mês\nCREATE TABLE eventos_202401 PARTITION OF eventos\n  FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');\n\n-- Query acessa apenas partição relevante\nSELECT * FROM eventos WHERE data >= '2024-01-01';",
        "benefit": "Melhora performance em 10x+. Simplifica backup/restore. Reduz tempo de manutenção.",
        "context": "Use com tabelas > 100GB. Timing baseado em frequência de acesso (diário, mensal, anual)."
    },
    
    # LÓGICA E PRECISÃO
    {
        "id": 5,
        "icon": "✅",
        "title": "Tratar NULL Explicitamente",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "NULL não é zero nem string vazia. Precisa tratamento especial com COALESCE ou CASE.",
        "bad_query": "SELECT SUM(comissao) FROM vendas WHERE status = 'concluida';",
        "good_query": "SELECT SUM(COALESCE(comissao, 0)) \nFROM vendas \nWHERE status = 'concluida' AND comissao IS NOT NULL;",
        "benefit": "Evita resultados inesperados. NULL + valor = NULL (erro comum). Precisão em cálculos críticos.",
        "context": "Crítico em cálculos financeiros. Se não tratar NULL, seu dashboard mostra dados incorretos."
    },
    {
        "id": 6,
        "icon": "🎯",
        "title": "Window Functions para Ranking e Agregações",
        "category": "Lógica & Precisão",
        "difficulty": "Avançado",
        "description": "Calcule rank, running total e moving averages sem subconsultas complexas.",
        "bad_query": "-- Subconsulta aninhada (confuso, lento)\nSELECT id, nome, \n(SELECT COUNT(*) FROM usuarios WHERE created_at < u.created_at) AS rank\nFROM usuarios u;",
        "good_query": "SELECT id, nome,\nROW_NUMBER() OVER (ORDER BY created_at) AS rank,\nSUM(vendas) OVER (ORDER BY data ROWS BETWEEN 30 PRECEDING AND CURRENT ROW) AS venda_30d\nFROM usuarios;",
        "benefit": "Código mais legível, performance superior, cálculos complexos simplificados.",
        "context": "Excelente para análises: ranking, running totals, moving averages, YoY comparisons."
    },
    {
        "id": 7,
        "icon": "🔗",
        "title": "Validar Integridade com Constraints",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Use PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK para garantir dados válidos no nível do banco.",
        "bad_query": "-- Sem constraints: dados inválidos entram\nCREATE TABLE vendas (id INT, valor FLOAT, usuario_id INT);",
        "good_query": "CREATE TABLE vendas (\n  id INT PRIMARY KEY,\n  valor FLOAT CHECK (valor > 0),\n  usuario_id INT NOT NULL,\n  FOREIGN KEY (usuario_id) REFERENCES usuarios(id),\n  UNIQUE(id)\n);",
        "benefit": "Previne dados inválidos na origem. Reduz bugs de aplicação. Economiza tempo de limpeza.",
        "context": "Essencial em sistemas críticos (financeiro, RH). Constraints capturam erros antes de queries erradas."
    },
    
    # DADOS E LIMPEZA
    {
        "id": 8,
        "icon": "🧹",
        "title": "Normalizar Dados em ETL",
        "category": "Dados & Limpeza",
        "difficulty": "Intermediário",
        "description": "Padronize formatos, remova duplicatas e outliers na extração, não na análise.",
        "bad_query": "-- Query de análise carregada de limpeza\nSELECT TRIM(nome), COUNT(*) \nFROM usuarios \nWHERE email != '' AND email NOT LIKE '%invalid%'\nGROUP BY TRIM(nome);",
        "good_query": "-- Pipeline ETL limpo\nWITH clean_users AS (\n  SELECT DISTINCT TRIM(LOWER(nome)) AS nome, email\n  FROM raw_usuarios\n  WHERE email IS NOT NULL AND email LIKE '%@%.%'\n)\nSELECT nome, COUNT(*) \nFROM clean_users\nGROUP BY nome;",
        "benefit": "Queries mais rápidas. Dados confiáveis. Fácil reuso em múltiplos dashboards.",
        "context": "Use CTEs (WITH) para ETL. Separe lógica de extração da análise."
    },
    {
        "id": 9,
        "icon": "📈",
        "title": "Usar CTEs (Common Table Expressions) para Modularidade",
        "category": "Dados & Limpeza",
        "difficulty": "Intermediário",
        "description": "Quebre queries complexas em etapas lógicas com WITH clauses.",
        "bad_query": "-- Query monolítica (impossível debugar)\nSELECT u.nome, SUM(CASE WHEN v.status='concluida' THEN v.valor ELSE 0 END) \nFROM usuarios u\nLEFT JOIN vendas v ON u.id = v.usuario_id\nWHERE u.created_at > '2024-01-01' AND v.data BETWEEN '2024-01-01' AND '2024-03-31'\nGROUP BY u.id, u.nome;",
        "good_query": "WITH usuarios_recentes AS (\n  SELECT id, nome FROM usuarios WHERE created_at > '2024-01-01'\n),\nvendas_trimestre AS (\n  SELECT usuario_id, SUM(valor) AS total\n  FROM vendas\n  WHERE status = 'concluida' AND data BETWEEN '2024-01-01' AND '2024-03-31'\n  GROUP BY usuario_id\n)\nSELECT u.nome, COALESCE(v.total, 0) AS vendas_3m\nFROM usuarios_recentes u\nLEFT JOIN vendas_trimestre v ON u.id = v.usuario_id;",
        "benefit": "Código legível. Fácil testabilidade. Identificar gargalos. Reutilizar CTEs.",
        "context": "Padrão ouro em análise de dados. Cada CTE = um step lógico."
    },
    {
        "id": 10,
        "icon": "⚙️",
        "title": "Desnormalizar Estrategicamente (Denormalization)",
        "category": "Dados & Limpeza",
        "difficulty": "Avançado",
        "description": "Às vezes, duplicar dados na estrutura acelera queries (análise vs. OLTP).",
        "bad_query": "-- 5 JOINs: lento para análise frequente\nSELECT v.id, u.nome, p.nome, c.nome, v.valor\nFROM vendas v\nJOIN usuarios u ON v.usuario_id = u.id\nJOIN produtos p ON v.produto_id = p.id\nJOIN categorias c ON p.categoria_id = c.id;",
        "good_query": "-- Tabela desnormalizada (data warehouse)\nCREATE TABLE vendas_denorm AS\nSELECT v.id, u.nome, p.nome, c.nome, v.valor\nFROM vendas v\nJOIN usuarios u ON v.usuario_id = u.id\nJOIN produtos p ON v.produto_id = p.id\nJOIN categorias c ON p.categoria_id = c.id;\n\n-- Query simples e rápida\nSELECT * FROM vendas_denorm WHERE ano = 2024;",
        "benefit": "Queries muito mais rápidas. Ideal para data warehouses (OLAP).",
        "context": "OLTP usa normalização (muitos JOINs, transações). OLAP usa denormalização (queries big, poucas inserções)."
    },
    
    # SEGURANÇA E MANUTENÇÃO
    {
        "id": 11,
        "icon": "🔐",
        "title": "Usar Prepared Statements para SQL Injection",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Parameterize queries para evitar injeção de SQL malicioso.",
        "bad_query": "-- PERIGOSO: SQL Injection\nquery = f\"SELECT * FROM usuarios WHERE email = '{user_email}'\"\n-- Se user_email = \"' OR '1'='1\" → acessa TODOS os usuários!",
        "good_query": "-- Seguro: Prepared Statement\nquery = \"SELECT * FROM usuarios WHERE email = %s\"\ncursor.execute(query, (user_email,))\n\n-- Parameterizado: %s, ?, @param (depende do DB)",
        "benefit": "Impede ataques de segurança. Padrão obrigatório em produção.",
        "context": "Sempre use prepared statements em aplicações web/mobile. Nunca concatene strings em SQL."
    },
    {
        "id": 12,
        "icon": "📋",
        "title": "Documentar Queries e Criar Dicionário de Dados",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Comente queries complexas e mantenha documentação das tabelas.",
        "bad_query": "SELECT u.id, COUNT(DISTINCT v.id) \nFROM usuarios u\nLEFT JOIN vendas v ON u.id = v.usuario_id\nWHERE u.created_at > '2024-01-01'\nGROUP BY u.id;",
        "good_query": "-- Query: Contagem de vendas por usuário (últimos 3 meses)\n-- Propósito: Dashboard de Engagement\n-- Owner: Rodrigo (data@empresa.com)\n-- Última atualização: 2024-03-08\n\nSELECT \n  u.id,\n  u.nome,\n  COUNT(DISTINCT v.id) AS total_vendas\nFROM usuarios u\nLEFT JOIN vendas v ON u.id = v.usuario_id\n  AND v.data > CURRENT_DATE - INTERVAL 3 MONTH\nWHERE u.created_at > '2024-01-01'\nGROUP BY u.id, u.nome;",
        "benefit": "Fácil handoff. Novos membros entendem lógica. Manutenção simplificada.",
        "context": "Crítico em equipes. Um comentário economiza horas de investigação."
    },
    {
        "id": 13,
        "icon": "🛡️",
        "title": "Usar Transactions (ACID) para Consistência",
        "category": "Segurança & Manutenção",
        "difficulty": "Intermediário",
        "description": "Agrupe operações relacionadas em transações para garantir tudo suceda ou tudo falhe.",
        "bad_query": "-- Sem transaction: débito realizado mas crédito falha\nUPDATE contas SET saldo = saldo - 100 WHERE id = 1;\nUPDATE contas SET saldo = saldo + 100 WHERE id = 2;",
        "good_query": "BEGIN TRANSACTION;\n\nUPDATE contas SET saldo = saldo - 100 WHERE id = 1;\nUPDATE contas SET saldo = saldo + 100 WHERE id = 2;\n\nCOMMIT; -- Ambas acontecem\n-- Ou ROLLBACK; em caso de erro",
        "benefit": "Impede data corruption. Essencial para operações financeiras.",
        "context": "ACID = Atomicity, Consistency, Isolation, Durability. Não negocie em sistemas críticos."
    },
    
    # ANÁLISE DE DADOS
    {
        "id": 14,
        "icon": "📊",
        "title": "Usar EXPLAIN/ANALYZE para Debugar Performance",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Inspecione o plano de execução para identificar gargalos.",
        "bad_query": "SELECT * FROM vendas WHERE usuario_id = 123;",
        "good_query": "EXPLAIN ANALYZE\nSELECT * FROM vendas WHERE usuario_id = 123;\n\n-- Output mostra:\n-- Seq Scan: scan sequencial (sem índice)\n-- Index Scan: usando índice (rápido)\n-- Cost: estimativa de tempo relativo",
        "benefit": "Identifica se query está usando índices. Optimiza slow queries.",
        "context": "Ferramenta imprescindível. EXPLAIN ANALYZE em produção com cuidado (usa recursos)."
    },
    {
        "id": 15,
        "icon": "🎯",
        "title": "Pivotear Dados com CASE WHEN vs. PIVOT",
        "category": "Análise de Dados",
        "difficulty": "Intermediário",
        "description": "Transforme linhas em colunas para análises cross-dimensionais.",
        "bad_query": "-- Resultado: muitas linhas, difícil comparar\nSELECT mes, categoria, SUM(vendas) \nFROM vendas_agrupadas\nGROUP BY mes, categoria;",
        "good_query": "-- Pivotado: comparação fácil\nSELECT mes,\n  SUM(CASE WHEN categoria = 'A' THEN vendas ELSE 0 END) AS categ_a,\n  SUM(CASE WHEN categoria = 'B' THEN vendas ELSE 0 END) AS categ_b,\n  SUM(CASE WHEN categoria = 'C' THEN vendas ELSE 0 END) AS categ_c\nFROM vendas_agrupadas\nGROUP BY mes;",
        "benefit": "Facilita comparações. Reduz linhas no resultado. Ideal para Excel/BI.",
        "context": "PIVOT sintaxe varia por DB (SQL Server, Oracle). CASE WHEN é portável."
    },
    {
        "id": 16,
        "icon": "🔄",
        "title": "Usar Recursion para Hierarquias",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Navegue estruturas hierárquicas (organograma, categorias aninhadas) com CTEs recursivas.",
        "bad_query": "-- Sem recursão: precisa de múltiplas queries\nSELECT * FROM categorias WHERE categoria_pai_id IS NULL;",
        "good_query": "WITH RECURSIVE categoria_tree AS (\n  -- Âncora: categorias raiz\n  SELECT id, nome, categoria_pai_id, 0 AS nivel\n  FROM categorias\n  WHERE categoria_pai_id IS NULL\n  \n  UNION ALL\n  \n  -- Recursão: subcategorias\n  SELECT c.id, c.nome, c.categoria_pai_id, ct.nivel + 1\n  FROM categorias c\n  JOIN categoria_tree ct ON c.categoria_pai_id = ct.id\n)\nSELECT * FROM categoria_tree ORDER BY nivel, nome;",
        "benefit": "Simplifica navegação hierárquica. Evita múltiplas queries.",
        "context": "Organograma, estrutura de custos, árbol de produto. Poderoso mas exige cuidado (ciclos)."
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
                <div style="color: #9ca3af; font-size: 0.85rem; margin-bottom: 10px; font-weight: 600;">📍 CONTEXTO:</div>
                <div style="color: #d1d5db; font-size: 0.9rem; line-height: 1.5;">{practice['context']}</div>
            </div>
            
            <div style="color: #10b981; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-top: 15px; margin-bottom: 10px; letter-spacing: 0.5px;">❌ Evitar:</div>
            <div class="code-block">
                <div class="code-text">{practice['bad_query']}</div>
            </div>
            
            <div style="color: #10b981; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-top: 15px; margin-bottom: 10px; letter-spacing: 0.5px;">✅ Fazer:</div>
            <div class="code-block">
                <div class="code-text">{practice['good_query']}</div>
            </div>
            
            <div class="practice-benefit">
                <div class="benefit-title">💡 Benefício:</div>
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
        <div style='font-size: 1.3rem; font-weight: 700; color: #ffffff; margin-bottom: 10px;'>💬 Quer Levar Suas Queries para o Próximo Nível?</div>
        <div style='color: #9ca3af; font-size: 0.95rem; line-height: 1.6;'>
            Essas práticas são apenas o começo. Consultoria em SQL estratégico para transformar seus dados em vantagem competitiva.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

try:
    exibir_rodape()
except Exception as e:
    st.markdown(
        f"""
        <hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'>
        <div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
        """, 
        unsafe_allow_html=True
    )
