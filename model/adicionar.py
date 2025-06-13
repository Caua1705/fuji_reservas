from utils.formatadores import formatar_nova_linha

#Função apra adicionar dados na planilha
def registrar_reserva(nova_linha,aba):
    aba.append_row(nova_linha)