import streamlit as st
import gspread
import re
import os
from datetime import datetime
from google.oauth2.service_account import Credentials  # Biblioteca moderna
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Página de Contato")

def salvar_contato(dados):
    """
    Salva os dados do formulário na planilha de contatos.
    Usa a biblioteca google-auth para evitar o erro invalid_grant.
    """
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    # Define o caminho do JSON (subindo um nível a partir da pasta Views)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    caminho_json = os.path.join(root_dir, "meuprojetocadsite-5ecb421b15a7.json")
    
    try:
        # Autenticação robusta (mesma lógica usada no utils.py)
        creds = Credentials.from_service_account_file(caminho_json, scopes=scope)
        client = gspread.authorize(creds)
        
        # URL da planilha de contatos
        url = "https://docs.google.com/spreadsheets/d/1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU/edit#gid=0"
        sheet = client.open_by_url(url).sheet1
        
        # Salva mantendo os dados existentes
        sheet.append_row(dados)
        
    except FileNotFoundError:
        raise Exception(f"Arquivo JSON não encontrado no servidor: {caminho_json}")
    except Exception as e:
        raise Exception(f"Erro na conexão com a planilha: {str(e)}")

def validar_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def main():
    # --- ESTILO CSS ---
    st.markdown("""
        <style>
        .stForm {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px !important;
        }
        button[kind="primaryFormSubmit"] {
            width: 100%;
            background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%) !important;
            color: white !important;
            border-radius: 12px !important;
            font-weight: bold !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.form(key="form_contato", clear_on_submit=True):
            nome = st.text_input("👤 Nome Completo")
            email = st.text_input("📧 E-mail Profissional")
            whatsapp = st.text_input("📱 WhatsApp (com DDD)")
            mensagem = st.text_area("💬 Como posso te ajudar?", height=150)
            
            botao_enviar = st.form_submit_button("Enviar Mensagem")

        if botao_enviar:
            if not nome or not email or not whatsapp or not mensagem:
                st.error("❌ Por favor, preencha todos os campos.")
            elif not validar_email(email.lower()):
                st.error("❌ E-mail inválido.")
            else:
                try:
                    with st.spinner("Enviando..."):
                        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        lista_dados = [data_hora, nome, email, whatsapp, mensagem]
                        
                        salvar_contato(lista_dados)
                        st.balloons()
                        st.success("✅ Mensagem enviada com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao enviar: {e}")

if __name__ == "__main__":
    main()

exibir_rodape()
