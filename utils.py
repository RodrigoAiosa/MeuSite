import streamlit as st
import gspread
import re
import os
import json
from datetime import datetime
from google.oauth2.service_account import Credentials # Biblioteca atualizada
from utils import exibir_rodape, registrar_acesso

# --- REGISTRO DE ACESSO ---
registrar_acesso("Página de Contato")

def salvar_contato(dados):
    """
    Salva os dados do formulário na planilha de contatos usando google-auth.
    Preserva registros anteriores conforme instrução.
    """
    # Escopos atualizados para Google Auth
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    
    # Caminho do JSON (ajustado para subir um nível a partir de Views/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    caminho_json = os.path.join(root_dir, "meuprojetocadsite-5ecb421b15a7.json")
    
    try:
        # Autenticação moderna usando as mesmas credenciais do utils.py
        creds = Credentials.from_service_account_file(caminho_json, scopes=scope)
        client = gspread.authorize(creds)
        
        # URL da sua planilha de contatos
        url = "https://docs.google.com/spreadsheets/d/1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU/edit#gid=0"
        sheet = client.open_by_url(url).sheet1
        
        # Append preservando dados existentes 
        sheet.append_row(dados)
        
    except FileNotFoundError:
        raise Exception(f"Arquivo JSON não encontrado em: {caminho_json}")
    except Exception as e:
        raise Exception(f"Erro na autenticação/planilha: {str(e)}")

def validar_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def main():
    # --- INJEÇÃO DE CSS PARA DESIGN DE ALTA CONVERSÃO ---
    st.markdown("""
        <style>
        .stForm {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px !important;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }

        div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div {
            background-color: rgba(15, 23, 42, 0.6) !important;
            border-radius: 12px !important;
            border: 1px solid rgba(0, 180, 216, 0.2) !important;
        }

        button[kind="primaryFormSubmit"] {
            width: 100%;
            background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%) !important;
            color: white !important;
            border-radius: 12px !important;
            font-weight: bold !important;
            height: 3rem;
        }

        .contact-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class='contact-header'>
            <h1 style='color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>
            <p style='color: #94a3b8; font-size: 1.1rem;'>
                Preencha os dados abaixo e entrarei em contato em até 24h.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.form(key="form_contato", clear_on_submit=True):
            nome = st.text_input("👤 Nome Completo", placeholder="Ex: Rodrigo Aiosa")
            
            f_col1, f_col2 = st.columns(2)
            with f_col1:
                email = st.text_input("📧 E-mail Profissional", placeholder="seu@email.com")
            with f_col2:
                whatsapp = st.text_input("📱 WhatsApp (com DDD)", placeholder="11988887777")
            
            mensagem = st.text_area("💬 Como posso te ajudar?", placeholder="Conte um pouco sobre seu desafio...", height=150)
            
            botao_enviar = st.form_submit_button("Enviar Mensagem Agora")

        if botao_enviar:
            if len(nome.strip()) < 10:
                st.error("❌ O nome deve ter no mínimo 10 caracteres.")
            elif not validar_email(email.lower()):
                st.error("❌ Por favor, insira um e-mail válido.")
            elif not (whatsapp.isdigit() and len(whatsapp) >= 10):
                st.error("❌ Insira um WhatsApp válido (apenas números com DDD).")
            elif not mensagem:
                st.error("❌ Por favor, preencha o campo de mensagem.")
            else:
                try:
                    with st.spinner("Enviando sua mensagem..."):
                        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        lista_dados = [data_hora, nome, email, whatsapp, mensagem]
                        
                        salvar_contato(lista_dados)
                        st.balloons()
                        st.success("✅ Sucesso! Recebi sua mensagem e falaremos em breve.")
                
                except Exception as e:
                    st.error(f"Erro ao enviar: {e}")

if __name__ == "__main__":
    main()

exibir_rodape()
