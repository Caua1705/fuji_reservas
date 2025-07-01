from src.config.settings import MSG_ERRO_EXCESSO_RESERVAS, MSG_ERRO_CAMPOS_OBRIGATORIOS, CAMPOS_OBRIGATORIOS_FORMULARIO

def validar_nova_reserva(df_filtrado,maximo_reservas):
    soma_reservas=df_filtrado["Número de Pessoas"].sum()
    if soma_reservas>maximo_reservas:
        raise ValueError(MSG_ERRO_EXCESSO_RESERVAS)
    

def validar_campos_nova_reserva(dict_dados):
    if not all([dict_dados.get(campo) for campo in CAMPOS_OBRIGATORIOS_FORMULARIO]):
        raise ValueError(MSG_ERRO_CAMPOS_OBRIGATORIOS)