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
st.caption("Gerencie suas reservas de forma simples, rápida e segura.")
linha_divisoria()

# Inicia planilha e dados
if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

aba = st.session_state.aba

# 📝 Formulário de nova reserva (sem expander)
st.markdown("## ➕ Nova Reserva")

with st.form("form_reserva", border=True):
    # Se seu `obter_dados_reserva()` retorna os campos com st.input, ele será exibido aqui
    dict_dados = obter_dados_reserva()

    enviado = st.form_submit_button("✅ Adicionar Reserva")

    if enviado:
        controlar_nova_reserva(
            st.session_state.df_reservas,
            dict_dados["Data"],
            dict_dados,
            aba
        )
        st.session_state.df_reservas = carregar_dataframe()

st.divider()

# 📋 Últimas reservas
st.markdown("## 📋 Próximas Reservas")

df = st.session_state.df_reservas.copy()

# Ordenar por Data e Horário (do mais recente pro mais antigo)
df = df.sort_values(by=["Data", "Horário"], ascending=True)

# Mostrar as 5 últimas reservas (mais novas no topo)
st.write(df.head(5))