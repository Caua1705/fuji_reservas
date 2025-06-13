ORDEM_CAMPOS_RESERVA = ["Data", "Horário", "Nome", "Telefone", "Número de Pessoas", "Área", "Observações"]

def formatar_nova_linha(dict_dados,ordem_campos):
     return [str(dict_dados[campo]) for campo in ordem_campos]