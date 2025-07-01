import pandas as pd

def formatar_dados(df):
     df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y", errors="coerce")
     df["Número de Pessoas"] = pd.to_numeric(df["Número de Pessoas"],errors="coerce").fillna(0).astype(int)
     return df

def formatar_linhas_agrupadas(df_agrupado):
     return df_agrupado.applymap(str).values.tolist()

def formatar_data_para_string(data):
    return data.strftime("%d/%m/%Y")


def formatar_coluna_data_para_string(df,coluna_data):
     df[coluna_data] = df[coluna_data].apply(formatar_data_para_string)
     return df


