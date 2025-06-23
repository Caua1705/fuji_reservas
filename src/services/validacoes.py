def validar_reserva(df_filtrado,maximo_reservas):
    soma_reservas=df_filtrado["Número de Pessoas"].sum()
    if soma_reservas>maximo_reservas:
        raise ValueError("O número de reservas é maior que o permitido.")