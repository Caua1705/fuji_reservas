def agrupar_por_dia(df):
    df_agrupado = df.groupby("Data")["Número de Pessoas"].sum().reset_index()
    df_agrupado["Data"] = df_agrupado["Data"].dt.date
    return df_agrupado