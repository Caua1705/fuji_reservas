from model.adicionar import adicionar_reserva
from utils.formatadores import formatar_nova_linha


#Recebebe os dados da view e executa o Model
def atualizar_dataframe(nova_linha,aba):
    nova_linha=formatar_nova_linha(nova_linha)
    adicionar_reserva(nova_linha,aba)