import streamlit as st
from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from services.carregar_dados import carregar_dataframe
from controller.reservas_controller import controlar_nova_reserva
from utils.estilo import linha_divisoria

# Config da página
st.set_page_config(page_title="Sistema de Reservas Fuji", layout="wide")

# Título
st.title("🍣 Sistema de Reservas Fuji")
linha_divisoria()

# Inicia planilha e dados
if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

aba = st.session_state.aba

# 📝 Formulário de nova reserva 
st.subheader("📝 Nova Reserva")

with st.form("form_reserva", border=True):
    dict_dados = obter_dados_reserva()

    enviado = st.form_submit_button("✅ Adicionar Reserva")

    if enviado:
        if dict_dados is None:
            st.warning("⚠️ Preencha todos os campos obrigatórios marcados com *.")
        else:
            controlar_nova_reserva(
                st.session_state.df_reservas,
                dict_dados["Data"],
                dict_dados,
                aba
            )
            st.session_state.df_reservas = carregar_dataframe()
            st.success("✅ Reserva adicionada com sucesso!")

