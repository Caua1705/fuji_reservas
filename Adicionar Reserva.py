import streamlit as st
from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from services.carregar_dados import carregar_todas_as_reservas
from controller.reservas_controller import controlar_nova_reserva,controlar_reservas_por_dia

# Config da página
st.set_page_config(page_title="Sistema de Reservas Fuji", layout="wide")

# Título
st.title("📝 Nova Reserva")

# Inicia planilha e dados
if "aba" not in st.session_state or "aba2" not in st.session_state or "aba3" not in st.session_state:
    st.session_state.aba,st.session_state.aba2,st.session_state.aba3 = conectar_planilha()

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_todas_as_reservas()

aba = st.session_state.aba
aba2 = st.session_state.aba2
aba3 = st.session_state.aba3

# 📝 Formulário de nova reserva 

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
            st.session_state.df_reservas = carregar_todas_as_reservas()
            controlar_reservas_por_dia(st.session_state.df_reservas,dict_dados["Unidade"])
            st.success("✅ Reserva adicionada com sucesso!")

