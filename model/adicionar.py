#Função apra adicionar dados na planilha
def registrar_reserva(nova_linha,aba):
    aba.append_row(nova_linha)

def registrar_reservas_por_dia(linhas, filial, aba2, aba3):
    abas={"Aldeota":aba2,"Cambeba":aba3}
    aba=abas[filial]
    cabecalho = aba.get_all_values()[0]  # pega primeira linha (cabeçalho)
    aba.clear()
    aba.append_row(cabecalho)
    aba.append_rows(linhas[1:])
    