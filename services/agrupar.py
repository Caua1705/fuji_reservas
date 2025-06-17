import pandas as pd

def agrupar_por_dia(df):
    print("Tipos no df antes de conversão:")
    print(df.dtypes)
    
    df = df.copy()
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y", errors="coerce")
    print("Tipos no df depois de converter Data:")
    print(df.dtypes)
    
    if df["Data"].isna().any():
        raise ValueError("Tem valores NaT na coluna Data, verificar dados de entrada!")
    
    df["Número de Pessoas"] = pd.to_numeric(df["Número de Pessoas"], errors='coerce').fillna(0).astype(int)
    df_agrupado = df.groupby("Data")["Número de Pessoas"].sum().reset_index()
    return df_agrupado