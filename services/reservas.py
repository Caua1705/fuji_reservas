import pandas as pd
from utils.formatadores import formatar_nova_linha, ORDEM_CAMPOS_RESERVA
from services.filtrar import filtrar_dataframe
from services.validacoes import validar_reserva
from model.adicionar import registrar_reserva

def processar_nova_reserva(df_reservas, data, dict_dados, aba, maximo_reservas=50):
    nova_linha = formatar_nova_linha(dict_dados, ORDEM_CAMPOS_RESERVA)  # dados do usuário
    
    # Cria um DataFrame com a nova linha, associando as colunas certas
    df_nova_linha = pd.DataFrame([nova_linha], columns=df_reservas.columns)
    
    # Concatena ao DataFrame existente (verticalmente)
    df_atualizado = pd.concat([df_reservas, df_nova_linha], ignore_index=True)
    
    # Filtra o DataFrame atualizado
    df_filtrado = filtrar_dataframe(df_atualizado, data)
    
    # Valida as reservas no DataFrame atualizado
    validar_reserva(df_filtrado, maximo_reservas)
    
    # Registra na planilha o dado do usuário
    registrar_reserva(nova_linha, aba)