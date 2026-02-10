import streamlit as st
import gspread
import uuid
import time
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# =========================================================
# SESSÃO
# =========================================================
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()


# =========================================================
# AUTENTICAÇÃO GOOGLE (STREAMLIT SECRETS)
# =========================================================
def obter_credenciais():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    return Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=scope,
    )


@st.cache_resource
def conectar_planilha():
    creds = obter_credenciais()
    client = gspread.authorize(creds)

    id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"

    return client.open_by_key(id_planilha).sheet1


# =========================================================
# LOG DE ACESSO
# =========================================================
def registrar_acesso(nome_pagina, acao="Visualização"):
    try:
        sheet = conectar_planilha()

        fuso = timezone(timedelta(hours=-3))
        agora = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")

        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"

        sheet.append_row([
            agora,
            st.session_state.get("session_id"),
            dispositivo,
            "Ativo",
            "Navegador",
            "Remote",
            "Direto",
            nome_pagina,
            acao,
            "00:00",
        ])

    except Exception as e:
        print("Erro ao registrar acesso:", e)


# =========================================================
# FORMULÁRIO DE CONTATO
# =========================================================
def salvar_formulario_contato(nome, email, whatsapp, mensagem):
    try:
        sheet = conectar_planilha()

        fuso = timezone(timedelta(hours=-3))
        data = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")

        sheet.append_row([
            data,
            nome,
            email,
            whatsapp,
            mensagem,
        ])

        return True

    except Exception as e:
        st.error(f"Erro ao salvar contato: {e}")
        return False


# =========================================================
# RODAPÉ
# =========================================================
def exibir_rodape():
    st.markdown(
        """
        <hr style='border:0.5px solid rgba(255,255,255,0.1); margin-top:50px;'>

        <div style='text-align:center; color:gray; font-size:0.8rem; padding-bottom:20px;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
        """,
        unsafe_allow_html=True,
    )
