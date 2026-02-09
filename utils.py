import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import json

def registrar_acesso(nome_pagina):
    """
    Registra informações de acesso no Google Sheets usando Streamlit Secrets.
    Evita erros de caminho de arquivo e protege suas chaves no GitHub.
    """
    try:
        # 1. Configuração de Escopo
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        
        # 2. Carregamento das Credenciais via Secrets (O Pulo do Gato para Deploy)
        # Em vez de ler um arquivo .json, lemos do st.secrets
        if "gcp_service_account" in st.secrets:
            creds_info = dict(st.secrets["gcp_service_account"])
            # Corrige as quebras de linha da chave privada
            creds_info["private_key"] = creds_info["private_key"].replace('\\n', '\n')
            creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_info, scope)
        else:
            st.error("Configuração 'gcp_service_account' não encontrada nos Secrets.")
            return

        # 3. Autenticação e Abertura da Planilha
        client = gspread.authorize(creds)
        # Use o ID da planilha (aquele código longo na URL) para maior precisão
        sheet = client.open("Relatorio_Acessos_Site").sheet1 

        # 4. Coleta de dados do visitante
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Coleta de cabeçalhos de forma segura
        headers = st.context.headers
        user_agent = headers.get("User-Agent", "Desconhecido")
        ip = headers.get("X-Forwarded-For", "Localhost").split(',')[0]
        
        # Identificação de SO simplificada
        so = "Windows" if "Windows" in user_agent else "Mobile" if "Android" in user_agent or "iPhone" in user_agent else "Outro"

        # 5. Gravação dos dados
        # Conforme sua instrução salva: preserva dados existentes e adiciona novos à tabela
        sheet.append_row([agora, "Acesso Portfólio", so, ip, nome_pagina])
        
        print(f"✅ SUCESSO: Acesso registrado na página '{nome_pagina}'")

    except Exception as e:
        # Log de erro silencioso para não quebrar a experiência do usuário
        print(f"❌ ERRO NO REGISTRO: {str(e)}")

def exibir_rodape():
    """Exibe o rodapé padrão em todas as páginas."""
    st.markdown("---")
    footer_html = """
    <div style='text-align: center; color: gray;'>
        <p style='margin-bottom: 5px;'><b>Rodrigo Aiosa © 2026</b> | Especialista em BI & Treinamentos</p>
        <div style='display: flex; justify-content: center; gap: 20px; font-size: 24px;'>
            <a href='https://wa.me/5511977019335' target='_blank'>
                <img src='https://cdn-icons-png.flaticon.com/512/733/733585.png' width='25' height='25'>
            </a>
            <a href='https://www.linkedin.com/in/rodrigoaiosa/' target='_blank'>
                <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='25' height='25'>
            </a>
        </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
