from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from controller.atualizar import atualizar_dataframe
import streamlit as st

st.set_page_config(layout="wide")

#Cria conexão
aba = conectar_planilha()
nova_linha=obter_dados_reserva()
if st.button("Adicionar Reserva"):
    #Coleta dados da Interface
    #Adiciona a nova linha
    atualizar_dataframe(nova_linha,aba)
