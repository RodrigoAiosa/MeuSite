import streamlit as st
import gspread
import uuid
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone
import time

# --- CONFIGURAÇÃO DE SESSÃO INICIAL ---
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())[:8]

# Registro do tempo de início da sessão para cálculo de duração
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = time.time()

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
    Registra o acesso evitando duplicidade e incluindo a duração da sessão.
    """
    # 1. GARANTIA DE SESSÃO
    if 'session_id' not in st.session_state:
        st.session_state['session_id'] = str(uuid.uuid4())[:8]
    
    id_sessao = st.session_state['session_id']

    # 2. TRAVA ANTI-DUPLICIDADE
    tempo_atual = time.time()
    ultima_pag = st.session_state.get('ultima_pagina_registrada')
    ultimo_time = st.session_state.get('ultimo_registro_time', 0)

    if ultima_pag == nome_pagina and (tempo_atual - ultimo_time) < 4:
        return 

    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("Relatorio_Acessos_Site").sheet1
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora_dt = datetime.now(fuso_brasilia)
            agora_str = agora_dt.strftime("%d/%m/%Y %H:%M:%S")
            
            # 3. CÁLCULO DA DURAÇÃO
            segundos_decorridos = int(tempo_atual - st.session_state.get('start_time', tempo_atual))
            duracao = str(timedelta(seconds=segundos_decorridos))
            
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

            # Linha com a nova coluna 'Duração' ao final
            linha = [
                agora_str, 
                id_sessao, 
                dispositivo, 
                so, 
                "Navegador", 
                ip, 
                "Direto", 
                nome_pagina, 
                acao, 
                duracao
            ]
            
            sheet.append_row(linha)
            
            # ATUALIZA A TRAVA
            st.session_state['ultima_pagina_registrada'] = nome_pagina
            st.session_state['ultimo_registro_time'] = tempo_atual

    except Exception as e:
        print(f"Erro silencioso no log: {e}")

def salvar_formulario_contato(dados_lista):
    """
    Salva contato na planilha bd_contato_form_site preservando o histórico.
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
        st.error(f"Erro ao salvar formulário: {e}")
        return False

def exibir_rodape():
    """
    Exibe o rodapé padrão em todas as páginas.
    """
    st.markdown("---")
    st.markdown("<div style='text-align: center; color: gray;'>Desenvolvido por Rodrigo Aiosa © 2026</div>", unsafe_allow_html=True)
