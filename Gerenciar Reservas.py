import streamlit as st
from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from services.carregar_dados import carregar_dataframe
from controller.reservas_controller import controlar_nova_reserva
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Sistema de Reservas Fuji", layout="wide")

# Título principal
st.markdown("## 🍣 Sistema de Reservas Fuji")
st.caption("Gerencie suas reservas de forma simples, rápida e segura.")
st.markdown("---")

# Inicializa planilha e dados
if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

aba = st.session_state.aba

# 🔘 Formulário com layout em colunas
with st.container():
    with st.expander("➕ Adicionar Nova Reserva", expanded=True):
        st.markdown("### 📝 Nova Reserva")

        with st.form("form_reserva"):
            # Obtem dados do form (assumindo que retorna um dicionário com os campos)
            dict_dados = obter_dados_reserva()

            # Botão mais estilizado
            enviado = st.form_submit_button("✅ Adicionar Reserva")

            if enviado:
                controlar_nova_reserva(
                    st.session_state.df_reservas,
                    dict_dados["Data"],
                    dict_dados,
                    aba
                )
                st.session_state.df_reservas = carregar_dataframe()
                st.toast("Reserva adicionada com sucesso! 🎉")
                st.rerun()  # Atualiza a página após adicionar

st.markdown("---")

# 🗂 Últimas Reservas com estilo de cartão
st.markdown("### 📋 Últimas Reservas")

with st.container():
    df = st.session_state.df_reservas.tail(10)

    st.dataframe(
        df.style.set_properties(**{
            "text-align": "left",
        }),
        use_container_width=True,
        height=400
    )