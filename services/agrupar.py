import streamlit as st

def agrupar_por_dia(df):
    df_agrupado=df.groupby("Data")["Número de Pessoas"].sum()
    return df_agrupado