import streamlit as st
from datetime import datetime
from src.config.settings import HORARIOS_RESERVAS

def obter_dados_reserva():
    col1, col2 = st.columns(2)
    with col1:
        data = st.date_input("📅 Data da Reserva *", value=datetime.today(), format="DD/MM/YYYY")
        nome = st.text_input("👤 Nome do Cliente *")
        quantidade_pessoas = st.number_input("👥 Número de Pessoas *", min_value=1, value=1)
        filial = st.selectbox("🏢 Unidade", ["Aldeota", "Cambeba"])

    with col2:
        horario = st.selectbox("⏰ Horário da Reserva *", HORARIOS_RESERVAS)
        telefone = st.text_input("📞 Telefone (somente números) *")
        area = st.selectbox("🍽️ Área do Restaurante *", ["Interno", "Externo"])
        email = st.text_input("✉️ E-mail para confirmação *")
    observacoes = st.text_input("📝 Observações")

    return {
        "Data": data,
        "Horário": horario,
        "Nome": nome,
        "Telefone": telefone,
        "Email":email,
        "Número de Pessoas": quantidade_pessoas,
        "Unidade":filial,
        "Área do Restaurante": area,
        "Observações": observacoes
    }