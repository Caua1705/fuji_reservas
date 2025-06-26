from pathlib import Path

def carregar_credenciais_google():
    try:
        import streamlit as st
        credenciais_google=st.secrets["CREDENCIAIS_GOOGLE"]
    except FileNotFoundError:
        import json
        caminho_credenciais_google = Path(__file__).parents[2] / "credenciais_google.json"
        with open(caminho_credenciais_google,"r") as credenciais:
            credenciais_google=json.load(credenciais)
    return credenciais_google

def carregar_credenciais_email():
    try:
        import streamlit as st
        email_origem=st.secrets["email"]["origem"]
        senha_app=st.secrets["email"]["senha_app"]
    except FileNotFoundError:
        import json
        caminho_credenciais_email = Path(__file__).parents[2] / "email_config.json"
        with open(caminho_credenciais_email,"r") as credenciais:
            credenciais_google=json.load(credenciais)
        email_origem=credenciais_google["origem"]
        senha_app=credenciais_google["senha_app"]
    return email_origem,senha_app
