def ler_todas_reservas(aba):
    return aba.get_all_values()


def registrar_reserva(nova_linha,aba):
    aba.append_row(nova_linha)


def registrar_reservas_por_dia(linhas, filial, abas):
    aba_selecionada = abas[filial]
    aba_selecionada.batch_clear(['A2:C'])
    aba_selecionada.update('A2', linhas)
