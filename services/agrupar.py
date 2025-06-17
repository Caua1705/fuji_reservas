import pandas as pd

def agrupar_por_dia(df):
    df["Número de Pessoas"] = pd.to_numeric(df["Número de Pessoas"])
    df_agrupado = df.groupby("Data")["Número de Pessoas"].sum().reset_index()
    df_agrupado["Data"] = df_agrupado["Data"].dt.strftime("%d/%m/%Y")
    return df_agrupado