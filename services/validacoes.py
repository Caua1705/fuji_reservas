import streamlit as st
def validar_reserva(df_filtrado,maximo_reservas):
    st.write(df_filtrado)
    soma_reservas=df_filtrado["Número de Pessoas"].sum()
    if soma_reservas>maximo_reservas:
        raise ValueError("O número de reservas é maior que o permitido.")