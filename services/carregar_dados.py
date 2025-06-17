import pandas as pd
from data.conexao import conectar_planilha

def carregar_todas_as_reservas():
    aba,_ = conectar_planilha()
    linhas = aba.get_all_values()

    if not linhas or len(linhas) < 2:
        # Não há dados suficientes (só colunas ou nem isso)
        return pd.DataFrame(columns=["Data", "Horário", "Nome", "Telefone", "Email", "Número de Pessoas", "Unidade", "Área do Restaurante", "Observações"])

    # Usa a primeira linha como cabeçalho
    colunas = linhas[0]
    dados = linhas[1:]

    return pd.DataFrame(dados, columns=colunas)
    

