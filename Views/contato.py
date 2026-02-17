import streamlit as st

# --- CONFIGURAÇÃO DO MENU LATERAL ---
def exibir_menu_lateral():
    st.sidebar.title("Menu")
    
    # Botões de navegação interna
    if st.sidebar.button("🏠 Home"):
        st.session_state.pagina = "home"
    
    if st.sidebar.button("👤 Sobre Mim"):
        st.session_state.pagina = "sobre"

    # --- BOTÃO DE CONTATO (REDIRECIONAMENTO EXTERNO) ---
    # Usando Markdown com CSS para parecer um botão do Streamlit, mas abrindo o link do CRUD Aiven
    st.sidebar.markdown(
        """
        <a href="https://crud-aiven.streamlit.app/" target="_blank" style="text-decoration: none;">
            <div style="
                display: flex;
                align-items: center;
                justify-content: center;
                background-color: #00b4d8;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
                margin-top: 10px;
                border: none;">
                📩 Contato (Formulário)
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

# --- EXECUÇÃO ---
exibir_menu_lateral()
