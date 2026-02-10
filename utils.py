import streamlit as st
import gspread
import json
import os
import uuid
import time
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO GLOBAL ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

if "start_time" not in st.session_state:
    st.session_state["start_time"] = time.time()

def obter_credenciais():
    """Conexão blindada: limpa a assinatura da chave para matar o erro de JWT Signature."""
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    caminho_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(caminho_json):
        raise FileNotFoundError(f"Arquivo {caminho_json} não encontrado na raiz!")

    with open(caminho_json, 'r') as f:
        info = json.load(f)
    
    # RESOLUÇÃO DO ERRO JWT: Limpeza radical de espaços e quebras de linha corrompidas
    if "private_key" in info:
        # Primeiro limpa espaços antes/depois, depois garante as quebras de linha corretas
        chave_limpa = info["private_key"].strip()
        info["private_key"] = chave_limpa.replace("\\n", "\n")
    
    return Credentials.from_service_account_info(info, scopes=scope)

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra acessos na planilha preservando todo o histórico anterior."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        # ID exato da sua planilha
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_str = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")
        
        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"

        # Adiciona nova linha preservando os registros existentes
        sheet.append_row([
            agora_str, st.session_state.get("session_id"), dispositivo,
            "Ativo", "Navegador", "Remote", "Direto", nome_pagina, acao, "00:00"
        ])
    except Exception as e:
        print(f"Erro Log: {e}")

def salvar_formulario_contato(dados):
    """Grava novos contatos sem apagar os registros existentes."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1
        
        # append_row é o comando de segurança para não sobrescrever
        sheet.append_row(dados)
        return True
    except Exception as e:
        st.error(f"Erro na API do Google: {str(e)}")
        return False

def exibir_rodape():
    """Rodapé padrão da SKY DATA SOLUTION."""
    st.markdown(
        """
        <hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'>
        <div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
        """,
        unsafe_allow_html=True
    )
