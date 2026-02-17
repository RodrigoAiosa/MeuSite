import streamlit as st

# No seu menu lateral (sidebar)
st.sidebar.title("Entre em contato")

# Botão estilizado que redireciona para o formulário funcional
st.sidebar.markdown(
    f"""
    <a href="https://crud-aiven.streamlit.app/" target="_self" style="text-decoration: none;">
        <div style="
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #00b4d8;
            color: white;
            padding: 12px;
            border-radius: 8px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            width: 100%;">
            📩 Ir para Formulário de Contato
        </div>
    </a>
    """,
    unsafe_allow_html=True
)
