import streamlit as st
import gspread
import json
import os
import uuid
import time
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()

def obter_credenciais():
    """Mata o erro de JWT Signature limpando a formatação da chave privada."""
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    caminho_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(caminho_json):
        raise FileNotFoundError(f"Arquivo {caminho_json} não encontrado!")

    with open(caminho_json, 'r') as f:
        info = json.load(f)
    
    # RESOLUÇÃO DO ERRO JWT: Remove espaços e garante quebras de linha reais
    if "private_key" in info:
        info["private_key"] = info["private_key"].replace("\\n", "\n").strip()
    
    return Credentials.from_service_account_info(info, scopes=scope)

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra logs preservando os dados existentes."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_str = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")
        
        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"

        # Adiciona linha no fim sem apagar nada
        sheet.append_row([
            agora_str, st.session_state.get("session_id"), dispositivo,
            "Ativo", "Navegador", "Remote", "Direto", nome_pagina, acao, "00:00"
        ])
    except Exception as e:
        print(f"Erro Log: {e}")

def salvar_formulario_contato(dados):
    """Grava novos dados e preserva o histórico da tabela."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1
        
        # O gspread.append_row garante a preservação dos dados antigos
        sheet.append_row(dados)
        return True
    except Exception as e:
        st.error(f"Erro na API do Google: {str(e)}")
        return False

def exibir_rodape():
    """Rodapé SKY DATA SOLUTION 2026."""
    st.markdown(
        """
        <hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'>
        <div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
        """,
        unsafe_allow_html=True
    )
