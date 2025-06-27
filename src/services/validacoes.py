from src.config.settings import MSG_ERRO_EXCESSO_RESERVAS

def validar_reserva(df_filtrado,maximo_reservas):
    soma_reservas=df_filtrado["Número de Pessoas"].sum()
    if soma_reservas>maximo_reservas:
        raise ValueError(MSG_ERRO_EXCESSO_RESERVAS)