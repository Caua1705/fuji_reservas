import streamlit as st
import pandas as pd
from services.carregar_dados import carregar_dataframe

# Carregar e preparar dados
if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

df_reservas = st.session_state.df_reservas
df_reservas["Data"] = pd.to_datetime(df_reservas["Data"], errors="coerce").dt.date

# 📅 Seleção de data
data_selecionada = st.date_input("Selecione o dia para gerenciar as reservas")

# 🔎 Filtrar reservas do dia
reservas_dia = df_reservas[df_reservas["Data"] == data_selecionada]

st.markdown(f"### 📋 Reservas para {data_selecionada.strftime('%d/%m/%Y')}")

# ➗ Separar por ambiente
col1, col2 = st.columns(2)

def exibir_cartoes(reservas, ambiente):
    if reservas.empty:
        st.info(f"Nenhuma reserva no ambiente {ambiente.lower()} para esta data.")
    for _, row in reservas.iterrows():
        st.markdown(f"""
        <div style="border:1px solid #DDD; border-radius:12px; padding:16px; margin-bottom:10px; background-color:#f9f9f9;">
            <h4 style="margin:0;">🕒 {row['Horário']}</h4>
            <p style="margin:4px 0;"><strong>👤 {row['Nome']}</strong></p>
            <p style="margin:4px 0;">👥 {row['Número de Pessoas']} pessoas</p>
            {"<p style='margin:4px 0;'>📞 " + row['Telefone'] + "</p>" if pd.notna(row['Telefone']) else ""}
            {"<p style='margin:4px 0;'>📝 <em>" + row['Observações'] + "</em></p>" if pd.notna(row['Observações']) and row['Observações'].strip() else ""}
        </div>
        """, unsafe_allow_html=True)

with col1:
    st.subheader("🍽️ Ambiente Interno")
    internas = reservas_dia[reservas_dia["Área do Restaurante"] == "Interno"]
    exibir_cartoes(internas, "Interno")

with col2:
    st.subheader("🌤️ Ambiente Externo")
    externas = reservas_dia[reservas_dia["Área do Restaurante"] == "Externo"]
    exibir_cartoes(externas, "Externo")