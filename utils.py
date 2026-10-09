import streamlit as st
import threading
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

_db_lock = threading.Lock()


@st.cache_resource(show_spinner=False)
def _conectar_supabase():
    """
    Conexão psycopg2 única, reaproveitada entre execuções e sessões.
    Abrir uma conexão TLS nova a cada rerun era o maior custo de cada página.
    """
    conn = psycopg2.connect(
        **SUPABASE_CONFIG,
        keepalives=1,
        keepalives_idle=30,
        keepalives_interval=10,
        keepalives_count=3,
    )
    conn.autocommit = True
    return conn


def _executar(sql: str, params: tuple = (), retornar: bool = False):
    """
    Executa um comando na conexão compartilhada.
    Se a conexão em cache tiver caído (timeout do pooler, rede), descarta-a
    e tenta uma vez com uma conexão nova. Falha ao conectar não é repetida,
    para não dobrar a espera quando o banco está fora do ar.
    """
    for tentativa in (1, 2):
        conn = _conectar_supabase()
        try:
            with _db_lock, conn.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchone() if retornar else None
        except (psycopg2.OperationalError, psycopg2.InterfaceError):
            _conectar_supabase.clear()
            if tentativa == 2:
                raise


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
    Registra o acesso na tabela registros_acesso.
    Chamada uma única vez, no main.py. Só grava quando o visitante muda de
    página: reruns na mesma página (cliques em botões, filtros) não geram
    novo INSERT.
    """
    try:
        inicializar_estado()
        if st.session_state.get("pagina_atual") == nome_pagina:
            return

        agora = datetime.now(timezone(timedelta(hours=-3)))
        st.session_state["pagina_atual"] = nome_pagina
        st.session_state["entrada_pagina"] = agora
        st.session_state["registro_id"] = None

        meta = _coletar_metadados()
        sid  = st.session_state["session_id"]

        linha = _executar(
            """
            INSERT INTO registros_acesso
                (data_hora, session_id, dispositivo, navegador, ip, pagina, acao, duracao)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (agora, sid, meta["dispositivo"], meta["navegador"],
             meta["ip"], nome_pagina, acao, "00:00"),
            retornar=True,
        )
        st.session_state["registro_id"] = linha[0] if linha else None

    except Exception as e:
        print(f"[registrar_acesso] Erro: {e}")


# ============================================================
# ATUALIZAÇÃO DE DURAÇÃO — UPDATE
# ============================================================

def atualizar_duracao_db():
    """Atualiza a duração no registro de acesso da página atual."""
    try:
        registro_id = st.session_state.get("registro_id")
        if registro_id is None:
            return
        _executar(
            "UPDATE registros_acesso SET duracao = %s WHERE id = %s",
            (calcular_duracao_texto(), registro_id),
        )
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

        _executar(
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

        servico = dados[2] if len(dados) > 2 else "Data Intelligence"
        whatsapp_link = gerar_link_whatsapp(dados[0], servico)

        st.success("Dados enviados com sucesso!")
        st.markdown(f"[Falar comigo agora no WhatsApp]({whatsapp_link})")
        return True

    except Exception as e:
        print(f"[salvar_formulario_contato] Erro: {e}")
        return False
