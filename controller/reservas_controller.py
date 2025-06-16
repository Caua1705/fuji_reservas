import streamlit as st
from services.reservas import processar_nova_reserva

def controlar_nova_reserva(df_reservas, data, dict_dados, aba):
    try:
        df_atualizado = processar_nova_reserva(df_reservas, data, dict_dados, aba)
        st.session_state.df_reservas = df_atualizado 
    except ValueError as e:
        st.error(e)  # Exibe a mensagem da exceção (ex: excesso de reservas)
        st.stop()