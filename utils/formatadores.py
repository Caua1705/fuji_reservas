import pandas as pd

ORDEM_CAMPOS_RESERVA = ["Data", "Horário", "Nome", "Telefone", "Número de Pessoas", "Filial", "Área", "Observações"]

def formatar_nova_linha(dict_dados,ordem_campos):
     return [str(dict_dados[campo]) for campo in ordem_campos]

def formatar_dados(df):
     df=df.copy()
     df["Data"]=pd.to_datetime(df["Data"],format="%d/%m/%Y",errors="coerce")
     df["Número de Pessoas"]=pd.to_numeric(df["Número de Pessoas"],errors="coerce").fillna(0).astype(int)
     return df
