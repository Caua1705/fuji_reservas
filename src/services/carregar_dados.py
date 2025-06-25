import pandas as pd
from src.model.reservas_model import ler_todas_reservas
from src.data.conexao import conectar_planilha
from src.utils.formatadores import formatar_dados
from src.utils.formatadores import COLUNAS_RESERVA

def obter_dados_brutos():
    abas = conectar_planilha()
    aba_reservas = abas[0]
    return ler_todas_reservas(aba_reservas)


def carregar_df_reservas():
    todas_reservas = obter_dados_brutos()
    
    if not todas_reservas or len(todas_reservas) < 2:
        dados = []
        colunas = COLUNAS_RESERVA
    else:
        colunas = todas_reservas[0]
        dados = todas_reservas[1:]

    df = pd.DataFrame(dados, columns=colunas)
    df = formatar_dados(df)
    return df

