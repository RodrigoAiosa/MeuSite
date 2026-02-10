import streamlit as st
import re
from datetime import datetime

from utils import (
    exibir_rodape,
    registrar_acesso,
    salvar_formulario_contato
)

# --- REGISTRO DE ACESSO ---
registrar_acesso("Página de Contato")


def validar_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)


def main():
    # --- CSS ---
    st.markdown("""
        <style>
        .stForm {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px !important;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.37);
        }

        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background-color: rgba(15, 23, 42, 0.6) !important;
            border-radius: 12px !important;
            border: 1px solid rgba(0, 180, 216, 0.2) !important;
        }

        button[kind="primaryFormSubmit"] {
            width: 100%;
            background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%) !important;
            color: white !important;
            border-radius: 12px !important;
            font-weight: bold !important;
        }

        .contact-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    st.markdown("""
        <div class='contact-header'>
            <h1 style='color: #00b4d8;'>🚀 Vamos escalar seu projeto?</h1>
            <p style='color: #94a3b8; font-size: 1.1rem;'>
                Preencha os dados abaixo e entrarei em contato em até 24h.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.form("form_contato", clear_on_submit=True):
            nome = st.text_input("👤 Nome Completo")

            c1, c2 = st.columns(2)
            with c1:
                email = st.text_input("📧 E-mail Profissional")
            with c2:
                whatsapp = st.text_input("📱 WhatsApp (DDD + número)")

            mensagem = st.text_area("💬 Como posso te ajudar?", height=150)

            enviar = st.form_submit_button("Enviar Mensagem Agora")

        if enviar:
            if len(nome.strip()) < 10:
                st.error("O nome deve ter no mínimo 10 caracteres.")

            elif not validar_email(email.lower()):
                st.error("Digite um e-mail válido.")

            elif not (whatsapp.isdigit() and len(whatsapp) == 11):
                st.error("WhatsApp deve conter 11 números.")

            elif not mensagem:
                st.error("Escreva sua mensagem.")

            else:
                with st.spinner("Enviando mensagem..."):
                    # AJUSTE: Transformando os campos em uma LISTA única para a função
                    dados_lista = [
                        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        nome,
                        email,
                        whatsapp,
                        mensagem
                    ]
                    
                    # Chamada corrigida passando apenas 1 argumento (a lista)
                    sucesso = salvar_formulario_contato(dados_lista)

                if sucesso:
                    st.balloons()
                    st.success("Mensagem enviada com sucesso!")


if __name__ == "__main__":
    main()

exibir_rodape()
