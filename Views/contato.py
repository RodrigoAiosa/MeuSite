import streamlit as st
from utils import salvar_formulario_contato, exibir_rodape

st.title("📬 Entre em Contato")
st.write("Preencha o formulário abaixo para enviar sua mensagem.")

with st.form("form_contato_site", clear_on_submit=True):
    nome = st.text_input("Nome Completo")
    email = st.text_input("E-mail")
    whatsapp = st.text_input("WhatsApp (DDD + Número)")
    mensagem = st.text_area("Sua Mensagem")
    
    submit = st.form_submit_button("Enviar Mensagem")

if submit:
    if nome and email and mensagem:
        # Chama a função que preserva os dados existentes
        com_sucesso = salvar_formulario_contato([nome, email, whatsapp, mensagem])
        if com_sucesso:
            st.success("Sua mensagem foi enviada com sucesso! Obrigado pelo contato.")
    else:
        st.warning("Por favor, preencha todos os campos obrigatórios (Nome, E-mail e Mensagem).")

exibir_rodape()
