import streamlit as st
import re
from datetime import datetime
from utils import exibir_rodape, registrar_acesso, salvar_formulario_contato

# --- REGISTRO DE ACESSO ---
registrar_acesso("Página de Contato")

def validar_email(email):
    # Regex robusta para validar e-mails profissionais
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def main():
    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
    
    with st.form("form_contato", clear_on_submit=True):
        nome = st.text_input("👤 Nome Completo")
        email = st.text_input("📧 E-mail Profissional")
        whatsapp = st.text_input("📱 WhatsApp (11 números)")
        mensagem = st.text_area("💬 Como posso te ajudar?")
        
        enviar = st.form_submit_button("Enviar Mensagem Agora")

        if enviar:
            # Validações para garantir a qualidade dos dados
            if len(nome.strip()) < 10:
                st.error("Insira o nome completo.")
            elif not validar_email(email.lower()):
                st.error("E-mail inválido.")
            elif not (whatsapp.isdigit() and len(whatsapp) == 11):
                st.error("WhatsApp deve ter 11 dígitos (DDD + número).")
            elif not mensagem.strip():
                st.error("Escreva uma mensagem.")
            else:
                with st.spinner("Enviando para a planilha..."):
                    # Organização dos dados conforme a planilha
                    dados_lista = [
                        datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 
                        nome, 
                        email, 
                        whatsapp, 
                        mensagem
                    ]
                    
                    # Correção do TypeError: enviando como lista única
                    sucesso = salvar_formulario_contato(dados_lista)
                    
                    if sucesso:
                        st.balloons()
                        st.success("Mensagem enviada com sucesso!")
                    else:
                        st.error("Falha técnica no envio. Verifique as credenciais do Google.")

if __name__ == "__main__":
    main()

exibir_rodape()
