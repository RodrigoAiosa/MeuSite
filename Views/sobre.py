import streamlit as st

# --- ESTILO CSS PARA A FOTO, LAYOUT E ÍCONES CENTRALIZADOS ---
st.markdown(
    """
    <style>
    .profile-pic {
        display: flex;
        justify-content: center;
        margin-top: -30px;
    }
    .profile-pic img {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        border: 5px solid #00b4d8;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .main-title {
        text-align: center;
        margin-top: 10px;
    }
    /* Centralização e remoção de bordas dos botões sociais */
    .social-icons {
        display: flex;
        justify-content: center;
        gap: 30px; /* Espaço entre os ícones */
        margin-top: 20px;
    }
    .social-icons a {
        transition: transform 0.3s;
        text-decoration: none;
    }
    .social-icons a:hover {
        transform: scale(1.2); /* Efeito de zoom ao passar o mouse */
    }
    .social-icons img {
        width: 50px; /* Tamanho dos ícones */
        height: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- CABEÇALHO COM FOTO ---
st.markdown(
    '<div class="profile-pic">'
    '<img src="https://media.licdn.com/dms/image/v2/D5603AQH-2rDkpd-OxA/profile-displayphoto-scale_200_200/B56ZmxqxTBKMAY-/0/1759622405960?e=1772064000&v=beta&t=_6-zEhPhGUF9GQwDJ-7OZ0DtlWLD4AJBwI5kPsz-X6U">'
    '</div>',
    unsafe_allow_html=True
)

st.markdown('<h1 class="main-title">Rodrigo Aiosa</h1>', unsafe_allow_html=True)

# --- SKILLS RÁPIDAS ---
st.write("")
st.markdown("""
<div style="text-align: center; font-size: 1.2em; color: #00b4d8; font-weight: bold;">
Python | Excel | Power BI | ETL | SQL SERVER | Linguagem M | DAX
</div>
""", unsafe_allow_html=True)

st.info("Minha expertise envolve a criação de relatórios interativos e a busca por soluções inovadoras para a otimização de processos.")

st.markdown("---")

# --- SEÇÃO: EXPERIÊNCIA DE MERCADO (TEXTO INTEGRAL) ---
st.subheader("🤝 Experiência de Mercado")

st.write("""
Especialista em Análise de Dados e Business Intelligence, com uma trajetória focada em transformar dados complexos em insights estratégicos que geram eficiência de processos e melhoram a tomada de decisão.

Atuo na implementação de projetos de dados **end-to-end**, desde a extração e transformação até a visualização final, utilizando uma stack tecnológica robusta:
""")

# Organização da Stack em colunas para melhor leitura
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🐍 Análise Avançada e Automação")
    st.write("Proficiência em **Python** para análise avançada e automação, e **Excel** para manipulação e modelagem de dados.")

    st.markdown("#### 📊 Business Intelligence (BI)")
    st.write("Expertise no **Power BI** para visualização dinâmica, incluindo a criação de modelos robustos com **DAX** (cálculos complexos) e a utilização da **Linguagem M** (para transformação eficiente de dados via Power Query).")

with col2:
    st.markdown("#### 🗄️ Gerenciamento de Dados")
    st.write("Sólidas habilidades em **SQL Server** e processos de **ETL**, garantindo a gestão eficiente e a integridade total dos bancos de dados.")

    st.markdown("#### 🎯 Minha Abordagem")
    st.write("Minha abordagem é orientada a resultados e focada na busca por soluções inovadoras que aumentem a eficiência operacional e forneçam uma base sólida para decisões estratégicas.")

st.write("")
st.write("Tenho orgulho de ter impulsionado resultados e fornecido inteligência de dados para clientes de alto nível como: **Cimed, Unimed Seguros, Ouro Safra, Kraft Heinz, Loggi, Usina Santa Terezinha, Megavig, Lowell e BSS Blindagens entre outros.**")

st.markdown("---")

# --- ÍCONES SOCIAIS CENTRALIZADOS E SEM BORDAS ---
st.markdown(
    f'''
    <div class="social-icons">
        <a href="https://www.linkedin.com/in/rodrigoaiosa/" target="_blank">
            <img src="https://images.icon-icons.com/99/PNG/96/linkedin_socialnetwork_17441.png" alt="LinkedIn">
        </a>
        <a href="https://wa.me/5511977019335" target="_blank">
            <img src="https://images.icon-icons.com/99/PNG/96/whatsapp_socialnetwork_17360.png" alt="WhatsApp">
        </a>
    </div>
    ''',
    unsafe_allow_html=True
)