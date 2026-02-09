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

def obter_credenciais():
    """Centraliza a busca do JSON de credenciais na raiz do projeto."""
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    # No Streamlit Cloud, o arquivo na raiz é acessado diretamente pelo nome
    caminho_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(caminho_json):
        # Tenta buscar um nível acima caso esteja sendo chamado de dentro de Views/
        caminho_json = os.path.join("..", "meuprojetocadsite-5ecb421b15a7.json")
        
    return Credentials.from_service_account_file(caminho_json, scopes=scope)

def registrar_acesso(nome_pagina, acao="Visualização"):
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        sheet = client.open("Relatorio_Acessos_Site").sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_str = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")
        
        segundos = int(time.time() - st.session_state["start_time"])
        duracao = str(timedelta(seconds=segundos))

        # Dados de cabeçalho para detecção básica
        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"

        sheet.append_row([
            agora_str, st.session_state["session_id"], dispositivo, 
            "Detectado", "Navegador", "Remote", "Direto", 
            nome_pagina, acao, duracao
        ])
    except Exception as e:
        print(f"Erro Log: {e}")

def exibir_rodape():
    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; color:gray; font-size: 0.8rem;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>",
        unsafe_allow_html=True
    )
