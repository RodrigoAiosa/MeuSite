import streamlit as st
import uuid
import psycopg2
import urllib.parse
from datetime import datetime, timedelta, timezone

# ============================================================
# CONFIGURAÇÕES — Supabase (Session Pooler IPv4)
# ============================================================

SUPABASE_CONFIG = {
    "host":            "aws-1-us-east-1.pooler.supabase.com",
    "database":        "postgres",
    "user":            "postgres.hqkhtpwmciavtobsutph",
    "password":        st.secrets.get("SUPABASE_PASSWORD", ""),
    "port":            "5432",
    "sslmode":         "require",
    "connect_timeout": 10,
}

WHATSAPP_NUMBER = "11977019335"


# ============================================================
# ESTADO DA SESSÃO
# ============================================================

def inicializar_estado():
    if "session_id" not in st.session_state:
        st.session_state["session_id"] = str(uuid.uuid4())[:8]
    if "entrada_pagina" not in st.session_state:
        st.session_state["entrada_pagina"] = datetime.now(timezone(timedelta(hours=-3)))
    if "leu_ate_o_fim" not in st.session_state:
        st.session_state["leu_ate_o_fim"] = False

inicializar_estado()


# ============================================================
# CONEXÃO — SUPABASE
# ============================================================

def _conectar_supabase():
    """Retorna uma conexão psycopg2 com o Supabase via Session Pooler IPv4."""
    return psycopg2.connect(**SUPABASE_CONFIG)


# ============================================================
# UTILITÁRIOS
# ============================================================

def calcular_duracao_texto() -> str:
    """Retorna o tempo decorrido desde a entrada na página no formato MM:SS."""
    agora = datetime.now(timezone(timedelta(hours=-3)))
    delta = agora - st.session_state["entrada_pagina"]
    segundos_totais = int(delta.total_seconds())
    minutos  = segundos_totais // 60
    segundos = segundos_totais % 60
    return f"{minutos:02d}:{segundos:02d}"


def _coletar_metadados() -> dict:
    """Extrai dispositivo, navegador e IP dos headers HTTP."""
    headers = st.context.headers
    ua  = headers.get("User-Agent", "").lower()
    ip  = headers.get("X-Forwarded-For", "Privado").split(",")[0].strip()

    dispositivo = (
        "iPhone"  if "iphone"  in ua else
        "Android" if "android" in ua else
        "PC"
    )
    navegador = (
        "Chrome"  if "chrome"  in ua else
        "Safari"  if "safari"  in ua else
        "Firefox" if "firefox" in ua else
        "Outro"
    )
    return {"dispositivo": dispositivo, "navegador": navegador, "ip": ip}


# ============================================================
# REGISTRO DE ACESSO — INSERT
# ============================================================

def registrar_acesso(nome_pagina: str, acao: str = "Visualização"):
    """
    Registra o acesso inicial na tabela registros_acesso.
    Chame no início de cada página do seu app.
    """
    try:
        inicializar_estado()
        st.session_state["pagina_atual"] = nome_pagina

        meta  = _coletar_metadados()
        agora = datetime.now(timezone(timedelta(hours=-3)))
        sid   = st.session_state["session_id"]

        conn = _conectar_supabase()
        cur  = conn.cursor()
        cur.execute(
            """
            INSERT INTO registros_acesso
                (data_hora, session_id, dispositivo, navegador, ip, pagina, acao, duracao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (agora, sid, meta["dispositivo"], meta["navegador"],
             meta["ip"], nome_pagina, acao, "00:00"),
        )
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f"[registrar_acesso] Erro: {e}")


# ============================================================
# ATUALIZAÇÃO DE DURAÇÃO — UPDATE
# ============================================================

def atualizar_duracao_db():
    """Atualiza a duração real no registro mais recente desta sessão."""
    try:
        tempo_real = calcular_duracao_texto()
        sid    = st.session_state.get("session_id")
        pagina = st.session_state.get("pagina_atual")

        conn = _conectar_supabase()
        cur  = conn.cursor()
        cur.execute(
            """
            UPDATE registros_acesso
            SET duracao = %s
            WHERE id = (
                SELECT id FROM registros_acesso
                WHERE session_id = %s AND pagina = %s
                ORDER BY data_hora DESC
                LIMIT 1
            )
            """,
            (tempo_real, sid, pagina),
        )
        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f"[atualizar_duracao_db] Erro: {e}")


# ============================================================
# RODAPÉ
# ============================================================

def exibir_rodape():
    """Atualiza a duração no Supabase e exibe o rodapé padrão."""
    atualizar_duracao_db()
    st.markdown(
        """
        <hr style='border: 0.5px solid rgba(255,255,255,0.1); margin-top: 50px;'>
        <div style='text-align:center; color:gray; font-size:0.8rem; padding-bottom:20px;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# FORMULÁRIO DE CONTATO
# ============================================================

def gerar_link_whatsapp(nome_cliente: str, servico: str = "Consultoria") -> str:
    """Gera um link personalizado para o WhatsApp."""
    texto = (
        f"Olá Rodrigo! Meu nome é {nome_cliente} e tenho interesse em {servico}. "
        "Vi seu portfólio e gostaria de conversar."
    )
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(texto)}"


def salvar_formulario_contato(dados: list) -> bool:
    """
    Salva os dados do formulário de contato no Supabase
    e atualiza a duração da sessão atual.
    """
    try:
        atualizar_duracao_db()

        conn = _conectar_supabase()
        cur  = conn.cursor()
        cur.execute(
            """
            INSERT INTO contatos
                (nome, email, servico, mensagem, data_hora)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                dados[0] if len(dados) > 0 else "",
                dados[1] if len(dados) > 1 else "",
                dados[2] if len(dados) > 2 else "Data Intelligence",
                dados[3] if len(dados) > 3 else "",
                datetime.now(timezone(timedelta(hours=-3))),
            ),
        )
        conn.commit()
        cur.close()
        conn.close()

        servico = dados[2] if len(dados) > 2 else "Data Intelligence"
        whatsapp_link = gerar_link_whatsapp(dados[0], servico)

        st.success("Dados enviados com sucesso!")
        st.markdown(f"[Falar comigo agora no WhatsApp]({whatsapp_link})")
        return True

    except Exception as e:
        print(f"[salvar_formulario_contato] Erro: {e}")
        return False
