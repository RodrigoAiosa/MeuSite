import streamlit as st
import random
import json
import os
from datetime import datetime
import urllib.parse
from utils import exibir_rodape, registrar_acesso

# -----------------------------------------
# REGISTRO DE ACESSO DA PÁGINA
# -----------------------------------------
registrar_acesso("Projetos Power BI")

# -----------------------------------------
# FUNÇÕES DE CONTADOR
# -----------------------------------------

def carregar_contador(nome_projeto):
    arquivo = f"contador_{nome_projeto}.json"

    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            return json.load(f)
    else:
        return {
            "total": 0,
            "ultimo_dia": datetime.now().strftime("%Y-%m-%d"),
            "visitas_dia": random.randint(200, 500)
        }

def salvar_contador(nome_projeto, dados):
    arquivo = f"contador_{nome_projeto}.json"
    with open(arquivo, "w") as f:
        json.dump(dados, f)

def gerar_visualizacoes(nome_projeto):
    dados = carregar_contador(nome_projeto)

    hoje = datetime.now()
    hoje_str = hoje.strftime("%Y-%m-%d")

    # Se mudou o dia, sorteia novo volume diário
    if dados["ultimo_dia"] != hoje_str:
        dados["total"] += dados["visitas_dia"]
        dados["visitas_dia"] = random.randint(200, 500)
        dados["ultimo_dia"] = hoje_str

    # Crescimento ao longo do dia (proporcional à hora atual)
    hora_decimal = hoje.hour + (hoje.minute / 60)
    percentual_dia = hora_decimal / 24

    visitas_hoje_parcial = int(dados["visitas_dia"] * percentual_dia)

    total_atual = dados["total"] + visitas_hoje_parcial

    salvar_contador(nome_projeto, dados)

    return total_atual

def registrar_clique(nome_projeto):
    dados = carregar_contador(nome_projeto)
    dados["total"] += 1
    salvar_contador(nome_projeto, dados)

# -----------------------------------------
# ESTILO CSS (mantido igual ao seu)
# -----------------------------------------

st.markdown(""" 
<style>
.counter {
    margin-bottom: 10px;
    font-size: 0.85rem;
    color: #00b4d8;
    font-weight: bold;
}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
""", unsafe_allow_html=True)

# -----------------------------------------
# PROJETOS
# -----------------------------------------

pbi_projects = [
    {"id":"stone","title":"💳 Relatório STONE","icon":"🏛️","url":"https://app.powerbi.com/view?r=STONE","desc":"Dashboard interativo de Faturamento B2B."},
    {"id":"meta","title":"📊 Vendas Meta vs Realizado","icon":"📈","url":"https://app.powerbi.com/view?r=META","desc":"Dashboard de Recrutamento e Seleção."},
    {"id":"bnz","title":"📦 Controle de Pedidos BNZ","icon":"📦","url":"https://app.powerbi.com/view?r=BNZ","desc":"Dashboard de Gestão de Estoque."},
]

# -----------------------------------------
# RENDERIZAÇÃO
# -----------------------------------------

for p in pbi_projects:

    views = gerar_visualizacoes(p["id"])

    wa_text = f"Olá Rodrigo! Gostaria de falar sobre o projeto 🚀 *{p['title']}* que vi no seu portfólio."
    wa_link = f"https://api.whatsapp.com/send?phone=5511977019335&text={urllib.parse.quote(wa_text)}"

    if st.button(f"Abrir {p['title']}", key=p["id"]):
        registrar_clique(p["id"])
        st.markdown(f"<script>window.open('{p['url']}')</script>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="margin-bottom:20px;">
        <div style="font-size:1.2rem; font-weight:bold;">{p['title']}</div>
        <div class="counter">👁️ {views:,} visualizações</div>
        <div style="color:#9ca3af;">{p['desc']}</div>
        <a href="{wa_link}" target="_blank">WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

exibir_rodape()
