def registrar_reservas_por_dia(aba,linhas):
    aba.batch_clear(['A2:C'])
    aba.update('A2', linhas)
