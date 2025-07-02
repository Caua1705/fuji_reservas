import pandas as pd
from src.services.filtrar import filtrar_dataframe_data
from src.services.validacoes import validar_nova_reserva
from src.utils.formatadores import formatar_data_para_string, formatar_dados

def criar_linha_reserva(dict_dados, colunas):
    return [str(dict_dados[campo]) for campo in colunas]


def gerar_dataframe_reserva(dict_dados, colunas):
    linha  = criar_linha_reserva(dict_dados, colunas)
    linha[0] = formatar_data_para_string(dict_dados["Data"])
    df = pd.DataFrame([linha], columns=colunas)
    df = formatar_dados(df)
    return df, linha 


def preparar_reserva_para_salvar(df_reservas, data, dict_dados, maximo_reservas):
    df_nova_linha, nova_linha  = gerar_dataframe_reserva(dict_dados, df_reservas.columns)
    df_atualizado = pd.concat([df_reservas, df_nova_linha], ignore_index=True)

    df_do_dia = filtrar_dataframe_data(df_atualizado, data)
    validar_nova_reserva(df_do_dia, maximo_reservas)
    return df_atualizado, nova_linha

