import streamlit as st
from services.carregar_dados import carregar_dataframe

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

df_reservas=st.session_state.df_reservas


st.write(df_reservas)