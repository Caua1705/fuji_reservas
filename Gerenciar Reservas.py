import streamlit as st
from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from controller.reservas_controller import processar_nova_reserva
from services.carregar_dados import carregar_dataframe

st.set_page_config(layout="wide")


# Título e Subtítulo
st.title("Sistema de Gerenciamento de Reservas Fuji")
st.markdown("### Organize, registre e acompanhe suas reservas de forma prática e segura em tempo real.")


#Cria conexão
if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()
aba = st.session_state.aba

with st.form("form_reserva"):
    dict_dados = obter_dados_reserva()
    enviado = st.form_submit_button("Adicionar Reserva")
    if enviado:
        df_reservas=carregar_dataframe()
        processar_nova_reserva(df_reservas,dict_dados["Data"],dict_dados,aba)
        st.success("Reserva adicionada com sucesso!")