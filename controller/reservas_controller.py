from model.adicionar import registrar_reserva
from utils.formatadores import formatar_nova_linha,ORDEM_CAMPOS_RESERVA
from services.filtrar import filtrar_dataframe
from controller.validacoes import validar_reserva

#Recebebe os dados da view e executa o Model
def processar_nova_reserva(df_reservas,data,dict_dados,aba):
    nova_linha_=formatar_nova_linha(dict_dados,ORDEM_CAMPOS_RESERVA)
    df_filtrado=filtrar_dataframe(df_reservas,data)
    validar_reserva(df_filtrado,50)
    registrar_reserva(nova_linha_,aba)