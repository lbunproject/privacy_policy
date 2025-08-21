# app.py
import pathlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Privacy Policy — WESO Miner", layout="wide")

# Hide Streamlit chrome (optional)
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

html_path = pathlib.Path("privacy_policy.html")
html = html_path.read_text(encoding="utf-8")

# Render the full HTML document inside an iframe
components.html(html, height=1400, scrolling=True)
