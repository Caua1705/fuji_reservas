import json
import streamlit as st
from src.config.paths import CAMINHOS

def buscar_credenciais(chave_secrets, caminho_json):
    try:
        return st.secrets[chave_secrets]
    except FileNotFoundError:
        with open(caminho_json, "r") as credenciais:
            return json.load(credenciais)


def get_credenciais_google():
    return buscar_credenciais("CREDENCIAIS_GOOGLE", CAMINHOS["Credenciais_google"])


def get_credenciais_email():
    dados = buscar_credenciais("CREDENCIAIS_EMAIL", CAMINHOS["Credenciais_email"])
    return dados["origem"], dados["senha_app"]

