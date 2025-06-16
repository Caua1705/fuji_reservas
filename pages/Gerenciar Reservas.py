import streamlit as st
import pandas as pd
from services.carregar_dados import carregar_dataframe

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

df=st.session_state.df_reservas

data_selecionada = st.date_input("Selecione o dia para gerenciar as reservas")

# 🔍 Filtrar as reservas daquele dia
reservas_dia = df[df['Data'] == pd.to_datetime(data_selecionada).strftime('%Y-%m-%d')]

st.markdown(f"### Reservas para {data_selecionada.strftime('%d/%m/%Y')}")

# ➗ Separar por ambiente
col1, col2 = st.columns(2)

with col1:
    st.subheader("Ambiente Interno")
    internas = reservas_dia[reservas_dia["Área do Restaurante"] == "Interno"]
    for _, row in internas.iterrows():
        st.markdown(f"""
        #### 🕒 {row['Horário']}
        - 👤 {row['Nome']}
        - 👥 {row['Número de Pessoas']} pessoas
        - 📞 {row['Telefone']}
        - 📝 {row['Observações'] or 'Sem observações'}
        """, unsafe_allow_html=True)

with col2:
    st.subheader("Ambiente Externo")
    externas = reservas_dia[reservas_dia["Área do Restaurante"] == "Externo"]
    for _, row in externas.iterrows():
        st.markdown(f"""
        #### 🕒 {row['Horário']}
        - 👤 {row['Nome']}
        - 👥 {row['Número de Pessoas']} pessoas
        - 📞 {row['Telefone']}
        - 📝 {row['Observações'] or 'Sem observações'}
        """, unsafe_allow_html=True)
