import streamlit as st
import gspread
import uuid
import os
import time
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# ---------------------------------------------------
# SESSION GLOBAL (multipage safe)
# ---------------------------------------------------
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

# Registra o início da sessão para calcular a duração
if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()


def registrar_acesso(nome_pagina, acao="Visualização"):
    """
    Registro seguro no Google Sheets.
    Nunca quebra o app.
    """
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_file(
            "meuprojetocadsite-5ecb421b15a7.json",
            scopes=scope
        )

        client = gspread.authorize(creds)
        sheet = client.open("Relatorio_Acessos_Site").sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_dt = datetime.now(fuso)
        agora_str = agora_dt.strftime("%d/%m/%Y %H:%M:%S")

        # Cálculo da Duração
        segundos_decorridos = int(time.time() - st.session_state["start_time"])
        duracao_formatada = str(timedelta(seconds=segundos_decorridos))

        headers = st.context.headers
        ua = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Localhost").split(",")[0]

        dispositivo = "Celular" if "mobile" in ua else "PC"

        # Append preservando dados existentes e adicionando a duração na última coluna
        sheet.append_row([
            agora_str,
            st.session_state.get("session_id", "unknown"),
            dispositivo,
            "Detectado",
            "Navegador",
            ip,
            "Direto",
            nome_pagina,
            acao,
            duracao_formatada  # Nova última coluna: Duração
        ])

    except Exception as e:
        print("LOG ERROR:", e)


def exibir_rodape():
    st.markdown("---")
    st.markdown(
        "<div style='text-align:center;color:gray'>"
        "Rodrigo Aiosa © 2026 | Especialista em BI & Treinamentos"
        "</div>",
        unsafe_allow_html=True
    )
