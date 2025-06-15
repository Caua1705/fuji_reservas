from services.reservas import processar_nova_reserva

def controlar_nova_reserva(df_reservas, data, dict_dados, aba):
    processar_nova_reserva(df_reservas, data, dict_dados, aba)