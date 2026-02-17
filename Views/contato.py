import streamlit as st
import re
from datetime import datetime
from utils import exibir_rodape, salvar_formulario_contato, registrar_acesso

# Registro de acesso para controle interno no CRUD Aiven
registrar_acesso("Contato")

def validar_whatsapp(numero):
    # Remove caracteres não numéricos e verifica se tem 11 dígitos
    apenas_numeros = re.sub(r'\D', '', numero)
    return len(apenas_numeros) == 11

def main():
    # Título estilizado
    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
    
    # Subtítulo conforme imagem 2
    st.markdown("<p style='text-align: center;'>Preencha os campos abaixo para registrar sua solicitação em nossa base de dados.</p>", unsafe_allow_html=True)

    with st.form("contato_form", clear_on_submit=True):
        # Campos com os placeholders idênticos à sua imagem de referência
        nome = st.text_input("👤 Nome Completo", placeholder="Digite seu nome aqui...")
        email = st.text_input("📧 E-mail Profissional", placeholder="exemplo@email.com")
        whatsapp = st.text_input("📱 WhatsApp", placeholder="11999999999", max_chars=11)
        mensagem = st.text_area("💬 Sua Mensagem", placeholder="Como podemos ajudar?")
        
        submit_button = st.form_submit_button("Enviar Mensagem")

        if submit_button:
            # Validações
            if not nome or not email or not whatsapp or not mensagem:
                st.error("⚠️ Por favor, preencha todos os campos.")
            elif not validar_whatsapp(whatsapp):
                st.error("⚠️ O WhatsApp deve conter exatamente 11 números (DDD + número).")
            else:
                with st.spinner("Enviando dados para o banco Aiven..."):
                    # Preparação da lista para a função salvar_formulario_contato
                    # Formato: [Data/Hora, Nome, Email, WhatsApp, Mensagem]
                    dados_lista = [
                        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        nome,
                        email,
                        whatsapp,
                        mensagem
                    ]
                    
                    # Persistência no Banco Aiven (via utils)
                    sucesso = salvar_formulario_contato(dados_lista)
                    
                    if sucesso:
                        st.balloons()
                        st.success("✅ Mensagem enviada com sucesso! Logo entraremos em contato.")
                    else:
                        # Erro amigável caso a conexão falhe
                        st.error("❌ Ocorreu um erro ao salvar os dados. Verifique a conexão com o banco Aiven.")

if __name__ == "__main__":
    main()

# Rodapé padrão do sistema
exibir_rodape()
