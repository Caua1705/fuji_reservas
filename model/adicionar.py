#Função apra adicionar dados na planilha
def registrar_reserva(nova_linha,aba):
    aba.append_row(nova_linha)

def registrar_reservas_por_dia(linhas, filial, aba2, aba3):
    abas={"Aldeota":aba2,"Cambeba":aba3}
    aba=abas[filial]
    # Limpa só as colunas A:C a partir da linha 2
    aba.batch_clear(['A2:C'])
    # Atualiza dados a partir da célula A2, de acordo com a qunatidade de colunas continda em linhas
    aba.update('A2', linhas)
    