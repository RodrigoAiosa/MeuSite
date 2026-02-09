import streamlit as st
from datetime import datetime
from utils import exibir_rodape, salvar_formulario_contato

def main():
    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
    
    with st.form(key="form_contato", clear_on_submit=True):
        nome = st.text_input("👤 Nome Completo")
        email = st.text_input("📧 E-mail Profissional")
        whatsapp = st.text_input("📱 WhatsApp")
        mensagem = st.text_area("💬 Como posso te ajudar?")
        enviar = st.form_submit_button("Enviar Mensagem Agora")

    if enviar:
        if nome and email and whatsapp and mensagem:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            sucesso = salvar_formulario_contato([data_hora, nome, email, whatsapp, mensagem])
            if sucesso:
                st.balloons()
                st.success("✅ Mensagem enviada com sucesso!")
        else:
            st.error("⚠️ Preencha todos os campos.")

if __name__ == "__main__":
    main()
exibir_rodape()
