import streamlit as st
import gspread
import uuid
from google.oauth2.service_account import Credentials
from datetime import datetime, timedelta, timezone

# --- CONFIGURAÇÃO DE SESSÃO ---
if 'session_id' not in st.session_state:
    st.session_state['session_id'] = str(uuid.uuid4())[:8]

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
            
            # Garante que as quebras de linha sejam interpretadas corretamente
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
    Registra o acesso na planilha Relatorio_Acessos_Site (9 colunas).
    Identifica Dispositivo e Sistema Operacional (Windows, Android, Linux, Mac, iOS).
    """
    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("Relatorio_Acessos_Site").sheet1
            
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
            
            # Inicialização de variáveis de detecção
            dispositivo = "PC"
            so = "Não Identificado"
            ip = "Nao_Capturado"
            
            try:
                headers = st.context.headers
                ua_string = headers.get("User-Agent", "").lower()
                
                # 1. Identificar IP
                ip_raw = headers.get("X-Forwarded-For", "")
                if ip_raw:
                    ip = ip_raw.split(',')[0]
                
                # 2. Identificar Sistema Operacional
                if "windows" in ua_string:
                    so = "Windows"
                elif "android" in ua_string:
                    so = "Android"
                    dispositivo = "Celular"
                elif "linux" in ua_string:
                    so = "Linux"
                elif "macintosh" in ua_string or "mac os" in ua_string:
                    so = "Mac OS"
                elif "iphone" in ua_string or "ipad" in ua_string:
                    so = "iOS"
                    dispositivo = "Celular"
                
                # 3. Refinar Dispositivo (caso não tenha pego no SO)
                if "mobile" in ua_string and dispositivo == "PC":
                    dispositivo = "Celular"
                    
            except:
                pass

            # Linha formatada para as colunas A até I da sua planilha
            linha = [
                agora,                          # Coluna A: data_hora
                st.session_state.get('session_id', 'N/A'), # Coluna B: session_id
                dispositivo,                    # Coluna C: dispositivo
                so,                             # Coluna D: sistema_operacional
                "Navegador",                    # Coluna E: navegador
                ip,                             # Coluna F: ip
                "Direto",                       # Coluna G: origem
                nome_pagina,                    # Coluna H: pagina
                acao                            # Coluna I: acao
            ]
            
            # append_row preserva dados existentes conforme sua regra
            sheet.append_row(linha)
    except Exception as e:
        print(f"Erro silencioso no log de acesso: {e}")

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
