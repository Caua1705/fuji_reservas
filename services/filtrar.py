import pandas as pd

def filtrar_dataframe(df_reservas, data):
    return df_reservas.loc[df_reservas["Data"].dt.date == data]

def filtrar_df_reservas(df,data):
     return df.loc[df["Data"] == data]

def filtrar_por_filial(df,filial):
    df=df.copy()
    return df.loc[df["Unidade"]==filial]