import streamlit as st
import pandas as pd
from services.carregar_dados import carregar_dataframe

st.set_page_config(page_title="Gerenciamento de Reservas", layout="wide")

# Carregar dados
if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

df_reservas = st.session_state.df_reservas
df_reservas["Data"] = pd.to_datetime(df_reservas["Data"], errors="coerce").dt.date

# Cabeçalho com título e data no canto direito
col1, col2 = st.columns([7, 1])

with col1:
    st.title("📅 Gerenciamento de Reservas")
    # Coloca o seletor de data aqui, logo após o título
    data_selecionada = st.date_input("Selecione o dia para gerenciar as reservas", value=pd.to_datetime("today"))

with col2:
    st.markdown(f"""
    <p style='
        color: black;
        font-size: 1.3rem;
        font-weight: bold;
        text-align: right;
        margin-bottom: 0;
    '>{data_selecionada.strftime('%d/%m/%Y')}</p>
    """, unsafe_allow_html=True)

# Filtrar reservas
reservas_dia = df_reservas[df_reservas["Data"] == data_selecionada]

# Colunas para ambientes
col1, col2 = st.columns(2)

def exibir_resumo(reservas, ambiente):
    if reservas.empty:
        st.info(f"Nenhuma reserva no ambiente {ambiente.lower()} para esta data.")
        return

    horarios_unicos = sorted(reservas["Horário"].dropna().unique())

    for horario in horarios_unicos:
        bloco = reservas[reservas["Horário"] == horario]
        total_pessoas = bloco["Número de Pessoas"].astype(int).sum()
        qtd_reservas = len(bloco)

        with st.expander(f"🕒 {horario} – {qtd_reservas} reserva(s), {total_pessoas} pessoa(s)"):
            for _, row in bloco.iterrows():
                st.markdown(f"""
                <div style="border:1px solid #DDD; border-radius:10px; padding:10px; margin-bottom:6px; background-color:#f9f9f9;">
                    <strong>👤 {row['Nome']}</strong><br>
                    👥 {row['Número de Pessoas']} pessoas<br>
                    📞 {row['Telefone']}<br>
                    📝 {row['Observações'] or 'Sem observações'}
                </div>
                """, unsafe_allow_html=True)

with col1:
    st.subheader("🍽️ Ambiente Interno")
    internas = reservas_dia[reservas_dia["Área do Restaurante"] == "Interno"]
    exibir_resumo(internas, "Interno")

with col2:
    st.subheader("🌤️ Ambiente Externo")
    externas = reservas_dia[reservas_dia["Área do Restaurante"] == "Externo"]
    exibir_resumo(externas, "Externo")