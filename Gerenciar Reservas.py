import streamlit as st
from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from services.carregar_dados import carregar_dataframe
from controller.reservas_controller import controlar_nova_reserva
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Sistema de Reservas Fuji", layout="wide")

# Título principal
st.title("🍣 Sistema de Reservas Fuji")
st.caption("Gerencie suas reservas de forma simples, rápida e segura.")

st.divider()

# Inicializa planilha e dados
if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

aba = st.session_state.aba

# Seção de formulário
with st.expander("➕ Adicionar Nova Reserva", expanded=True):
    st.subheader("Preencha os dados abaixo:")
    with st.form("form_reserva"):
        dict_dados = obter_dados_reserva()
        enviado = st.form_submit_button("Adicionar Reserva")

        if enviado:
            controlar_nova_reserva(
                st.session_state.df_reservas,
                dict_dados["Data"],
                dict_dados,
                aba
            )
            st.session_state.df_reservas = carregar_dataframe()
            st.success("✅ Reserva adicionada com sucesso!")
            st.balloons()

st.divider()

# Mostrar últimas reservas (opcional)
st.subheader("📋 Últimas reservas adicionadas")
st.dataframe(st.session_state.df_reservas.tail(10), use_container_width=True)