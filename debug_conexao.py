import streamlit as st
import psycopg2
from datetime import datetime, timedelta, timezone

st.title("🔧 Debug — Conexão Supabase")

SUPABASE_CONFIG = {
    "host":            "aws-1-us-east-1.pooler.supabase.com",
    "database":        "postgres",
    "user":            "postgres.hqkhtpwmciavtobsutph",
    "password":        st.secrets.get("SUPABASE_PASSWORD", ""),
    "port":            "5432",
    "sslmode":         "require",
    "connect_timeout": 10,
}

# ── 1. Verifica secret ───────────────────────────────────────
st.subheader("1. Secret configurado?")
senha = st.secrets.get("SUPABASE_PASSWORD", None)
if senha:
    st.success(f"✅ SUPABASE_PASSWORD = {str(senha)[:4]}***")
else:
    st.error("❌ SUPABASE_PASSWORD — NÃO ENCONTRADO!")
    st.stop()

# ── 2. Testa conexão ────────────────────────────────────────
st.subheader("2. Conexão com o banco (Session Pooler IPv4 — porta 5432)")
try:
    conn = psycopg2.connect(**SUPABASE_CONFIG)
    st.success("✅ Conexão estabelecida com sucesso!")
    cur = conn.cursor()

    # ── 3. Verifica tabela ───────────────────────────────────
    st.subheader("3. Tabela registros_acesso existe?")
    cur.execute("""
        SELECT COUNT(*) FROM information_schema.tables
        WHERE table_name = 'registros_acesso';
    """)
    existe = cur.fetchone()[0]

    if existe:
        st.success("✅ Tabela encontrada!")

        # ── 4. Testa INSERT ──────────────────────────────────
        st.subheader("4. Teste de INSERT")
        try:
            agora = datetime.now(timezone(timedelta(hours=-3)))
            cur.execute("""
                INSERT INTO registros_acesso
                    (data_hora, session_id, dispositivo, navegador, ip, pagina, acao, duracao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id;
            """, (agora, "DEBUG-001", "PC", "Chrome", "0.0.0.0", "debug", "Teste", "00:00"))
            id_gerado = cur.fetchone()[0]
            conn.commit()
            st.success(f"✅ INSERT OK — id gerado: {id_gerado}")
            st.info("⚠️ Rode o ver_tabela.py para confirmar, depois limpe com limpar_tabela.py")
        except Exception as e:
            st.error(f"❌ Erro no INSERT: {e}")
    else:
        st.error("❌ Tabela NÃO encontrada!")

    cur.close()
    conn.close()

except Exception as e:
    st.error(f"❌ Falha na conexão: {e}")

# ── 5. Headers do usuário ────────────────────────────────────
st.subheader("5. Headers HTTP (metadados do visitante)")
headers = st.context.headers
st.write(f"**User-Agent:** {headers.get('User-Agent', 'não encontrado')}")
st.write(f"**IP:** {headers.get('X-Forwarded-For', 'não encontrado')}")
