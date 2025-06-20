import streamlit as st
from data.conexao import conectar_planilha
from services.carregar_dados import carregar_todas_as_reservas

def inicializar_abas_planilha():
    if ("aba" not in st.session_state 
        or "aba2" not in st.session_state 
        or "aba3" not in st.session_state):
        st.session_state.aba,st.session_state.aba2,st.session_state.aba3 = conectar_planilha()
    return st.session_state.aba,st.session_state.aba2,st.session_state.aba3

def inicializar_dados():
    if "df_reservas" not in st.session_state:
        st.session_state.df_reservas = carregar_todas_as_reservas()
    return st.session_state.df_reservas