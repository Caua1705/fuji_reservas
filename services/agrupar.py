from utils.dias_semana import DICIONARIO_DIAS

def agrupar_por_dia(df,):
    df_agrupado = df.groupby("Data")["Número de Pessoas"].sum().reset_index()
    df_agrupado["Dia da semana"] = df_agrupado["Data"].apply(lambda x: DICIONARIO_DIAS[x.weekday()]) 
    df_agrupado=[["Data","Dia da semana","Número de Pessoas"]]
    return df_agrupado 