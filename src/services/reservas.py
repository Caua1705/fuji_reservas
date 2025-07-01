import pandas as pd
from src.model.reservas_model import registrar_reserva
from src.services.filtrar import filtrar_dataframe_data
from src.services.validacoes import validar_nova_reserva
from src.utils.formatadores import formatar_data_para_string, formatar_dados

def criar_linha_reserva(dict_dados, colunas):
    return [str(dict_dados[campo]) for campo in colunas]


def gerar_dataframe_reserva(dict_dados, colunas):
    lista_nova_linha = criar_linha_reserva(dict_dados, colunas)
    lista_nova_linha[0] = formatar_data_para_string(dict_dados["Data"])
    df_nova_linha = pd.DataFrame([lista_nova_linha], columns=colunas)
    df_nova_linha = formatar_dados(df_nova_linha)
    return df_nova_linha, lista_nova_linha


def processar_nova_reserva(df_reservas, data, dict_dados, aba_reservas, maximo_reservas):
    df_nova_linha, linha_para_salvar = gerar_dataframe_reserva(dict_dados, df_reservas.columns)
    df_atualizado = pd.concat([df_reservas, df_nova_linha], ignore_index=True)

    df_filtrado = filtrar_dataframe_data(df_atualizado, data)
    validar_nova_reserva(df_filtrado, maximo_reservas)

    registrar_reserva(linha_para_salvar, aba_reservas)
    return df_atualizado

