import gspread
from google.oauth2.service_account import Credentials
from src.data.credenciais import carregar_credenciais_google

def conectar_planilha():
    acesso = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    credenciais_google=carregar_credenciais_google()

    credenciais = Credentials.from_service_account_info(
        credenciais_google,
        scopes=acesso
    )

    cliente = gspread.authorize(credenciais)  

    planilha = cliente.open("reservas_fuji")
    aba = planilha.get_worksheet(0)
    aba2=planilha.get_worksheet(1)
    aba3=planilha.get_worksheet(2)

    return aba,aba2,aba3