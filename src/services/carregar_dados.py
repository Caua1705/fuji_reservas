import pandas as pd
from src.config.settings import COLUNAS_PLANILHA_RESERVAS   
from src.model.reservas_model import ler_todas_reservas
from src.utils.formatadores import formatar_dados

def obter_dados_brutos(aba):
    todas_reservas = ler_todas_reservas(aba)
    return todas_reservas


def carregar_df_reservas(aba_reservas):
    todas_reservas = obter_dados_brutos(aba_reservas)
    
    if not todas_reservas or len(todas_reservas) < 2:
        dados = []
        colunas = COLUNAS_PLANILHA_RESERVAS  
    else:
        colunas = todas_reservas[0]
        dados = todas_reservas[1:]

    df = pd.DataFrame(dados, columns=colunas)
    df = formatar_dados(df)
    return df

