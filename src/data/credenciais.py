import json
import streamlit as st
from src.utils.paths import caminhos

def buscar_credenciais(chave_secrets, caminho_json):
    try:
        return st.secrets[chave_secrets]
    except FileNotFoundError:
        with open(caminho_json,"r") as credenciais:
            return json.load(credenciais)


def get_credenciais_google():
    return buscar_credenciais("CREDENCIAIS_GOOGLE",caminhos["Credenciais_google"])


def get_credenciais_email():
    dados = buscar_credenciais("email",caminhos["Credenciais_email"])
    return dados["origem"], dados["senha_app"]

