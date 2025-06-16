import streamlit as st
import pandas as pd
from datetime import datetime
from services.carregar_dados import carregar_dataframe
from services.filtrar import filtrar_df_reservas
from services.reservas import exibir_resumo

st.set_page_config(page_title="Gerenciamento de Reservas", layout="wide")

# Carregar dados
if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

df_reservas = st.session_state.df_reservas
df_reservas["Data"] = pd.to_datetime(df_reservas["Data"], errors="coerce").dt.date

st.title("📅 Gerenciamento de Reservas")
col1,col2=st.columns(2)
with col1:
    data_selecionada = st.date_input("Selecione o dia para gerenciar as reservas", datetime.today().date(),format="DD/MM/YYYY")
with col2:
    filial=st.selectbox("🏢 Filial",["Aldeota","Cambeba"])

# Filtrar reservas
reservas_dia = filtrar_df_reservas(df_reservas,data_selecionada)

# Colunas para ambientes
col1, col2 = st.columns(2)
with col1:
    st.subheader("🍽️ Ambiente Interno")
    df_ambiente_interno = reservas_dia.loc[reservas_dia["Área do Restaurante"]=="Interno"]
    exibir_resumo(df_ambiente_interno, "Interno", filial)

with col2:
    st.subheader("🌤️ Ambiente Externo")
    df_ambiente_externo = reservas_dia.loc[reservas_dia["Área do Restaurante"]=="Externo"]
    exibir_resumo(df_ambiente_externo, "Externo", filial)