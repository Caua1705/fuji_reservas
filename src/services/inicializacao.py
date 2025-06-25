import streamlit as st
from src.data.conexao import conectar_planilha, get_abas
from src.services.carregar_dados import carregar_df_reservas

def inicializar_abas_planilha():
    if not all(aba in st.session_state for aba in ["aba_reservas", "aba_resumo_aldeota", "aba_resumo_cambeba"]):
        cliente = conectar_planilha()
        st.session_state.aba_reservas,st.session_state.aba_resumo_aldeota,st.session_state.aba_resumo_cambeba = get_abas(cliente)
    return st.session_state.aba_reservas, st.session_state.aba_resumo_aldeota, st.session_state.aba_resumo_cambeba 
        

def inicializar_dados(aba):
    if "df_reservas" not in st.session_state:
        st.session_state.df_reservas = carregar_df_reservas(aba)
    return st.session_state.df_reservas