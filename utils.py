import streamlit as st
import gspread
import json
import os
import uuid
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())[:8]

def obter_credenciais():
    """Resolve o erro de assinatura JWT limpando a formatação da chave privada."""
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
    
    # O nome do arquivo deve ser exatamente o que está no seu GitHub
    caminho_json = "meuprojetocadsite-5ecb421b15a7.json"
    
    if not os.path.exists(caminho_json):
        st.error(f"Erro: Arquivo {caminho_json} não encontrado no repositório.")
        return None

    try:
        with open(caminho_json, 'r') as f:
            info = json.load(f)
        
        # LIMPEZA CRÍTICA: Resolve o erro 'Invalid JWT Signature'
        # Substitui quebras de linha literais por reais e remove espaços extras
        if "private_key" in info:
            info["private_key"] = info["private_key"].replace("\\n", "\n").strip()
            
        return Credentials.from_service_account_info(info, scopes=scope)
    except Exception as e:
        st.error(f"Erro ao carregar credenciais: {e}")
        return None

def registrar_acesso(nome_pagina, acao="Visualização"):
    """Registra acessos preservando o histórico da planilha."""
    try:
        creds = obter_credenciais()
        if not creds:
            return

        client = gspread.authorize(creds)
        # ID da sua planilha extraído da sua URL
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        sheet = client.open_by_key(id_planilha).sheet1

        fuso = timezone(timedelta(hours=-3))
        agora_str = datetime.now(fuso).strftime("%d/%m/%Y %H:%M:%S")
        
        # Identificação básica do dispositivo
        ua = st.context.headers.get("User-Agent", "").lower()
        dispositivo = "Celular" if "mobile" in ua else "PC"

        # append_row adiciona uma nova linha e NÃO apaga os dados existentes
        sheet.append_row([
            agora_str, 
            st.session_state.get("session_id"), 
            dispositivo, 
            "Ativo", 
            "Navegador", 
            "Remote", 
            "Direto", 
            nome_pagina, 
            acao, 
            "00:00"
        ])
    except Exception as e:
        print(f"Erro ao registrar acesso: {e}")

def salvar_formulario_contato(dados):
    """Salva dados do formulário preservando a tabela existente."""
    try:
        creds = obter_credenciais()
        if not creds:
            return False
            
        client = gspread.authorize(creds)
        id_planilha = "1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU"
        # Acessa a planilha bd_contato_form_site
        sheet = client.open_by_key(id_planilha).sheet1
        
        # append_row garante que o novo contato entre na última linha
        sheet.append_row(dados)
        return True
    except Exception as e:
        # Exibe o erro exato para diagnóstico se a API falhar
        st.error(f"Erro na API do Google: {str(e)}")
        return False

def exibir_rodape():
    """Rodapé padrão SKY DATA SOLUTION."""
    st.markdown("""
        <hr style='border: 0.5px solid rgba(255, 255, 255, 0.1); margin-top: 50px;'>
        <div style='text-align:center; color:gray; font-size: 0.8rem; padding-bottom: 20px;'>
            SKY DATA SOLUTION © 2026 | Rodrigo Aiosa
        </div>
    """, unsafe_allow_html=True)
