import streamlit as st
from services.reservas import processar_nova_reserva
from services.email import enviar_email_cliente

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

# def controlar_reservas_por_dia(df_reservas,filial,aba2,aba3):
#     processar_reservas_agrupadas(df_reservas,filial,aba2,aba3)
