import streamlit as st
import psycopg2
import uuid
import streamlit.components.v1 as components
from datetime import datetime, timedelta, timezone

# --- INICIALIZAÇÃO SEGURA ---
def inicializar_estado():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())[:8]
    if "entrada_pagina" not in st.session_state:
        # Define horário de Brasília (-3)
        st.session_state["entrada_pagina"] = datetime.now(timezone(timedelta(hours=-3)))
    if "id_acesso_db" not in st.session_state:
        st.session_state["id_acesso_db"] = None
    if "leu_ate_o_fim" not in st.session_state:
        st.session_state["leu_ate_o_fim"] = False

# Chamamos a inicialização imediatamente
inicializar_estado()

# --- CONEXÃO COM BD_SKYDATA ---
def get_db_connection():
    """Conecta ao banco PostgreSQL no Aiven usando Secrets."""
    return psycopg2.connect(
        host=st.secrets["DB_HOST"],
        port=st.secrets["DB_PORT"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASS"],
        sslmode="require"
    )

def calcular_duracao_texto():
    """Calcula o tempo decorrido desde a entrada em formato HH:MM:SS para o Postgres."""
    agora = datetime.now(timezone(timedelta(hours=-3)))
    delta = agora - st.session_state["entrada_pagina"]
    segundos_totais = int(delta.total_seconds())
    horas = segundos_totais // 3600
    minutos = (segundos_totais % 3600) // 60
    segundos = segundos_totais % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

# --- NOVA FUNÇÃO DE REGISTRO NO BANCO ---
def registrar_acesso_db(nome_pagina, acao="Visualização"):
    """Registra o acesso na tabela controle_acesso_site do BD_SKYDATA."""
    try:
        # Só registra se for um novo acesso na sessão ou mudança de página
        if st.session_state["id_acesso_db"] is None:
            headers = st.context.headers
            ua = headers.get("User-Agent", "").lower()
            ip = headers.get("X-Forwarded-For", "Privado").split(",")[0]
            
            # Detecção de Dispositivo e Navegador
            dispositivo = "iPhone" if "iphone" in ua else "Android" if "android" in ua else "PC"
            so = "iOS" if "iphone" in ua else "Android" if "android" in ua else "Windows/Mac"
            navegador = "Chrome" if "chrome" in ua else "Safari" if "safari" in ua else "Firefox" if "firefox" in ua else "Outro"
            
            agora = st.session_state["entrada_pagina"]
            session_id = st.session_state["session_id"]

            conn = get_db_connection()
            cur = conn.cursor()
            
            # Garante fuso horário de Brasília na sessão
            cur.execute("SET TIME ZONE 'America/Sao_Paulo';")

            query = """
                INSERT INTO controle_acesso_site 
                (data_hora, session_id, dispositivo, sistema_operacional, navegador, ip, origem, pagina, acao, duracao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id_acesso;
            """
            
            valores = (
                agora, session_id, dispositivo, so, navegador, 
                ip, "Direto", nome_pagina, acao, '00:00:00'
            )
            
            cur.execute(query, valores)
            # Captura o ID gerado automaticamente para atualizar a duração depois
            st.session_state["id_acesso_db"] = cur.fetchone()[0]
            
            conn.commit()
            cur.close()
            conn.close()
    except Exception as e:
        print(f"Erro ao registrar acesso no DB: {e}")

def atualizar_duracao_db():
    """Atualiza a coluna duracao no banco de dados."""
    id_acesso = st.session_state.get("id_acesso_db")
    if id_acesso:
        try:
            duracao_atual = calcular_duracao_texto()
            conn = get_db_connection()
            cur = conn.cursor()
            
            cur.execute(
                "UPDATE controle_acesso_site SET duracao = %s WHERE id_acesso = %s",
                (duracao_atual, id_acesso)
            )
            
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao atualizar duração: {e}")

def exibir_rodape():
    """Exibe o rodapé e atualiza o tempo de permanência no banco."""
    atualizar_duracao_db()
    st.markdown(
        "<hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'>"
        "<div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>"
        "SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>", 
        unsafe_allow_html=True
    )

def salvar_formulario_contato_db(nome, email, whatsapp, mensagem):
    """Salva os dados do formulário na tabela contato_site."""
    try:
        atualizar_duracao_db()
        conn = get_db_connection()
        cur = conn.cursor()
        
        query = """
            INSERT INTO contato_site (nome_completo, email, whatsapp, mensagem)
            VALUES (%s, %s, %s, %s)
        """
        cur.execute(query, (nome, email, whatsapp, mensagem))
        
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao salvar formulário: {e}")
        return False
