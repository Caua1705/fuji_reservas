def ler_todas_reservas(aba):
    return aba.get_all_values()


def registrar_reserva(aba,nova_linha):
    aba.append_row(nova_linha)


