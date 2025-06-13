from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from controller.atualizar import atualizar_dataframe
import streamlit as st

st.set_page_config(layout="wide")


# Título e Subtítulo
st.title("Sistema de Gerenciamento de Reservas Fuji")
st.markdown("### Organize, registre e acompanhe suas reservas de forma prática e segura em tempo real.")


#Cria conexão
if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()
aba = st.session_state.aba
with st.form("form_reserva"):
    nova_linha = obter_dados_reserva()
    enviado = st.form_submit_button("Adicionar Reserva")
    if enviado:
        atualizar_dataframe(nova_linha, aba)
        st.success("Reserva adicionada com sucesso!")