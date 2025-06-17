#Função apra adicionar dados na planilha
def registrar_reserva(nova_linha,aba):
    aba.append_row(nova_linha)

def registrar_reservas_por_dia(linhas,filial,aba2,aba3):
    if filial=="Aldeota":
        aba2.append_rows(linhas)
    elif filial=="Cambeba":
        aba3.append_rows(linhas)
