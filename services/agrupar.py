import pandas as pd
def agrupar_por_dia(df):
    df = df.copy()
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    if df["Data"].isnull().any():
        # aqui você pode ignorar linhas com data inválida, ou tratar de outro jeito
        df = df.dropna(subset=["Data"])
    df["Data"] = df["Data"].dt.date
    df_agrupado = df.groupby("Data", as_index=False)["Número de Pessoas"].sum()
    return df_agrupado