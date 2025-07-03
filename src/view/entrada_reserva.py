import streamlit as st
from datetime import datetime
from src.config.settings import HORARIOS_RESERVAS

def obter_dados_reserva():
    st.markdown("## Nova Reserva")

    st.markdown("#### Informações do Cliente")
    col1, col2 = st.columns(2)

    with col1:
        nome = st.text_input("Nome completo *")
        telefone = st.text_input("Telefone (somente números) *")
        email = st.text_input("E-mail para confirmação *")

    with col2:
        quantidade_pessoas = st.number_input("Número de pessoas *", min_value=1, value=1)
        filial = st.selectbox("Unidade", ["Aldeota", "Cambeba"])
        area = st.selectbox("Área do restaurante *", ["Interno", "Externo"])

    st.markdown("#### Agendamento da Mesa")
    col3, col4 = st.columns(2)
    with col3:
        data = st.date_input("Data *", value=datetime.today(), format="DD/MM/YYYY")
    with col4:
        horario = st.selectbox("Horário *", HORARIOS_RESERVAS)

    st.markdown("#### Observações (opcional)")
    observacoes = st.text_area("", placeholder="Deseja informar alguma preferência ou pedido especial?")

    return {
        "Data": data,
        "Horário": horario,
        "Nome": nome,
        "Telefone": telefone,
        "Email": email,
        "Número de Pessoas": quantidade_pessoas,
        "Unidade": filial,
        "Área do Restaurante": area,
        "Observações": observacoes
    }