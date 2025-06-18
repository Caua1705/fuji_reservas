def agrupar_por_dia(df):
    df_agrupado = df.groupby("Data")["Número de Pessoas"].sum().reset_index()
    df_agrupado["Data"]=df_agrupado["Data"].apply(lambda x:x.strftime("%d/%m/%Y"))
    return df_agrupado