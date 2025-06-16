import streamlit as st
from services.carregar_dados import carregar_dataframe
from utils.formatadores import formatar_dados

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

df_reservas=st.session_state.df_reservas

df=formatar_dados(df_reservas)




st.write(df_reservas)