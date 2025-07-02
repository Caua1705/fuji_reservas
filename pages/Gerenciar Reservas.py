import streamlit as st
from datetime import datetime
from src.services.inicializacao import inicializar_dados
from src.services.filtrar import filtrar_dataframe_data,filtrar_por_filial
# from src.services.reservas import exibir_resumo
from src.utils.estilo import linha_divisoria

st.set_page_config(page_title="Gerenciamento de Reservas", layout="wide")

# Inicializar dados
df_reservas = inicializar_dados(st.session_state["aba_reservas"])

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

# Filtros
col_filtros1, col_filtros2 = st.columns(2)
with col_filtros1:
    data_selecionada = st.date_input("📅 Selecione a data", datetime.today().date(), format="DD/MM/YYYY")
with col_filtros2:
    filial = st.selectbox("🏢 Filial", ["Aldeota", "Cambeba"])
linha_divisoria()

# Filtrar reservas por data
reservas_dia = filtrar_dataframe_data(df_reservas, data_selecionada)
#Filtrar por Filial
reservas_dia_filial=filtrar_por_filial(reservas_dia,filial)
# Colunas para ambientes
col1, col2 = st.columns(2)

# with col1:
#     st.markdown(f"### 🍽️ Ambiente Interno – {filial}")
#     df_ambiente_interno = reservas_dia_filial.loc[reservas_dia_filial["Área do Restaurante"] == "Interno"]
#     st.markdown(f"**Total de reservas:** {len(df_ambiente_interno)}")
#     exibir_resumo(df_ambiente_interno, "Interno")

# with col2:
#     st.markdown(f"### 🌤️ Ambiente Externo – {filial}")
#     df_ambiente_externo = reservas_dia_filial.loc[reservas_dia_filial["Área do Restaurante"] == "Externo"]
#     st.markdown(f"**Total de reservas:** {len(df_ambiente_externo)}")
#     exibir_resumo(df_ambiente_externo, "Externo")