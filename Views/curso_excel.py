import streamlit as st
import streamlit.components.v1 as components

with open("Views/excel-treino.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=900, scrolling=True)
