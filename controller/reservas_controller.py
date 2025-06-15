import streamlit as st
from services.reservas import processar_nova_reserva

def controlar_nova_reserva(df_reservas, data, dict_dados, aba):
    try:
        processar_nova_reserva(df_reservas, data, dict_dados, aba)
    except ValueError as e:
        st.error(str(e))  # Exibe a mensagem da exceção (ex: excesso de reservas)
        st.stop()