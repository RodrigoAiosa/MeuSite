import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import re
import os
import json
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Página de Contato")

def salvar_contato(dados):
    """
    Salva os dados do formulário na planilha de contatos.
    Ajustado para buscar o JSON na pasta raiz, um nível acima de /Views.
    """
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # --- AJUSTE DE CAMINHO ---
    # Pega o caminho da pasta 'Views'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Sobe um nível para a pasta raiz (onde está o seu JSON)
    root_dir = os.path.dirname(current_dir)
    # Monta o caminho final
    caminho_json = os.path.join(root_dir, "meuprojetocadsite-5ecb421b15a7.json")
    
    # Carregamento seguro para evitar erros de assinatura
    try:
        with open(caminho_json, 'r') as f:
            creds_info = json.load(f)
        
        creds_info["private_key"] = creds_info["private_key"].replace('\\n', '\n')
        
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_info, scope)
        client = gspread.authorize(creds)
        
        # URL da sua planilha de contatos
        url = "https://docs.google.com/spreadsheets/d/1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU/edit#gid=0"
        sheet = client.open_by_url(url).sheet1
        
        # Preserva registros anteriores e adiciona o novo (conforme sua preferência salva)
        sheet.append_row(dados)
        
    except FileNotFoundError:
        raise Exception(f"Arquivo JSON não encontrado em: {caminho_json}")

def validar_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def main():
    # --- INJEÇÃO DE CSS ---
    st.markdown("""
        <style>
        div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div {
            transition: all 0.3s ease-in-out !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        div[data-baseweb="input"]:hover > div, div[data-baseweb="textarea"]:hover > div {
            border-color: #8A2BE2 !important;
            box-shadow: 0 0 10px rgba(138, 43, 226, 0.4) !important;
        }
        div[data-baseweb="input"]:focus-within > div, div[data-baseweb="textarea"]:focus-within > div {
            border-color: #9400D3 !important;
            box-shadow: 0 0 15px rgba(148, 0, 211, 0.7) !important;
        }
        button[kind="primaryFormSubmit"] {
            background-color: #8A2BE2 !important;
            border: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📬 Entre em Contato")
    st.write("Preencha o formulário abaixo para enviar sua mensagem.")

    with st.form(key="form_contato", clear_on_submit=True):
        nome = st.text_input("Nome Completo")
        email = st.text_input("E-mail")
        whatsapp = st.text_input("WhatsApp (Somente 11 números com DDD)")
        mensagem = st.text_area("Sua Mensagem")
        botao_enviar = st.form_submit_button("Enviar Mensagem")

    if botao_enviar:
        if len(nome.strip()) < 10:
            st.error("❌ O nome deve ter no mínimo 10 caracteres.")
        elif not validar_email(email.lower()):
            st.error("❌ Por favor, insira um e-mail válido.")
        elif not (whatsapp.isdigit() and len(whatsapp) == 11):
            st.error("❌ O WhatsApp deve conter apenas números e ter exatamente 11 dígitos.")
        elif not mensagem:
            st.error("❌ Por favor, preencha o campo de mensagem.")
        else:
            try:
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                lista_dados = [data_hora, nome, email, whatsapp, mensagem]
                
                salvar_contato(lista_dados)
                st.success("✅ Mensagem enviada e salva com sucesso!")
                
            except Exception as e:
                st.error(f"Erro crítico: {e}")

if __name__ == "__main__":
    main()

exibir_rodape()