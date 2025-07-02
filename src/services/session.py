import streamlit as st
from src.config.settings import MAPA_FILIAL_PARA_ABA

def obter_aba_geral():
    nome_aba_geral = MAPA_FILIAL_PARA_ABA[None]
    return st.session_state[nome_aba_geral]


def obter_aba_por_filial(filial):
    nome_aba = MAPA_FILIAL_PARA_ABA[filial]
    return st.session_state[nome_aba]
