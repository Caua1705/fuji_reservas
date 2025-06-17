import pandas as pd

def agrupar_por_dia(df):
    df["Número de Pessoas"] = pd.to_numeric(df["Número de Pessoas"])
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y", errors="coerce")  # força datetime
    df_agrupado = df.groupby("Data")["Número de Pessoas"].sum().reset_index()
    df_agrupado["Data"] = df_agrupado["Data"].dt.strftime("%d/%m/%Y")
    return df_agrupado