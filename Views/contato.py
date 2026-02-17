import streamlit as st
import re
import urllib.parse
from datetime import datetime
from utils import exibir_rodape, salvar_formulario_contato, registrar_acesso

# Registro de acesso para controle interno
registrar_acesso("Contato")

def validar_email(email):
    # Regex para validar e-mails profissionais
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def gerar_link_whatsapp(nome, mensagem_usuario):
    # Mensagem personalizada conforme a regra de negócio
    texto = f"Olá Rodrigo! Meu nome é {nome}. Gostaria de falar sobre: {mensagem_usuario}"
    texto_encoded = urllib.parse.quote(texto)
    # Seu WhatsApp: 11977019335
    return f"https://wa.me/5511977019335?text={texto_encoded}"

def main():
    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
    
    # Banner informativo (conforme o print enviado)
    st.info("📅 **Deseja marcar uma reunião ou falar sobre um projeto?** Use o formulário abaixo ou me chame diretamente.")

    with st.form("form_contato", clear_on_submit=True):
        nome = st.text_input("👤 Nome Completo")
        email = st.text_input("📧 E-mail Profissional")
        whatsapp_contato = st.text_input("📱 Seu WhatsApp (11 números)")
        mensagem = st.text_area("💬 Como posso te ajudar? (Ex: Quero marcar uma reunião, comprar um serviço...)")
        
        enviar = st.form_submit_button("Enviar Mensagem e Abrir Conversa")

        if enviar:
            # Validações rigorosas
            if len(nome.strip()) < 5:
                st.error("Por favor, insira seu nome completo.")
            elif not validar_email(email.lower()):
                st.error("E-mail profissional inválido.")
            elif not (whatsapp_contato.isdigit() and len(whatsapp_contato) == 11):
                st.error("WhatsApp deve ter 11 dígitos (DDD + número).")
            elif not mensagem.strip():
                st.error("Por favor, descreva como posso te ajudar.")
            else:
                with st.spinner("Salvando dados e preparando contato..."):
                    # Preparação dos dados para salvar (Preservando existentes)
                    dados_lista = [
                        datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 
                        nome, 
                        email, 
                        whatsapp_contato, 
                        mensagem
                    ]
                    
                    # Chamada da função para salvar no banco de dados/planilha
                    sucesso = salvar_formulario_contato(dados_lista)
                    
                    if sucesso:
                        st.balloons()
                        st.success("Dados registrados com sucesso!")
                        
                        # Geração do hiperlink personalizado do WhatsApp
                        link_wa = gerar_link_whatsapp(nome, mensagem)
                        
                        # Exibição do link de reunião/contato (substituindo Calendly)
                        st.markdown(f"""
                            <div style="text-align: center; padding: 20px; border: 2px solid #00b4d8; border-radius: 10px; background-color: #0e1117;">
                                <h3 style="color: #00b4d8;">✅ Tudo pronto!</h3>
                                <p>Clique no botão abaixo para agendar nossa reunião ou iniciar a conversa:</p>
                                <a href="{link_wa}" target="_blank" style="background-color: #25d366; color: white; padding: 12px 24px; text-decoration: none; border-radius: 5px; font-weight: bold; display: inline-block; transition: 0.3s;">
                                    🚀 Falar com Rodrigo no WhatsApp
                                </a>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("Houve um erro ao salvar os dados. Verifique a conexão com o banco.")

if __name__ == "__main__":
    main()

exibir_rodape()
