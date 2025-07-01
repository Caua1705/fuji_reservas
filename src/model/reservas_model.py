import streamlit as st

def ler_todas_reservas(aba):
    return aba.get_all_values()


def registrar_reserva(nova_linha,aba):
    aba.append_row(nova_linha)


def registrar_reservas_por_dia(linhas, filial, mapa_filial, abas_no_session_state):
    nome_aba = mapa_filial[filial]
    aba_selecionada = abas_no_session_state[nome_aba]
    aba_selecionada.batch_clear(['A2:C'])
    aba_selecionada.update('A2', linhas)
