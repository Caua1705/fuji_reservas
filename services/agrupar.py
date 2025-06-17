import pandas as pd

def agrupar_por_dia(df):
    df["Número de Pessoas"]=pd.to_numeric(df["Número de Pessoas"])
    return df.groupby("Data")["Número de Pessoas"].sum().reset_index()