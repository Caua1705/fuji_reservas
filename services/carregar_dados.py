import pandas as pd
from data.conexao import conectar_planilha

def carregar_dataframe():
    aba = conectar_planilha()
    dados = aba.get_all_records()
    return pd.DataFrame(dados)
    