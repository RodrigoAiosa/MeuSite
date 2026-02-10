import streamlit as st
import gspread
import uuid
from google.oauth2.service_account import Credentials
from datetime import datetime, timezone


# -------------------------
# SESSION ID
# -------------------------
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]


# -------------------------
# CONEXÃO GOOGLE SHEETS
# -------------------------
def conectar_gsheet():
    try:
        creds_dict = dict(st.secrets["gcp_service_account"])
        creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ]

        creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)
        return gspread.authorize(creds)

    except Exception as e:
        print("Erro conexão gsheet:", e)
        return None


# -------------------------
# REGISTRAR ACESSO
# -------------------------
def registrar_acesso(pagina):
    client = conectar_gsheet()

    if client is None:
        return

    try:
        sheet = client.open("Relatorio_Acessos_Site").sheet1

        agora = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        dispositivo = st.context.headers.get("User-Agent", "unknown")

        sheet.append_row([
            agora,
            dispositivo,
            pagina,
            st.session_state["session_id"],
        ])

    except Exception as e:
        print("Erro registrar acesso:", e)


# -------------------------
# RODAPÉ
# -------------------------
def exibir_rodape():
    st.markdown("---")
    st.caption("SKY DATA SOLUTION © 2026 | Rodrigo Aiosa")
