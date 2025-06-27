import gspread
from src.config.settings import SCOPES
from google.oauth2.service_account import Credentials
from src.data.credenciais import get_credenciais_google

def conectar_planilha():
    credenciais_google = get_credenciais_google()
    credenciais = Credentials.from_service_account_info(credenciais_google,scopes=SCOPES)
    cliente = gspread.authorize(credenciais) 
    return cliente 


def get_abas():
    cliente = conectar_planilha()
    planilha = cliente.open("reservas_fuji")
    return [planilha.get_worksheet(i) for i in range(3)]