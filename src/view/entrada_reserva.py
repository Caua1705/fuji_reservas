import streamlit as st
from datetime import datetime
from src.config.settings import HORARIOS_RESERVAS

def obter_dados_reserva():
    st.markdown("## Nova Reserva")

    with st.container():
        st.markdown("#### Dados do Cliente e Reserva")
        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input("Nome completo *")
            telefone = st.text_input("Telefone (somente números) *")
            email = st.text_input("E-mail para confirmação *")
            quantidade_pessoas = st.number_input("Número de pessoas *", min_value=1, value=1)

        with col2:
            data = st.date_input("Data da reserva *", value=datetime.today(), format="DD/MM/YYYY")
            horario = st.selectbox("Horário da reserva *", HORARIOS_RESERVAS)
            filial = st.selectbox("Unidade", ["Aldeota", "Cambeba"])
            area = st.selectbox("Área do restaurante *", ["Interno", "Externo"])

    st.markdown("#### Observações (opcional)")
    observacoes = st.text_area("", placeholder="Alguma solicitação especial para a reserva?")

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
