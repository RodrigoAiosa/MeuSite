import streamlit as st
from utils import registrar_acesso, exibir_rodape

# 1. Registro automático de acesso à página
registrar_acesso("Página de Contato")

def exibir_contato():
    st.title("📬 Entre em Contato")
    st.write("Preencha o formulário abaixo para enviar sua mensagem.")

    # Criando o formulário de contato
    with st.form("form_contato"):
        nome = st.text_input("Nome Completo", placeholder="Digite seu nome...")
        email = st.text_input("E-mail", placeholder="seuemail@exemplo.com")
        whatsapp = st.text_input("WhatsApp (Somente 11 números com DDD)", placeholder="11999999999")
        mensagem = st.text_area("Sua Mensagem", placeholder="Como posso te ajudar?")

        botao_enviar = st.form_submit_button("Enviar Mensagem")

        if botao_enviar:
            # Validação simples de campos
            if not nome or not email or not mensagem:
                st.error("Por favor, preencha todos os campos obrigatórios (Nome, E-mail e Mensagem).")
            elif "@" not in email or "." not in email:
                st.error("Por favor, insira um e-mail válido.")
            else:
                try:
                    # Registra a ação de envio na planilha usando a estrutura correta:
                    # data_hora | dispositivo | sistema operacional | ip | página
                    registrar_acesso(f"Mensagem enviada por: {nome}")
                    
                    st.success("✅ Mensagem enviada com sucesso! Entrarei em contato em breve.")
                    st.balloons()
                except Exception as e:
                    st.error(f"Erro ao processar o envio: {e}")

    # Exibição do rodapé padrão
    exibir_rodape()

# Executa a função na página
if __name__ == "__main__":
    exibir_contato()
