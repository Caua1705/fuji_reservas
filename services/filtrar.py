import pandas as pd

def filtrar_dataframe(df_reservas, data):
    return df_reservas.loc[df_reservas["Data"].dt.date == data]

def filtrar_df_reservas(df,data):
     return df.loc[df["Data"] == data]

def filtrar_por_filial(df, filial):
    if df is None or not hasattr(df, 'copy'):
        # Evita erros se df não for DataFrame
        return pd.DataFrame(columns=df.columns if hasattr(df, 'columns') else [])
    df = df.copy()
    return df.loc[df["Unidade"] == filial]