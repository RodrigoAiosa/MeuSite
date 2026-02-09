import streamlit as st
import gspread
import uuid
import os
import time
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()

def registrar_acesso(nome_pagina, acao="Visualização"):
    """
    Registra o acesso na planilha Google Sheets.
    Preserva dados existentes e adiciona novas linhas.
    """
    try:
        scope = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        # O arquivo JSON deve estar na raiz do projeto
        creds = Credentials.from_service_account_file(
            "meuprojetocadsite-5ecb421b15a7.json",
            scopes=scope
        )

        client = gspread.authorize(creds)
        # Certifique-se que o nome da aba/planilha está correto
        sheet = client.open("Relatorio_Acessos_Site").sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_dt = datetime.now(fuso)
        agora_str = agora_dt.strftime("%d/%m/%Y %H:%M:%S")

        segundos_decorridos = int(time.time() - st.session_state["start_time"])
        duracao_formatada = str(timedelta(seconds=segundos_decorridos))

        headers = st.context.headers
        ua = headers.get("User-Agent", "").lower()
        ip = headers.get("X-Forwarded-For", "Localhost").split(",")[0]

        dispositivo = "Celular" if "mobile" in ua else "PC"

        # Adiciona nova linha preservando as anteriores
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
            duracao_formatada 
        ])

    except Exception as e:
        # Silencioso no front-end para não atrapalhar o usuário
        print(f"Erro no Registro de Log: {e}")

def exibir_rodape():
    """
    Exibe o rodapé padrão com uma única linha divisória.
    """
    st.markdown(
        """
        <hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px; margin-bottom: 20px;'>
        <div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
        """,
        unsafe_allow_html=True
    )
