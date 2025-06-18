import pandas as pd
import streamlit as st
def agrupar_por_dia(df):
    df_agrupado = df.groupby("Data")["Número de Pessoas"].sum().reset_index()
    st.write(df_agrupado)
    st.stop()
    # df_agrupado["Data"] = pd.to_datetime(df_agrupado["Data"], errors="coerce")
    # df_agrupado["Data"] = df_agrupado["Data"].dt.date
    return df_agrupado