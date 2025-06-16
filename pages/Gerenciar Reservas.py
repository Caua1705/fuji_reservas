import streamlit as st
import pandas as pd
from services.carregar_dados import carregar_dataframe

st.set_page_config(page_title="Gerenciamento de Reservas", layout="wide")

# Carregar os dados
if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

df_reservas = st.session_state.df_reservas
df_reservas["Data"] = pd.to_datetime(df_reservas["Data"], errors="coerce").dt.date

# =======================
# 🔝 TOPO DA PÁGINA
# =======================
st.markdown("""
    <div style="padding: 1rem 0;">
        <h1 style="margin-bottom: 0;">📅 Gerenciamento de Reservas</h1>
        <p style="color: gray; font-size: 1rem;">Visualize rapidamente todas as reservas do restaurante organizadas por ambiente e horário.</p>
    </div>
""", unsafe_allow_html=True)

# 📆 Seletor de Data
data_selecionada = st.date_input("Selecione o dia para gerenciar as reservas", value=pd.to_datetime("today"))

# 🔍 Filtro
reservas_dia = df_reservas[df_reservas["Data"] == data_selecionada]