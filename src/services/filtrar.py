#Tem duas funções iguais no mesmo código! e será que eu preciso copiar tambem na hora de filtrar por data,
#que nem eu fiz em filtrar por filial
def filtrar_dataframe(df_reservas, data):
    return df_reservas.loc[df_reservas["Data"].dt.date == data]

def filtrar_df_reservas(df,data):
     return df.loc[df["Data"].dt.date == data]

def filtrar_por_filial(df,filial):
    df=df.copy()
    return df.loc[df["Unidade"]==filial]

def filtrar_filial_e_data(df,filial,data):
    df=df.copy()
    df_filtrado = df.loc[(df["Data"].dt.date==data) & 
                        (df["Unidade"]==filial)]
    return df_filtrado