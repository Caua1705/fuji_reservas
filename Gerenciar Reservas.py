import streamlit as st
from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from services.carregar_dados import carregar_dataframe
from controller.reservas_controller import controlar_nova_reserva

st.set_page_config(layout="wide")
st.title("Sistema de Gerenciamento de Reservas Fuji")
st.markdown("### Organize, registre e acompanhe suas reservas de forma prática e segura em tempo real.")

if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()

# Guarda o dataframe no estado para evitar recarregar sempre
if "df_reservas" not in st.session_state:
    df_reservas=carregar_dataframe()
    st.session_state.df_reservas = df_reservas

aba = st.session_state.aba

with st.form("form_reserva"):
    dict_dados = obter_dados_reserva()
    enviado = st.form_submit_button("Adicionar Reserva")
    if enviado:
        controlar_nova_reserva(st.session_state.df_reservas, dict_dados["Data"], dict_dados, aba)
        
        # Recarrega o dataframe atualizado após gravar na planilha
        df_reservas=carregar_dataframe()
        st.session_state.df_reservas = df_reservas
        
        st.success("Reserva adicionada com sucesso!")
