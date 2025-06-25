import pandas as pd
from src.model.reservas_model import ler_todas_reservas
from src.data.conexao import conectar_planilha
from src.utils.formatadores import formatar_dados
from src.utils.formatadores import COLUNAS_RESERVA

def obter_dados_brutos(aba):
    abas = conectar_planilha()
    todas_reservas = ler_todas_reservas(abas[aba])
    return todas_reservas


def carregar_df_reservas(aba):
    todas_reservas = obter_dados_brutos(aba)
    
    if not todas_reservas or len(todas_reservas) < 2:
        dados = []
        colunas = COLUNAS_RESERVA
    else:
        colunas = todas_reservas[0]
        dados = todas_reservas[1:]

    df = pd.DataFrame(dados, columns=colunas)
    df = formatar_dados(df)
    return df

