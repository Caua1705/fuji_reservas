import streamlit as st
from src.utils.config import MAPA_FILIAL_PARA_ABA, MAXIMO_RESERVAS
from src.data.credenciais import get_credenciais_google
from src.services.email_cliente import enviar_email_cliente
from src.services.reservas import processar_nova_reserva
from src.services.resumo import salvar_resumo_reservas

def controlar_nova_reserva(df_reservas, data, dict_dados, aba_reservas):
    """Processa nova reserva e envia email para o cliente."""
    df_atualizado = processar_nova_reserva(
        df_reservas, data, dict_dados, aba_reservas, MAXIMO_RESERVAS
    )

    email_origem, senha_app = get_credenciais_google()
    enviar_email_cliente(
        email_origem,
        senha_app,
        dict_dados["Email"],
        dict_dados["Nome"],
        data,
        dict_dados["Horário"],
        dict_dados["Unidade"],
    )
    return df_atualizado


def controlar_reservas_por_dia(df_reservas, filial):
    """Salva resumo de reservas por filial na planilha do google."""
    salvar_resumo_reservas(df_reservas, filial, MAPA_FILIAL_PARA_ABA, st.session_state)