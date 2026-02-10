import streamlit as st
import gspread
import json
import os
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

def obter_credenciais():
    """Mata o erro de assinatura JWT e valida a conta de serviço aiosaprojeto."""
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    # Garante que está lendo o arquivo correto que você subiu
    caminho_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(caminho_json):
        st.error(f"Arquivo {caminho_json} não encontrado!")
        return None

    with open(caminho_json, 'r') as f:
        info = json.load(f)
    
    # LIMPEZA OBRIGATÓRIA: Resolve o erro 'Invalid JWT Signature' das imagens
    if "private_key" in info:
        info["private_key"] = info["private_key"].replace("\\n", "\n").strip()
    
    return Credentials.from_service_account_info(info, scopes=scope)

def salvar_formulario_contato(dados):
    """Adiciona nova linha preservando todo o histórico da planilha."""
    try:
        creds = obter_credenciais()
        if not creds: return False
        
        client = gspread.authorize(creds)
        # ID da sua planilha extraído das abas do seu navegador
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1
        
        # O append_row garante que nada seja apagado, apenas adicionado
        sheet.append_row(dados)
        return True
    except Exception as e:
        st.error(f"Erro na API do Google: {str(e)}")
        return False

def registrar_acesso(nome_pagina):
    """Log de auditoria preservando dados."""
    try:
        creds = obter_credenciais()
        if not creds: return
        client = gspread.authorize(creds)
        sheet = client.open_by_key("1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU").sheet1
        agora = datetime.now(timezone(timedelta(hours=-3))).strftime("%d/%m/%Y %H:%M:%S")
        sheet.append_row([agora, "Acesso", "-", "-", "-", "-", "-", nome_pagina, "Visualização", "00:00"])
    except:
        pass

def exibir_rodape():
    st.markdown("<hr><div style='text-align:center; color:gray; font-size: 0.8rem;'>SKY DATA SOLUTION © 2026 | Rodrigo Aiosa</div>", unsafe_allow_html=True)
