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
    # INICIANTE (20+)
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
        "icon": "🎓",
        "title": "Usar LIMIT em Development",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Sempre limitar resultados em queries de teste.",
        "bad_query": "SELECT * FROM usuarios;",
        "good_query": "SELECT * FROM usuarios LIMIT 100;",
        "benefit": "Evita lentidão ao testar em prod.",
        "context": "Development vs Production."
    },
    {
        "icon": "📍",
        "title": "WHERE antes de JOINs",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Filtre antes de juntar tabelas.",
        "bad_query": "SELECT * FROM vendas v JOIN usuarios u ON v.usuario_id = u.id WHERE v.ano = 2024;",
        "good_query": "SELECT * FROM vendas v JOIN usuarios u ON v.usuario_id = u.id WHERE v.ano = 2024;",
        "benefit": "Reduz volume processado.",
        "context": "Boas práticas de query."
    },
    {
        "icon": "🔤",
        "title": "Maiúsculas em SQL Keywords",
        "category": "Dados & Limpeza",
        "difficulty": "Iniciante",
        "description": "Use maiúsculas em SELECT, FROM, WHERE.",
        "bad_query": "select id, nome from usuarios where ativo = true;",
        "good_query": "SELECT id, nome FROM usuarios WHERE ativo = true;",
        "benefit": "Legibilidade, padrão da indústria.",
        "context": "Code style."
    },
    {
        "icon": "👥",
        "title": "Usar Aliases em JOINs",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Dê nomes curtos às tabelas.",
        "bad_query": "SELECT usuarios.id, vendas.valor FROM usuarios JOIN vendas ON usuarios.id = vendas.usuario_id;",
        "good_query": "SELECT u.id, v.valor FROM usuarios u JOIN vendas v ON u.id = v.usuario_id;",
        "benefit": "Query mais legível e compacta.",
        "context": "Padrão obrigatório em queries."
    },
    {
        "icon": "📊",
        "title": "GROUP BY com Agregação",
        "category": "Análise de Dados",
        "difficulty": "Iniciante",
        "description": "Sempre usar COUNT, SUM em GROUP BY.",
        "bad_query": "SELECT usuario_id, status FROM vendas GROUP BY usuario_id, status;",
        "good_query": "SELECT usuario_id, status, COUNT(*) AS total FROM vendas GROUP BY usuario_id, status;",
        "benefit": "Resultado com contexto numérico.",
        "context": "Análises de negócio."
    },
    {
        "icon": "🔍",
        "title": "DISTINCT para Remover Duplicatas",
        "category": "Dados & Limpeza",
        "difficulty": "Iniciante",
        "description": "Use DISTINCT quando necessário.",
        "bad_query": "SELECT email FROM usuarios;",
        "good_query": "SELECT DISTINCT email FROM usuarios;",
        "benefit": "Valores únicos apenas.",
        "context": "Limpeza de dados."
    },
    {
        "icon": "⏱️",
        "title": "Date Format Consistente",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Use ISO 8601 (YYYY-MM-DD).",
        "bad_query": "WHERE data = '01/03/2024';",
        "good_query": "WHERE data = '2024-03-01';",
        "benefit": "Sem ambiguidade de formatação.",
        "context": "Padrão internacional."
    },
    {
        "icon": "🚫",
        "title": "Evitar UPDATE Sem WHERE",
        "category": "Segurança & Manutenção",
        "difficulty": "Iniciante",
        "description": "Sempre especifique condição.",
        "bad_query": "UPDATE usuarios SET ativo = false;",
        "good_query": "UPDATE usuarios SET ativo = false WHERE deletado_em IS NOT NULL;",
        "benefit": "Evita atualizar toda a tabela.",
        "context": "Proteção contra erros."
    },
    {
        "icon": "📌",
        "title": "ORDER BY para Paginação",
        "category": "Performance",
        "difficulty": "Iniciante",
        "description": "Use ORDER BY com LIMIT.",
        "bad_query": "SELECT * FROM usuarios LIMIT 10;",
        "good_query": "SELECT * FROM usuarios ORDER BY created_at DESC LIMIT 10;",
        "benefit": "Resultado consistente.",
        "context": "Paginação em aplicações."
    },
    {
        "icon": "🎯",
        "title": "ILIKE para Case-Insensitive",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "PostgreSQL: use ILIKE.",
        "bad_query": "WHERE email = 'TEST@MAIL.COM';",
        "good_query": "WHERE email ILIKE 'test@mail.com';",
        "benefit": "Busca sem considerar maiúsculas.",
        "context": "PostgreSQL specific."
    },
    {
        "icon": "📐",
        "title": "Validar Tipos de Dados",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Verifique tipos ao importar.",
        "bad_query": "INSERT INTO vendas (valor) VALUES ('abc');",
        "good_query": "INSERT INTO vendas (valor) VALUES (123.45);",
        "benefit": "Evita erros de tipo.",
        "context": "Data validation."
    },
    {
        "icon": "🔗",
        "title": "INNER vs LEFT JOIN",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "INNER: ambas existem. LEFT: primeira.",
        "bad_query": "SELECT * FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id;",
        "good_query": "SELECT * FROM usuarios u INNER JOIN vendas v ON u.id = v.usuario_id;",
        "benefit": "Evita NULLs desnecessários.",
        "context": "Escolha do JOIN correto."
    },
    {
        "icon": "🧮",
        "title": "CAST para Conversão",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Converta tipos explicitamente.",
        "bad_query": "SELECT price + '5' FROM products;",
        "good_query": "SELECT price + CAST('5' AS INT) FROM products;",
        "benefit": "Operações seguras.",
        "context": "Type casting."
    },
    {
        "icon": "⚠️",
        "title": "HAVING para Filtrar GROUP BY",
        "category": "Análise de Dados",
        "difficulty": "Iniciante",
        "description": "Use HAVING após GROUP BY.",
        "bad_query": "SELECT usuario_id, COUNT(*) FROM vendas WHERE COUNT(*) > 5 GROUP BY usuario_id;",
        "good_query": "SELECT usuario_id, COUNT(*) FROM vendas GROUP BY usuario_id HAVING COUNT(*) > 5;",
        "benefit": "Sintaxe correta e eficiente.",
        "context": "Agregação com condição."
    },
    {
        "icon": "🔀",
        "title": "UNION para Combinar Resultados",
        "category": "Dados & Limpeza",
        "difficulty": "Iniciante",
        "description": "Combine dois SELECTs.",
        "bad_query": "SELECT id FROM usuarios; SELECT id FROM clientes;",
        "good_query": "SELECT id FROM usuarios UNION SELECT id FROM clientes;",
        "benefit": "Um resultado combinado.",
        "context": "Combinação de datasets."
    },
    {
        "icon": "📊",
        "title": "COUNT(*) vs COUNT(coluna)",
        "category": "Análise de Dados",
        "difficulty": "Iniciante",
        "description": "COUNT(*) inclui NULLs.",
        "bad_query": "SELECT COUNT(email) FROM usuarios;",
        "good_query": "SELECT COUNT(*) FROM usuarios;",
        "benefit": "Conta correta de registros.",
        "context": "Agregação."
    },
    {
        "icon": "🎁",
        "title": "DEFAULT em CREATE TABLE",
        "category": "Lógica & Precisão",
        "difficulty": "Iniciante",
        "description": "Defina valores padrão.",
        "bad_query": "CREATE TABLE usuarios (id INT, ativo BOOLEAN);",
        "good_query": "CREATE TABLE usuarios (id INT, ativo BOOLEAN DEFAULT true);",
        "benefit": "Menos NULLs inesperados.",
        "context": "Schema design."
    },

    # INTERMEDIÁRIO (20+)
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
        "icon": "🔍",
        "title": "LIKE com Pattern Matching",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Use % e _ para buscas parciais.",
        "bad_query": "SELECT * FROM usuarios WHERE nome = 'Maria';",
        "good_query": "SELECT * FROM usuarios WHERE nome LIKE 'Maria%';",
        "benefit": "Buscas flexíveis.",
        "context": "Full-text search básico."
    },
    {
        "icon": "⏸️",
        "title": "Batch Processing",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "Processe em lotes, não um por um.",
        "bad_query": "FOR each row: INSERT INTO log VALUES (row);",
        "good_query": "INSERT INTO log SELECT * FROM staging;",
        "benefit": "Performance em 100x.",
        "context": "Bulk operations."
    },
    {
        "icon": "🔀",
        "title": "LEFT JOIN com NULL Check",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Identifique registros sem match.",
        "bad_query": "SELECT u.id FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id;",
        "good_query": "SELECT u.id FROM usuarios u LEFT JOIN vendas v ON u.id = v.usuario_id WHERE v.id IS NULL;",
        "benefit": "Encontra registros órfãos.",
        "context": "Data reconciliation."
    },
    {
        "icon": "📊",
        "title": "SUM + CASE para Condicional",
        "category": "Análise de Dados",
        "difficulty": "Intermediário",
        "description": "Soma condicional.",
        "bad_query": "SELECT SUM(valor) FROM vendas WHERE status = 'pago';",
        "good_query": "SELECT SUM(CASE WHEN status = 'pago' THEN valor ELSE 0 END) FROM vendas;",
        "benefit": "Flexibilidade em agregação.",
        "context": "Análises complexas."
    },
    {
        "icon": "🎓",
        "title": "Usar COALESCE para NULLs",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Substitua NULLs por padrão.",
        "bad_query": "SELECT desconto FROM vendas;",
        "good_query": "SELECT COALESCE(desconto, 0) FROM vendas;",
        "benefit": "Evita cálculos com NULL.",
        "context": "Data cleaning."
    },
    {
        "icon": "🔢",
        "title": "BETWEEN para Ranges",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "Mais eficiente que AND.",
        "bad_query": "SELECT * FROM vendas WHERE data >= '2024-01-01' AND data <= '2024-12-31';",
        "good_query": "SELECT * FROM vendas WHERE data BETWEEN '2024-01-01' AND '2024-12-31';",
        "benefit": "Sintaxe mais clara.",
        "context": "Range queries."
    },
    {
        "icon": "⚡",
        "title": "Index Compostos para Multi-Coluna",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "Índices em múltiplas colunas.",
        "bad_query": "CREATE INDEX idx_user ON vendas(usuario_id);\nCREATE INDEX idx_status ON vendas(status);",
        "good_query": "CREATE INDEX idx_user_status ON vendas(usuario_id, status);",
        "benefit": "Melhor performance em queries com AND.",
        "context": "Index strategy."
    },
    {
        "icon": "🎯",
        "title": "IN com Subconsulta",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Filtre por resultados de query.",
        "bad_query": "SELECT * FROM usuarios WHERE id IN (1, 2, 3, 4, 5);",
        "good_query": "SELECT * FROM usuarios WHERE id IN (SELECT user_id FROM premium_users);",
        "benefit": "Dinâmico e escalável.",
        "context": "Filtros complexos."
    },
    {
        "icon": "📌",
        "title": "NOT IN com Cuidado",
        "category": "Performance",
        "difficulty": "Intermediário",
        "description": "NOT IN ignora NULLs, use NOT EXISTS.",
        "bad_query": "SELECT * FROM usuarios WHERE id NOT IN (SELECT user_id FROM bloqueados);",
        "good_query": "SELECT * FROM usuarios u WHERE NOT EXISTS (SELECT 1 FROM bloqueados b WHERE b.user_id = u.id);",
        "benefit": "Comportamento esperado.",
        "context": "NULL handling."
    },
    {
        "icon": "🔀",
        "title": "CROSS JOIN para Combinações",
        "category": "Análise de Dados",
        "difficulty": "Intermediário",
        "description": "Produto cartesiano.",
        "bad_query": "SELECT * FROM cidades, produtos;",
        "good_query": "SELECT * FROM cidades CROSS JOIN produtos;",
        "benefit": "Sintaxe explícita.",
        "context": "Combinações todas."
    },
    {
        "icon": "📊",
        "title": "GROUP BY com HAVING",
        "category": "Análise de Dados",
        "difficulty": "Intermediário",
        "description": "Filtre grupos por agregação.",
        "bad_query": "SELECT usuario_id, COUNT(*) FROM vendas GROUP BY usuario_id;",
        "good_query": "SELECT usuario_id, COUNT(*) AS total FROM vendas GROUP BY usuario_id HAVING COUNT(*) > 10;",
        "benefit": "Filtra após agregação.",
        "context": "Análise de dados."
    },
    {
        "icon": "🎯",
        "title": "CAST para Data/Hora",
        "category": "Lógica & Precisão",
        "difficulty": "Intermediário",
        "description": "Converta string para date.",
        "bad_query": "SELECT * FROM vendas WHERE data = '2024-03-08';",
        "good_query": "SELECT * FROM vendas WHERE CAST(data AS DATE) = '2024-03-08';",
        "benefit": "Comparação correta.",
        "context": "Type conversion."
    },

    # AVANÇADO (20+)
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
        "icon": "📊",
        "title": "EXPLAIN/ANALYZE",
        "category": "Otimização",
        "difficulty": "Avançado",
        "description": "Inspecione o plano de execução.",
        "bad_query": "SELECT * FROM vendas WHERE usuario_id = 123;",
        "good_query": "EXPLAIN ANALYZE\nSELECT * FROM vendas WHERE usuario_id = 123;",
        "benefit": "Identifica se usa índices.",
        "context": "Ferramenta imprescindível."
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
    },
    {
        "icon": "📈",
        "title": "Row_Number, Rank, Dense_Rank",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Diferentes formas de ranking.",
        "bad_query": "SELECT id, COUNT(*) FROM vendas GROUP BY id;",
        "good_query": "SELECT id, ROW_NUMBER() OVER (ORDER BY valor DESC) AS row_num, RANK() OVER (ORDER BY valor DESC) AS rank FROM vendas;",
        "benefit": "Ranking flexível.",
        "context": "Analytics avançado."
    },
    {
        "icon": "🎯",
        "title": "LAG e LEAD para Comparação",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Compare com linha anterior/próxima.",
        "bad_query": "SELECT data, valor FROM vendas ORDER BY data;",
        "good_query": "SELECT data, valor, LAG(valor) OVER (ORDER BY data) AS prev_valor, LEAD(valor) OVER (ORDER BY data) AS next_valor FROM vendas;",
        "benefit": "Análise temporal.",
        "context": "Time series analysis."
    },
    {
        "icon": "🔀",
        "title": "PARTITION BY em Window Functions",
        "category": "Análise de Dados",
        "difficulty": "Avançado",
        "description": "Window functions por grupo.",
        "bad_query": "SELECT usuario_id, SUM(valor) FROM vendas GROUP BY usuario_id;",
        "good_query": "SELECT usuario_id, valor, SUM(valor) OVER (PARTITION BY usuario_id) AS total_user FROM vendas;",
        "benefit": "Agregação sem perder detalhes.",
        "context": "Advanced analytics."
    },
    {
        "icon": "⚡",
        "title": "Materialized Views",
        "category": "Performance",
        "difficulty": "Avançado",
        "description": "Cache de queries complexas.",
        "bad_query": "SELECT * FROM vendas WHERE ano = 2024;",
        "good_query": "CREATE MATERIALIZED VIEW vendas_2024 AS SELECT * FROM vendas WHERE ano = 2024;\nREFRESH MATERIALIZED VIEW vendas_2024;",
        "benefit": "Queries pré-calculadas.",
        "context": "Performance otimizada."
    },
    {
        "icon": "🔐",
        "title": "Row-Level Security",
        "category": "Segurança & Manutenção",
        "difficulty": "Avançado",
        "description": "Controle de acesso por linha.",
        "bad_query": "SELECT * FROM usuarios;",
        "good_query": "CREATE POLICY user_policy ON usuarios USING (usuario_atual = current_user);",
        "benefit": "Segurança de dados.",
        "context": "Multi-tenant systems."
    },
    {
        "icon": "📊",
        "title": "CUBE para Análise Multi-Dimensional",
        "category": "Otimização",
        "difficulty": "Avançado",
        "description": "Agregações em todas as combinações.",
        "bad_query": "SELECT categoria, regiao, SUM(vendas) FROM vendas GROUP BY categoria, regiao;",
        "good_query": "SELECT categoria, regiao, SUM(vendas) FROM vendas GROUP BY CUBE(categoria, regiao);",
        "benefit": "Análise multi-dimensional.",
        "context": "OLAP cubes."
    },
    {
        "icon": "🎓",
        "title": "ROLLUP para Agregação Hierárquica",
        "category": "Otimização",
        "difficulty": "Avançado",
        "description": "Agregações por níveis.",
        "bad_query": "SELECT ano, mes, dia, SUM(vendas) FROM vendas GROUP BY ano, mes, dia;",
        "good_query": "SELECT ano, mes, dia, SUM(vendas) FROM vendas GROUP BY ROLLUP(ano, mes, dia);",
        "benefit": "Totalizações automáticas.",
        "context": "Hierarchical aggregation."
    },
    {
        "icon": "🔄",
        "title": "Temporal Tables para Auditoria",
        "category": "Monitoramento",
        "difficulty": "Avançado",
        "description": "Rastreie histórico de dados.",
        "bad_query": "UPDATE usuarios SET email = 'new@mail.com' WHERE id = 1;",
        "good_query": "CREATE TABLE usuarios_history (id, email, valid_from, valid_to);\nUPDATE usuarios SET email = 'new@mail.com' WHERE id = 1;",
        "benefit": "Auditoria completa.",
        "context": "Compliance requirements."
    },
    {
        "icon": "⚙️",
        "title": "JSON Functions para Dados Semiestruturados",
        "category": "Arquitetura",
        "difficulty": "Avançado",
        "description": "Trabalhe com JSON no SQL.",
        "bad_query": "SELECT * FROM usuarios;",
        "good_query": "SELECT data->>'nome', data->'endereco'->>'cidade' FROM usuarios;",
        "benefit": "Flexibilidade estrutural.",
        "context": "NoSQL in SQL."
    },
    {
        "icon": "📈",
        "title": "Full-Text Search",
        "category": "Performance",
        "difficulty": "Avançado",
        "description": "Busca textual otimizada.",
        "bad_query": "SELECT * FROM artigos WHERE conteudo LIKE '%postgres%';",
        "good_query": "SELECT * FROM artigos WHERE to_tsvector(conteudo) @@ plainto_tsquery('postgres');",
        "benefit": "Busca semântica rápida.",
        "context": "Text search advanced."
    },
    {
        "icon": "🎯",
        "title": "Array Functions",
        "category": "Arquitetura",
        "difficulty": "Avançado",
        "description": "Trabalhe com arrays no PostgreSQL.",
        "bad_query": "SELECT tags FROM posts;",
        "good_query": "SELECT tags FROM posts WHERE 'sql' = ANY(tags);",
        "benefit": "Dados estruturados flexíveis.",
        "context": "PostgreSQL specific."
    },
    {
        "icon": "🔐",
        "title": "Encryption at Rest",
        "category": "Segurança & Manutenção",
        "difficulty": "Avançado",
        "description": "Criptografe dados sensíveis.",
        "bad_query": "INSERT INTO usuarios (email, ssn) VALUES ('test@mail.com', '123-45-6789');",
        "good_query": "INSERT INTO usuarios (email, ssn) VALUES ('test@mail.com', pgp_sym_encrypt('123-45-6789', 'key'));",
        "benefit": "Proteção de dados.",
        "context": "Security compliance."
    },
    {
        "icon": "📊",
        "title": "Approximate Aggregate Functions",
        "category": "Otimização",
        "difficulty": "Avançado",
        "description": "Aproximações rápidas de counts.",
        "bad_query": "SELECT COUNT(DISTINCT usuario_id) FROM vendas;",
        "good_query": "SELECT approx_distinct(usuario_id) FROM vendas;",
        "benefit": "Performance dramática.",
        "context": "BigData scenarios."
    },
    {
        "icon": "⏱️",
        "title": "Query Timeout Strategy",
        "category": "Monitoramento",
        "difficulty": "Avançado",
        "description": "Configure timeout para queries.",
        "bad_query": "SELECT * FROM tabela_gigante;",
        "good_query": "SET statement_timeout = '5s';\nSELECT * FROM tabela_gigante LIMIT 1000;",
        "benefit": "Evita lock-ups.",
        "context": "Production safety."
    },
    {
        "icon": "🎓",
        "title": "Connection Pooling",
        "category": "Arquitetura",
        "difficulty": "Avançado",
        "description": "Reutilize conexões.",
        "bad_query": "# Criar nova conexão a cada query",
        "good_query": "# Usar PgBouncer ou similar para pool",
        "benefit": "Escalabilidade.",
        "context": "System architecture."
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
