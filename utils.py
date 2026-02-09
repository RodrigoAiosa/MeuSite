import streamlit as st
import gspread
import uuid
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone
import time

# --- CONFIGURAÇÃO DE SESSÃO INICIAL ---
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())[:8]

# Inicializa o rastreador de última página para evitar duplicidade
if 'ultima_pagina_registrada' not in st.session_state:
    st.session_state['ultima_pagina_registrada'] = None

def conectar_google_sheets():
    """
    Autentica no Google Sheets usando st.secrets com tratamento de chave PEM.
    """
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    try:
        if "gcp_service_account" in st.secrets:
            creds_info = dict(st.secrets["gcp_service_account"])
            if "private_key" in creds_info:
                creds_info["private_key"] = creds_info["private_key"].replace("\\n", "\n")
            
            creds = Credentials.from_service_account_info(creds_info, scopes=scope)
            return gspread.authorize(creds)
        return None
    except Exception as e:
        st.error(f"Erro Crítico de Autenticação: {e}")
        return None

def registrar_acesso(nome_pagina, acao="Visualização"):
    """
    Registra o acesso evitando duplicidade causada pelo Rerun do Streamlit no Mobile.
    """
    # 1. GARANTIA DE SESSÃO
    if 'session_id' not in st.session_state:
        st.session_state['session_id'] = str(uuid.uuid4())[:8]
    
    id_sessao = st.session_state['session_id']

    # 2. TRAVA ANTI-DUPLICIDADE
    # Se a página atual for igual à última registrada nos últimos 2 segundos, ignora.
    tempo_atual = time.time()
    if 'ultimo_registro_time' not in st.session_state:
        st.session_state['ultimo_registro_time'] = 0

    if st.session_state['ultima_pagina_registrada'] == nome_pagina and \
       (tempo_atual - st.session_state['ultimo_registro_time']) < 3:
        return # Sai da função sem registrar duplicado

    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("Relatorio_Acessos_Site").sheet1
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
            
            dispositivo = "PC"
            so = "Não Identificado"
            ip = "Nao_Capturado"
            
            try:
                headers = st.context.headers
                ua_string = headers.get("User-Agent", "").lower()
                ip_raw = headers.get("X-Forwarded-For", "")
                if ip_raw: ip = ip_raw.split(',')[0]
                
                if "windows" in ua_string: so = "Windows"
                elif "android" in ua_string: 
                    so = "Android"
                    dispositivo = "Celular"
                elif "linux" in ua_string: so = "Linux"
                elif "macintosh" in ua_string or "mac os" in ua_string: so = "Mac OS"
                elif "iphone" in ua_string or "ipad" in ua_string:
                    so = "iOS"
                    dispositivo = "Celular"
                if "mobile" in ua_string and dispositivo == "PC": dispositivo = "Celular"
            except: pass

            linha = [agora, id_sessao, dispositivo, so, "Navegador", ip, "Direto", nome_pagina, acao]
            sheet.append_row(linha)
            
            # ATUALIZA A TRAVA: Salva que esta página acabou de ser registrada
            st.session_state['ultima_pagina_registrada'] = nome_pagina
            st.session_state['ultimo_registro_time'] = tempo_atual

    except Exception as e:
        print(f"Erro silencioso no log: {e}")

def salvar_formulario_contato(dados_lista):
    """
    Salva contato preservando o histórico.
    """
    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("bd_contato_form_site").sheet1
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
            sheet.append_row([agora] + dados_lista)
            return True
    except Exception as e:
        st.error(f"Erro ao salvar: {e}")
        return False

def exibir_rodape():
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: gray;'>Desenvolvido por Rodrigo Aiosa © 2026</div>", unsafe_allow_html=True)
