import pandas as pd

def agrupar_por_dia(df):
    # Converte para datetime, força erros para NaT
    df = df.copy()
    if not pd.api.types.is_datetime64_any_dtype(df["Data"]):
        df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    
    # Opcional: checar e remover linhas com data inválida (NaT)
    if df["Data"].isnull().any():
        st.warning("Existem registros com data inválida que serão ignorados.")
        df = df[df["Data"].notnull()]
    
    df["Data"] = df["Data"].dt.date  # transforma datetime64 para date (só data)
    df_agrupado = df.groupby("Data", as_index=False)["Número de Pessoas"].sum()
    return df_agrupado
