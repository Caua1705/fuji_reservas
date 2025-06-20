import streamlit as st
from datetime import datetime
from services.inicializacao import inicializar_dados
from services.filtrar import filtrar_df_reservas, filtrar_por_filial
from services.reservas import exibir_resumo

st.set_page_config(page_title="🍣 Fuji Lounge – Reservas", layout="wide")

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

st.markdown("---")

# FILTROS
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        data_selecionada = st.date_input("📅 Data", datetime.today().date(), format="DD/MM/YYYY")
    with col2:
        filial = st.selectbox("🏢 Filial", ["Aldeota", "Cambeba"])

# Mostrar data
st.markdown(f"**📅 Reservas para:** `{data_selecionada.strftime('%d/%m/%Y')}`")
st.markdown("---")

# Filtrar dados
reservas_dia = filtrar_df_reservas(df_reservas, data_selecionada)
reservas_dia_filial = filtrar_por_filial(reservas_dia, filial)

# AMBIENTES
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"### 🍽️ Ambiente Interno – {filial}")
    df_interno = reservas_dia_filial.loc[reservas_dia_filial["Área do Restaurante"] == "Interno"]
    st.markdown(f"**Total de reservas:** {len(df_interno)}")
    if df_interno.empty:
        st.markdown(
            "<div style='background:#f8f9fa;padding:1rem;border-radius:8px;border:1px solid #dee2e6'>"
            "Nenhuma reserva no ambiente <strong>Interno</strong> para esta data."
            "</div>", unsafe_allow_html=True
        )
    else:
        exibir_resumo(df_interno, "Interno")

with col2:
    st.markdown(f"### 🌤️ Ambiente Externo – {filial}")
    df_externo = reservas_dia_filial.loc[reservas_dia_filial["Área do Restaurante"] == "Externo"]
    st.markdown(f"**Total de reservas:** {len(df_externo)}")
    if df_externo.empty:
        st.markdown(
            "<div style='background:#f8f9fa;padding:1rem;border-radius:8px;border:1px solid #dee2e6'>"
            "Nenhuma reserva no ambiente <strong>Externo</strong> para esta data."
            "</div>", unsafe_allow_html=True
        )
    else:
        exibir_resumo(df_externo, "Externo")