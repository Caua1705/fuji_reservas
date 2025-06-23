from pathlib import Path

def carregar_credenciais():
    try:
        import streamlit as st
        credenciais_json=st.secrets["CREDENCIAIS_GOOGLE"]
    except FileNotFoundError:
        import json
        caminho_credenciais= Path(__file__).parents[2] / "credenciais.json"
        with open(caminho_credenciais,"r") as credenciais:
            credenciais_json=json.load(credenciais)
    return credenciais_json