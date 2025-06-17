#Função apra adicionar dados na planilha
def registrar_reserva(nova_linha,aba):
    aba.append_row(nova_linha)

def registrar_reservas_por_dia(linhas, filial, aba2, aba3):
    if filial == "Aldeota":
        cabecalho = aba2.get_all_values()[0]  # pega primeira linha (cabeçalho)
        aba2.clear()
        aba2.append_row(cabecalho)
        aba2.append_rows(linhas)
    elif filial == "Cambeba":
        cabecalho = aba3.get_all_values()[0]
        aba3.clear()
        aba3.append_row(cabecalho)
        aba3.append_rows(linhas)