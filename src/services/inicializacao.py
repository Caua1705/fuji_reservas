import streamlit as st
from src.data.conexao import get_abas
from src.services.carregar_dados import carregar_df_reservas
from src.config.settings import MAPA_FILIAL_PARA_ABA

def inicializar_abas_planilha():
    if not all(aba in st.session_state for aba in MAPA_FILIAL_PARA_ABA.values()):
        for chave, aba in zip(MAPA_FILIAL_PARA_ABA.values(), get_abas()):
            st.session_state[chave] = aba
        

def inicializar_dados(aba):
    if "df_reservas" not in st.session_state:
        st.session_state["df_reservas"] = carregar_df_reservas(aba)
    return st.session_state["df_reservas"] 