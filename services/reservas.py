import pandas as pd
from utils.formatadores import formatar_nova_linha, ORDEM_CAMPOS_RESERVA
from services.filtrar import filtrar_dataframe
from utils.formatadores import formatar_dados
from services.validacoes import validar_reserva
from model.adicionar import registrar_reserva

def processar_nova_reserva(df_reservas, data, dict_dados, aba, maximo_reservas=50):
    # Formata a nova linha com os dados fornecidos
    nova_linha = formatar_nova_linha(dict_dados, ORDEM_CAMPOS_RESERVA)
    df_nova_linha = pd.DataFrame([nova_linha], columns=df_reservas.columns)
    df_nova_linha = formatar_dados(df_nova_linha)

    # Cria o DataFrame atualizado simulando a adição
    df_atualizado = pd.concat([df_reservas, df_nova_linha], ignore_index=True)
    df_atualizado = formatar_dados(df_atualizado)

    # Filtra as reservas do mesmo dia para validação
    df_filtrado = filtrar_dataframe(df_atualizado, pd.to_datetime(data, format="%d/%m/%Y").date())
    
    # Valida se o total de reservas para o dia excede o máximo
    validar_reserva(df_filtrado, maximo_reservas)

    # Registra na planilha
    registrar_reserva(nova_linha, aba)
    
    return df_atualizado