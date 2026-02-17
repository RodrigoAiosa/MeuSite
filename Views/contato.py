import streamlit as st
import re
import urllib.parse
from datetime import datetime
from utils import exibir_rodape, salvar_formulario_contato, registrar_acesso

# Registro de acesso para controle interno no CRUD Aiven
registrar_acesso("Contato")

def validar_email(email):
    # Regex para validar e-mails profissionais
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def gerar_link_whatsapp(nome, mensagem_usuario):
    # Mensagem personalizada baseada no pedido do usuário
    texto = f"Olá Rodrigo! Meu nome é {nome}. Gostaria de conversar sobre: {mensagem_usuario}"
    texto_encoded = urllib.parse.quote(texto)
    # Seu WhatsApp: 11977019335
    return f"https://wa.me/5511977019335?text={texto_encoded}"

def main():
    # Título estilizado conforme o padrão visual da página
    st.markdown("<h1 style='text-align: center; color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>", unsafe_allow_html=True)
    
    # Banner informativo - Substituindo Calendly por contato direto
    st.info("📅 **Deseja marcar uma reunião ou falar sobre um projeto?** Preencha o formulário abaixo para registrar seu interesse e me chame no WhatsApp.")

    with st.form("form_contato_aiven", clear_on_submit=True):
        nome = st.text_input("👤 Nome Completo")
        email = st.text_input("📧 E-mail Profissional")
        whatsapp_contato = st.text_input("📱 Seu WhatsApp (11 números)")
        mensagem = st.text_area("💬 Como posso te ajudar? (Ex: Quero marcar uma reunião, orçamento, etc.)")
        
        enviar = st.form_submit_button("Enviar Dados e Abrir WhatsApp")

        if enviar:
            # Validações antes de processar
            if len(nome.strip()) < 5:
                st.error("Por favor, insira seu nome completo.")
            elif not validar_email(email.lower()):
                st.error("Por favor, utilize um e-mail válido.")
            elif not (whatsapp_contato.isdigit() and len(whatsapp_contato) == 11):
                st.error("WhatsApp inválido. Use o formato: 11999999999.")
            elif not mensagem.strip():
                st.error("A mensagem não pode estar vazia.")
            else:
                with st.spinner("Integrando dados ao CRUD Aiven..."):
                    # Preparação da lista de dados para salvar e preservar histórico
                    dados_lista = [
                        datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 
                        nome, 
                        email, 
                        whatsapp_contato, 
                        mensagem
                    ]
                    
                    # Salva no banco de dados via utils
                    sucesso = salvar_formulario_contato(dados_lista)
                    
                    if sucesso:
                        st.balloons()
                        st.success("Dados salvos com sucesso no sistema!")
                        
                        # Link dinâmico do WhatsApp
                        link_wa = gerar_link_whatsapp(nome, mensagem)
                        
                        # Bloco de Call to Action para Reunião/WhatsApp
                        st.markdown(f"""
                            <div style="text-align: center; padding: 25px; border: 2px solid #00b4d8; border-radius: 15px; background-color: #0e1117; margin-top: 20px;">
                                <h3 style="color: #00b4d8; margin-bottom: 15px;">✅ Registro Concluído!</h3>
                                <p style="font-size: 1.1em;">Agora, clique no botão abaixo para <b>confirmar nossa reunião</b> e iniciar o atendimento:</p>
                                <a href="{link_wa}" target="_blank" style="background-color: #25d366; color: white; padding: 15px 30px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block; box-shadow: 0px 4px 15px rgba(37, 211, 102, 0.3);">
                                    💬 Iniciar Conversa Agora
                                </a>
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("Erro ao conectar com o banco de dados Aiven. Verifique suas credenciais.")

if __name__ == "__main__":
    main()

# Rodapé padrão do projeto
exibir_rodape()
