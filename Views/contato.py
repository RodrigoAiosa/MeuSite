import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import re

def salvar_contato(dados):
    # Configuração de escopo e credenciais
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # Certifique-se de que este arquivo JSON está na mesma pasta do seu script
    creds = ServiceAccountCredentials.from_json_keyfile_name("meuprojetocadsite-5ecb421b15a7.json", scope)
    client = gspread.authorize(creds)
    
    # URL da sua planilha conforme verificado nas configurações de compartilhamento
    url = "https://docs.google.com/spreadsheets/d/1JXVHEK4qjj4CJUdfaapKjBxl_WFmBDFHMJyIItxfchU/edit#gid=0"
    sheet = client.open_by_url(url).sheet1
    
    # Adiciona a nova linha ao final, preservando todos os registros anteriores
    sheet.append_row(dados)

def validar_email(email):
    # Regex para validação de e-mail padrão
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return re.search(regex, email)

def main():
    # --- INJEÇÃO DE CSS PARA EFEITO VISUAL ---
    st.markdown("""
        <style>
        /* Transição suave para os campos */
        div[data-baseweb="input"] > div, div[data-baseweb="textarea"] > div {
            transition: all 0.3s ease-in-out !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        
        /* Brilho Roxo ao posicionar o mouse (Hover) */
        div[data-baseweb="input"]:hover > div, div[data-baseweb="textarea"]:hover > div {
            border-color: #8A2BE2 !important;
            box-shadow: 0 0 10px rgba(138, 43, 226, 0.4) !important;
        }

        /* Brilho Roxo ao clicar no campo (Focus) */
        div[data-baseweb="input"]:focus-within > div, div[data-baseweb="textarea"]:focus-within > div {
            border-color: #9400D3 !important;
            box-shadow: 0 0 15px rgba(148, 0, 211, 0.7) !important;
        }
        
        /* Personalização opcional do botão para combinar */
        button[kind="primaryFormSubmit"] {
            background-color: #8A2BE2 !important;
            border: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("📬 Entre em Contato")
    st.write("Preencha o formulário abaixo para enviar sua mensagem.")

    with st.form(key="form_contato", clear_on_submit=True):
        nome = st.text_input("Nome Completo")
        email = st.text_input("E-mail")
        whatsapp = st.text_input("WhatsApp (Somente 11 números com DDD)")
        mensagem = st.text_area("Sua Mensagem")
        
        botao_enviar = st.form_submit_button("Enviar Mensagem")

    if botao_enviar:
        # --- VALIDAÇÕES COM REGEX E LÓGICA ---
        
        # 1. Nome com no mínimo 10 caracteres
        if len(nome.strip()) < 10:
            st.error("❌ O nome deve ter no mínimo 10 caracteres.")
        
        # 2. Validação de E-mail via Regex
        elif not validar_email(email.lower()):
            st.error("❌ Por favor, insira um e-mail válido.")
        
        # 3. WhatsApp: Somente números e exatamente 11 dígitos
        elif not (whatsapp.isdigit() and len(whatsapp) == 11):
            st.error("❌ O WhatsApp deve conter apenas números e ter exatamente 11 dígitos (Ex: 11999998888).")
            
        elif not mensagem:
            st.error("❌ Por favor, preencha o campo de mensagem.")
            
        else:
            try:
                # Gerar timestamp para o registro
                data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                # Organização dos dados para a planilha
                lista_dados = [data_hora, nome, email, whatsapp, mensagem]
                
                # Salva no Google Sheets (Append Mode)
                salvar_contato(lista_dados)
                st.success("✅ Mensagem enviada e salva com sucesso!")
                
            except Exception as e:
                # Exibe o erro caso a API falhe (mesmo após ativação)
                st.error(f"Erro crítico ao conectar com a planilha: {e}")

    # Rodapé padrão Rodrigo AIOSA
    st.markdown("---")
    footer_html = """
    <div style='text-align: center; color: gray;'>
        <p style='margin-bottom: 5px;'>Desenvolvido por <b>Rodrigo AIOSA</b></p>
        <div style='display: flex; justify-content: center; gap: 20px; font-size: 24px;'>
            <a href='https://wa.me/5511977019335' target='_blank'>
                <img src='https://cdn-icons-png.flaticon.com/512/733/733585.png' width='25' height='25'>
            </a>
            <a href='https://www.linkedin.com/in/rodrigoaiosa/' target='_blank'>
                <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='25' height='25'>
            </a>
        </div>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()