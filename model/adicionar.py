from utils.formatadores import formatar_nova_linha

#Função apra adicionar dados na planilha
def adicionar_reserva(nova_linha,aba):
    nova_linha_formatada=formatar_nova_linha(nova_linha)
    aba.append_row(nova_linha_formatada)