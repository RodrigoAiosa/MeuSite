import streamlit as st
import gspread
import re
from datetime import datetime
from utils import exibir_rodape, registrar_acesso, obter_credenciais

# Registro de entrada
registrar_acesso("Página de Contato")

def salvar_contato(dados):
    """Salva os dados preservando o histórico da planilha."""
    try:
        creds = obter_credenciais()
        client = gspread.authorize(creds)
        # Use a URL exata para evitar erro de 'account not found'
        url_planilha = "https://docs.google.com/spreadsheets/d/1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU/edit#gid=0"
        sheet = client.open_by_url(url_planilha).sheet1
        sheet.append_row(dados)
    except Exception as e:
        raise Exception(f"Falha na conexão: {str(e)}")

def validar_email(email):
    return re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email)

def main():
    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
    
    with st.container():
        with st.form(key="form_contato", clear_on_submit=True):
            nome = st.text_input("👤 Nome Completo", placeholder="Rodrigo Aiosa")
            col_mail, col_zap = st.columns(2)
            with col_mail:
                email = st.text_input("📧 E-mail Profissional")
            with col_zap:
                whatsapp = st.text_input("📱 WhatsApp (com DDD)")
            
            mensagem = st.text_area("💬 Como posso te ajudar?")
            botao = st.form_submit_button("Enviar Mensagem Agora")

        if botao:
            if not nome or not email or not whatsapp or not mensagem:
                st.error("❌ Preencha todos os campos.")
            elif not validar_email(email.lower()):
                st.error("❌ E-mail inválido.")
            else:
                try:
                    with st.spinner("Enviando..."):
                        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        salvar_contato([agora, nome, email, whatsapp, mensagem])
                        st.balloons()
                        st.success("✅ Mensagem enviada! Entrarei em contato em breve.")
                except Exception as e:
                    st.error(f"Erro crítico: {e}")

if __name__ == "__main__":
    main()

exibir_rodape()
