import pandas as pd
def agrupar_por_dia(df):
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce").dt.date
    df_agrupado = df.groupby("Data", as_index=False)["Número de Pessoas"].sum()
    return df_agrupado