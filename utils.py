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
    Versão robusta para capturar acessos mobile/4G.
    """
    try:
        client = conectar_google_sheets()
        if client:
            sheet = client.open("Relatorio_Acessos_Site").sheet1
            
            fuso_brasilia = timezone(timedelta(hours=-3))
            agora = datetime.now(fuso_brasilia).strftime("%d/%m/%Y %H:%M:%S")
            
            # Lógica robusta para headers (evita erro no 4G)
            try:
                headers = st.context.headers
                ua_string = headers.get("User-Agent", "").lower()
                # Tenta pegar o IP real, senão usa um padrão
                ip_raw = headers.get("X-Forwarded-For", "IP_Nao_Identificado")
                ip = ip_raw.split(',')[0] if ip_raw else "IP_Nao_Identificado"
                
                # Identificação de dispositivo ampliada
                if any(x in ua_string for x in ["mobile", "android", "iphone", "ipad"]):
                    dispositivo = "Celular"
                else:
                    dispositivo = "PC"
            except:
                # Se os headers falharem (comum em algumas redes móveis), registra como desconhecido mas NÃO PARA o script
                dispositivo = "Mobile/Outro"
                ip = "Nao_Capturado"

            # Linha formatada para as colunas A até I da sua planilha
            linha = [
                agora,                          # Coluna A: data_hora
                st.session_state.get('session_id', 'N/A'), # Coluna B: session_id
                dispositivo,                    # Coluna C: dispositivo
                "Detectado",                    # Coluna D: sistema_operacional
                "Navegador",                    # Coluna E: navegador
                ip,                             # Coluna F: ip
                "Direto",                       # Coluna G: origem
                nome_pagina,                    # Coluna H: pagina
                acao                            # Coluna I: acao
            ]
            
            # append_row preserva dados existentes conforme diretriz de 2026-01-18
            sheet.append_row(linha)
    except Exception as e:
        # Apenas para debug interno se necessário
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
            
            # Salva Data + Nome, Email, WhatsApp, Mensagem
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
