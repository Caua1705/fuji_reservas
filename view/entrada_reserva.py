import streamlit as st
from datetime import datetime

def obter_dados_reserva():
    col1, col2 = st.columns(2)
    with col1:
        data = st.date_input("📅 Data da Reserva *", value=datetime.today(), format="DD/MM/YYYY")
        nome = st.text_input("👤 Nome do Cliente *")
        quantidade_pessoas = st.number_input("👥 Número de Pessoas *", min_value=1, value=1)
        filial=st.selectbox("🏢 Unidade",["Aldeota","Cambeba"])

    with col2:
        horario = st.selectbox("⏰ Horário da Reserva *", [
            "17:00","17:30", "18:00", "18:30", "19:00", "19:30", 
            "20:00", "20:30", "21:00", "21:30", "22:00"
        ])
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