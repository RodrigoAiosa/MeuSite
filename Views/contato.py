import streamlit as st
import re
from datetime import datetime
from utils import exibir_rodape, registrar_acesso, salvar_formulario_contato

# --- REGISTRO DE ACESSO ---
registrar_acesso("Página de Contato")

def validar_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def main():
    # ... (CSS e Header permanecem iguais) ...
    st.title("🚀 Vamos escalar seu projeto?")
    
    with st.form("form_contato", clear_on_submit=True):
        nome = st.text_input("👤 Nome Completo")
        email = st.text_input("📧 E-mail Profissional")
        whatsapp = st.text_input("📱 WhatsApp (11 números)")
        mensagem = st.text_area("💬 Como posso te ajudar?")
        enviar = st.form_submit_button("Enviar Mensagem Agora")

        if enviar:
            if len(nome.strip()) < 10 or not validar_email(email.lower()) or len(whatsapp) != 11:
                st.error("Verifique os campos preenchidos.")
            else:
                with st.spinner("Enviando..."):
                    # AJUSTE: Enviando como lista para evitar TypeError
                    dados_lista = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), nome, email, whatsapp, mensagem]
                    sucesso = salvar_formulario_contato(dados_lista)
                    if sucesso:
                        st.success("Enviado com sucesso!")
                        st.balloons()

if __name__ == "__main__":
    main()
exibir_rodape()
