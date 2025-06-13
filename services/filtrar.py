def filtrar_dataframe(df_reservas,data):
    return df_reservas.loc[df_reservas["Data"]==data]