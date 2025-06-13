import gspread
from google.oauth2.service_account import Credentials
import streamlit as st

@st.cache_data(show_spinner=False)
def conectar_planilha():
    acesso = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    credenciais = Credentials.from_service_account_file("credenciais.json", scopes=acesso)
    cliente = gspread.authorize(credenciais)

    planilha = cliente.open("reservas_fuji")
    aba = planilha.sheet1

    return aba

st.cache_data