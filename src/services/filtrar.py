def filtrar_dataframe_data(df, data):
    return df.loc[df["Data"].dt.date == data]


def filtrar_por_filial(df, filial):
    return df.loc[df["Unidade"]==filial]


def filtrar_filial_e_data(df, filial, data):
    return df.loc[
        (df["Data"].dt.date==data) & 
        (df["Unidade"]==filial)
        ]