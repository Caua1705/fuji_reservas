import streamlit as st
from datetime import datetime
from services.inicializacao import inicializar_dados
from services.filtrar import filtrar_df_reservas,filtrar_por_filial
from services.reservas import exibir_resumo
from utils.estilo import linha_divisoria

st.set_page_config(page_title="Gerenciamento de Reservas", layout="wide")

# Inicializar dados
df_reservas = inicializar_dados()

# TOPO com título + botão
col1, col2 = st.columns([5, 1])
with col1:
    st.markdown("## 🛎️ Gestão de Reservas")
with col2:
    st.markdown(
        """
        <a href='https://docs.google.com/spreadsheets/d/11Xr7aQMRXVMHnfelO0D-ekvOQy-DoJgf3Q7nTBYVf_s/edit?usp=sharing' target='_blank'>
            <button style='background-color:#28a745;color:white;padding:0.5em 1em;
                           border:none;border-radius:6px;cursor:pointer;width:100%'>
                📂 Abrir Planilha
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

# Sidebar - filtros
col_filtros1, col_filtros2 = st.columns(2)
with col_filtros1:
    data_selecionada = st.date_input("📅 Selecione a data", datetime.today().date(), format="DD/MM/YYYY")
with col_filtros2:
    filial = st.selectbox("🏢 Filial", ["Aldeota", "Cambeba"])
# Mostrar data selecionada
# st.markdown(f"**📅 Data selecionada:** {data_selecionada.strftime('%d/%m/%Y')}")

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