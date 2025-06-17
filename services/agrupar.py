import streamlit as st

def agrupar_por_dia(df):
    return df.groupby("Data")["Número de Pessoas"].sum().reset_index()