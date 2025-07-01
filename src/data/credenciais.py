import json
import streamlit as st
from src.config.paths import CAMINHOS

def buscar_credenciais(chave_secrets, caminho_json):
    try:
        return st.secrets[chave_secrets]
    except FileNotFoundError:
<<<<<<< HEAD
        import json
        caminho_credenciais_google = Path(__file__).parents[2] / "credenciais_google.json"
        with open(caminho_credenciais_google,"r") as credenciais:
            credenciais_google=json.load(credenciais)
    return credenciais_google
=======
        with open(caminho_json,"r") as credenciais:
            return json.load(credenciais)


def get_credenciais_google():
    return buscar_credenciais("CREDENCIAIS_GOOGLE",CAMINHOS["Credenciais_google"])


def get_credenciais_email():
    dados = buscar_credenciais("email",CAMINHOS["Credenciais_email"])
    return dados["origem"], dados["senha_app"]
>>>>>>> refatorando_codigos

