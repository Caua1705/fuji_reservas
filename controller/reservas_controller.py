import streamlit as st
from services.reservas import processar_nova_reserva,processar_reservas_agrupadas
from services.email import enviar_email_cliente
from services.agrupar import agrupar_por_dia
import pandas as pd

def controlar_nova_reserva(df_reservas, data, dict_dados, aba):
    try:
        email_origem=st.secrets["email"]["origem"]
        senha_app=st.secrets["email"]["senha_app"]
        df_atualizado = processar_nova_reserva(df_reservas, data, dict_dados, aba)
        enviar_email_cliente(email_origem, dict_dados["Email"], senha_app, dict_dados["Nome"], data, dict_dados["Horário"], dict_dados["Unidade"])
        st.session_state.df_reservas = df_atualizado 
    except ValueError as e:
        st.error(e)  # Exibe a mensagem da exceção (ex: excesso de reservas)
        st.stop() 

def controlar_reservas_por_dia(df_reservas, filial, aba2, aba3):
    if df_reservas is None:
        st.error("df_reservas está vazio (None).")
        return
    if not isinstance(df_reservas, pd.DataFrame):
        st.error(f"df_reservas tem tipo inválido: {type(df_reservas)}")
        return
    if df_reservas.empty:
        st.warning("df_reservas está vazio.")
        return
    processar_reservas_agrupadas(df_reservas, filial, aba2, aba3)