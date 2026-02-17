import streamlit as st

# --- MENU LATERAL ---
def exibir_menu_lateral():
    st.sidebar.title("Navegação")
    
    # Botões normais para páginas internas
    if st.sidebar.button("🏠 Home"):
        st.session_state.pagina = "home"
    
    # --- BOTÃO DE CONTATO (REDIRECIONAMENTO DIRETO) ---
    # Este bloco substitui o botão comum por um link real que abre seu formulário funcional
    st.sidebar.markdown(
        """
        <a href="https://crud-aiven.streamlit.app/" target="_self" style="text-decoration: none;">
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
                cursor: pointer;
                border: none;">
                📩 Contato
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )

# Chamar a função
exibir_menu_lateral()
