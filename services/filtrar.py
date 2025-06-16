import pandas as pd
def formatar_dados(df):
    df = df.copy()
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y", errors="coerce")  # manter datetime64
    df["Número de Pessoas"] = pd.to_numeric(df["Número de Pessoas"], errors="coerce").fillna(0).astype(int)
    return df