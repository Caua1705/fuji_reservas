import pandas as pd
from data.conexao import conectar_planilha
from utils.formatadores import formatar_dados

def carregar_todas_as_reservas():
    aba,_,_ = conectar_planilha()
    linhas = aba.get_all_values()

    if not linhas or len(linhas) < 2:
        # Não há dados suficientes (só colunas ou nem isso)
        df = pd.DataFrame(columns=["Data", "Horário", "Nome", "Telefone", "Email", "Número de Pessoas", "Unidade", "Área do Restaurante", "Observações"])
        df = formatar_dados(df)
        
    # Usa a primeira linha como cabeçalho
    colunas = linhas[0]
    dados = linhas[1:]

    df = pd.DataFrame(dados, columns=colunas)
    df = formatar_dados(df)
    return df
    

