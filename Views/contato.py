import streamlit as st
from utils import registrar_acesso, exibir_rodape, registrar_formulario_contato
import time # Adicionado para controlar o tempo antes do F5

# 1. Registro automático de visita
registrar_acesso("Página de Contato")

def exibir_contato():
    st.title("📬 Entre em Contato")
    st.write("Preencha o formulário abaixo para enviar sua mensagem.")

    # Criando o formulário de contato
    with st.form("form_contato", clear_on_submit=True): # clear_on_submit limpa os campos visualmente
        nome = st.text_input("Nome Completo", placeholder="Digite seu nome...")
        email = st.text_input("E-mail", placeholder="seuemail@exemplo.com")
        whatsapp = st.text_input("WhatsApp (Somente 11 números com DDD)", placeholder="11999999999")
        mensagem = st.text_area("Sua Mensagem", placeholder="Como posso te ajudar?")

        botao_enviar = st.form_submit_button("Enviar Mensagem")

        if botao_enviar:
            if not nome or not email or not mensagem:
                st.error("Por favor, preencha todos os campos obrigatórios.")
            elif "@" not in email or "." not in email:
                st.error("Por favor, insira um e-mail válido.")
            else:
                try:
                    # 2. Registro na planilha de contatos
                    sucesso = registrar_formulario_contato(nome, email, whatsapp, mensagem)
                    
                    if sucesso:
                        st.success("✅ Mensagem enviada com sucesso! Atualizando...")
                        st.balloons()
                        
                        # Aguarda 3 segundos para o usuário ler a mensagem e ver os balões
                        time.sleep(3)
                        
                        # Executa o "F5" (Rerun) da página
                        st.rerun()
                    else:
                        st.error("❌ Erro ao salvar na planilha. Verifique as permissões.")
                        
                except Exception as e:
                    st.error(f"Erro ao processar o envio: {e}")

    exibir_rodape()

if __name__ == "__main__":
    exibir_contato()
