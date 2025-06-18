import pandas as pd

ORDEM_CAMPOS_RESERVA = ["Data", "Horário", "Nome", "Telefone", "Email", "Número de Pessoas", "Unidade", "Área do Restaurante", "Observações"]

def formatar_nova_linha(dict_dados,ordem_campos):
     return [str(dict_dados[campo]) for campo in ordem_campos]

def formatar_dados(df):
     df["Data"]=pd.to_datetime(df["Data"],format="%d/%m/%Y",errors="coerce")
     df["Número de Pessoas"]=pd.to_numeric(df["Número de Pessoas"],errors="coerce").fillna(0).astype(int)
     return df

def formatar_linhas_agrupadas(df_agrupado):
     return [[str(item)for item in linha]for linha in df_agrupado.values.tolist()]

def formatar_data(df,coluna_data):
     df[coluna_data] = pd.to_datetime(df[coluna_data], errors="coerce").dt.date
     df[coluna_data]=df[coluna_data].apply(lambda x:x.strftime())
     return df