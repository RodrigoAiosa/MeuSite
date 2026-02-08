import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os
import json

def registrar_acesso(nome_pagina):
    """
    Registra informações de acesso no Google Sheets.
    Garante o tratamento correto da chave privada para evitar erros de JWT.
    """
    try:
        # 1. Configuração de Escopo
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        
        # 2. Localização do arquivo JSON (Caminho absoluto)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        caminho_json = os.path.join(current_dir, "meuprojetocadsite-5ecb421b15a7.json")
        
        if not os.path.exists(caminho_json):
            print(f"❌ ERRO: Arquivo JSON não encontrado em: {caminho_json}")
            return

        # 3. Carregamento manual para limpar a chave privada (O pulo do gato)
        with open(caminho_json, 'r') as f:
            credentials_dict = json.load(f)
        
        # Corrige as quebras de linha da chave que o Google exige
        credentials_dict["private_key"] = credentials_dict["private_key"].replace('\\n', '\n')

        # 4. Autenticação via dicionário (mais estável que carregar pelo nome do arquivo)
        creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_dict, scope)
        client = gspread.authorize(creds)
        
        # 5. Abertura da Planilha
        # Certifique-se que o nome é EXATAMENTE este no seu Google Drive
        sheet = client.open("Relatorio_Acessos_Site").sheet1 

        # 6. Coleta de dados do visitante
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        user_agent = st.context.headers.get("User-Agent", "Desconhecido")
        ip = st.context.headers.get("X-Forwarded-For", "Localhost").split(',')[0]
        
        # Identificação de SO simplificada
        so = "Windows" if "Windows" in user_agent else "Mobile" if "Android" in user_agent or "iPhone" in user_agent else "Outro"

        # 7. Gravação (Sempre adiciona ao final)
        sheet.append_row([agora, "Acesso Portfólio", so, ip, nome_pagina])
        
        # Log de sucesso no terminal do VS Code
        print(f"✅ SUCESSO: Acesso registrado na página '{nome_pagina}'")

    except Exception as e:
        # Se o erro de JWT persistir aqui, o arquivo JSON pode estar corrompido na origem
        print(f"❌ ERRO NO REGISTRO: {str(e)}")

def exibir_rodape():
    """Função para exibir o rodapé padrão em todas as páginas."""
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