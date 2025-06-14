import streamlit as st
from datetime import datetime
#Recebe dados da reserva
def obter_dados_reserva():
    col1,col2=st.columns(2)
    with col1:
        data=st.date_input("Data da Reserva",value=datetime.today(),format="DD/MM/YYYY")
        nome=st.text_input("Nome do Cliente")
        quantidade_pessoas=st.number_input("Número de Pessoas",min_value=0)
    with col2:
        horario=st.time_input("Horário da Reserva")
        telefone=st.text_input("Telefone (somente números)")
        area = st.radio("Área do Restaurante", ["Interno", "Externo"],horizontal=True)
    observacoes=st.text_input("Observações")
    return {
        "Data": data,
        "Horário": horario,
        "Nome": nome,
        "Telefone": telefone,
        "Número de Pessoas": quantidade_pessoas,
        "Área": area,
        "Observações": observacoes
    }