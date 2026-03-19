import streamlit as st
import psycopg2
from datetime import datetime, timedelta, timezone

st.title("🔧 Debug — Conexão Supabase")

# ── 1. Verifica secrets ──────────────────────────────────────
st.subheader("1. Secrets configurados?")

chaves = ["SUPABASE_HOST", "SUPABASE_DB", "SUPABASE_USER", "SUPABASE_PASSWORD", "SUPABASE_PORT"]
tudo_ok = True

for chave in chaves:
    valor = st.secrets.get(chave, None)
    if valor:
        # Mostra só os 4 primeiros caracteres por segurança
        st.success(f"✅ {chave} = {str(valor)[:4]}***")
    else:
        st.error(f"❌ {chave} — NÃO ENCONTRADO!")
        tudo_ok = False

# ── 2. Testa conexão ────────────────────────────────────────
st.subheader("2. Conexão com o banco")

if tudo_ok:
    try:
        conn = psycopg2.connect(
            host=st.secrets.get("SUPABASE_HOST"),
            database=st.secrets.get("SUPABASE_DB"),
            user=st.secrets.get("SUPABASE_USER"),
            password=st.secrets.get("SUPABASE_PASSWORD"),
            port=st.secrets.get("SUPABASE_PORT"),
            sslmode="require",
            connect_timeout=5,
        )
        st.success("✅ Conexão estabelecida com sucesso!")

        # ── 3. Verifica tabela ───────────────────────────────
        st.subheader("3. Tabela registros_acesso existe?")
        cur = conn.cursor()
        cur.execute("""
            SELECT COUNT(*) FROM information_schema.tables
            WHERE table_name = 'registros_acesso';
        """)
        existe = cur.fetchone()[0]

        if existe:
            st.success("✅ Tabela encontrada!")

            # ── 4. Testa INSERT ──────────────────────────────
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
                st.info("⚠️ Rode o ver_tabela.py para ver o registro, depois limpe com limpar_tabela.py")
            except Exception as e:
                st.error(f"❌ Erro no INSERT: {e}")
        else:
            st.error("❌ Tabela NÃO encontrada! Crie a tabela no Supabase.")

        cur.close()
        conn.close()

    except Exception as e:
        st.error(f"❌ Falha na conexão: {e}")
else:
    st.warning("⚠️ Corrija os secrets antes de testar a conexão.")

# ── 5. Headers do usuário ────────────────────────────────────
st.subheader("5. Headers HTTP (metadados do visitante)")
headers = st.context.headers
ua  = headers.get("User-Agent", "não encontrado")
ip  = headers.get("X-Forwarded-For", "não encontrado")
st.write(f"**User-Agent:** {ua}")
st.write(f"**IP:** {ip}")
