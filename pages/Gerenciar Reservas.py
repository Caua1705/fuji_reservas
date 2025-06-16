import streamlit as st
from services.carregar_dados import carregar_dataframe
import pandas as pd

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

df_reservas=st.session_state.df_reservas

df_reservas["Data"]=pd.to_datetime(df_reservas["Data"],errors="coerce")


st.write(df_reservas)