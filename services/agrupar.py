def agrupar_por_dia(df):
    df_agrupado = df.groupby("Data")["Número de Pessoas"].sum().reset_index()
    return df_agrupado