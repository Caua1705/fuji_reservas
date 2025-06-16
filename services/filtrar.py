import pandas as pd

def filtrar_dataframe(df_reservas, data):
    if isinstance(data, str):
        data = pd.to_datetime(data, format="%d/%m/%Y", errors="coerce").date()
    return df_reservas.loc[df_reservas["Data"].dt.date  == data]

def filtrar_df_reservas(df,data):
     return df.loc[df["Data"] == data]