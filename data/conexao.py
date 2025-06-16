import gspread
from google.oauth2.service_account import Credentials
import streamlit as st

def conectar_planilha():
    acesso = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    credenciais = Credentials.from_service_account_info(
        st.secrets["CREDENCIAIS_JSON"],
        scopes=acesso
    )

    cliente = gspread.authorize(credenciais)  # já é suficiente

    planilha = cliente.open("reservas_fuji")
    aba = planilha.sheet1

    return aba