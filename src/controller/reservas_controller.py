import streamlit as st
from src.services.reservas import processar_nova_reserva,processar_reservas_agrupadas
from src.services.email_cliente import enviar_email_cliente

def controlar_nova_reserva(df_reservas, data, dict_dados, aba):
    
    email_origem=st.secrets["email"]["origem"]
    senha_app=st.secrets["email"]["senha_app"]
    df_atualizado = processar_nova_reserva(df_reservas, data, dict_dados, aba)
    enviar_email_cliente(email_origem,
                            dict_dados["Email"],
                            senha_app,
                            dict_dados["Nome"],
                            data,
                            dict_dados["Horário"],
                            dict_dados["Unidade"])
    return df_atualizado 

def controlar_reservas_por_dia(df_reservas,filial,aba2,aba3):
    processar_reservas_agrupadas(df_reservas,filial,aba2,aba3)
