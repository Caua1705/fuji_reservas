import streamlit as st
import pandas as pd
from datetime import datetime
from services.carregar_dados import carregar_todas_as_reservas
from services.filtrar import filtrar_df_reservas,filtrar_por_filial
from services.reservas import exibir_resumo
from utils.estilo import linha_divisoria

st.set_page_config(page_title="Gerenciamento de Reservas", layout="wide")

# Carregar dados
if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_todas_as_reservas()

df_reservas = st.session_state.df_reservas

# Título e botão de nova reserva
st.markdown("## 🛎️ Gestão de Reservas")
linha_divisoria()

# Sidebar - filtros
with st.sidebar:
    data_selecionada = st.date_input("📅 Selecione a data", datetime.today().date(), format="DD/MM/YYYY")
    filial = st.selectbox("🏢 Filial", ["Aldeota", "Cambeba"])

# Mostrar data selecionada
st.markdown(f"**📅 Data selecionada:** {data_selecionada.strftime('%d/%m/%Y')}")

# Filtrar reservas por data
reservas_dia = filtrar_df_reservas(df_reservas, data_selecionada)
#Filtrar por Filial
reservas_dia_filial=filtrar_por_filial(reservas_dia,filial)
# Colunas para ambientes
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### 🍽️ Ambiente Interno – {filial}")
    df_ambiente_interno = reservas_dia_filial.loc[reservas_dia_filial["Área do Restaurante"] == "Interno"]
    st.markdown(f"**Total de reservas:** {len(df_ambiente_interno)}")
    exibir_resumo(df_ambiente_interno, "Interno")

with col2:
    st.markdown(f"### 🌤️ Ambiente Externo – {filial}")
    df_ambiente_externo = reservas_dia_filial.loc[reservas_dia_filial["Área do Restaurante"] == "Externo"]
    st.markdown(f"**Total de reservas:** {len(df_ambiente_externo)}")
    exibir_resumo(df_ambiente_externo, "Externo")