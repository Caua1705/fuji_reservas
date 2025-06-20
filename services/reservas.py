import pandas as pd
import streamlit as st
from utils.formatadores import formatar_nova_linha,ORDEM_CAMPOS_RESERVA,formatar_data,formatar_dados,formatar_linhas_agrupadas
from services.filtrar import filtrar_dataframe,filtrar_por_filial
from services.agrupar import agrupar_por_dia
from services.validacoes import validar_reserva
from model.adicionar import registrar_reserva,registrar_reservas_por_dia


def processar_nova_reserva(df_reservas, data, dict_dados, aba, maximo_reservas=50):
    # Formata a nova linha para adicionar na planilha
    nova_linha = formatar_nova_linha(dict_dados, ORDEM_CAMPOS_RESERVA)
    #Cria um DataFrame com a nova linha
    df_nova_linha = pd.DataFrame([nova_linha], columns=df_reservas.columns)
    df_nova_linha = formatar_dados(df_nova_linha)
    # Cria o DataFrame atualizado simulando a adição
    df_atualizado = pd.concat([df_reservas, df_nova_linha], ignore_index=True)
    # df_atualizado=converter_datav(df_atualizado)
    # Filtra as reservas do mesmo dia para validação
    df_filtrado = filtrar_dataframe(df_atualizado, data)
    
    # Valida se o total de reservas para o dia excede o máximo
    validar_reserva(df_filtrado, maximo_reservas)
    # Registra na planilha
    registrar_reserva(nova_linha, aba)
    return df_atualizado

def processar_reservas_agrupadas(df_reservas,filial,aba2,aba3):
    df_filtrado=filtrar_por_filial(df_reservas,filial)
    df_agrupado=agrupar_por_dia(df_filtrado)
    df_agrupado=formatar_data(df_agrupado,"Data")
    linhas = formatar_linhas_agrupadas(df_agrupado)
    registrar_reservas_por_dia(linhas,filial,aba2,aba3)


def exibir_resumo(df_reservas, ambiente, filial):
    df_agrupado_filial=df_reservas.loc[df_reservas["Unidade"]==filial]
    st.write(df_agrupado_filial)
    
    if df_agrupado_filial.empty:
        st.info(f"Nenhuma reserva no ambiente **{ambiente}** para esta data.")
        return

    horarios_unicos = df_agrupado_filial["Horário"].unique()

    for horario in horarios_unicos:
        df_horario = df_agrupado_filial.loc[df_agrupado_filial["Horário"]==horario]
        total_pessoas = df_horario["Número de Pessoas"].sum()
        qtd_reservas = len(df_horario)

        with st.expander(f"🕒 {horario} – {qtd_reservas} reserva(s), {total_pessoas} pessoa(s)"):
            for _, row in df_horario.iterrows():
                st.markdown(f"""
                <div style="border:1px solid #DDD; border-radius:10px; padding:10px; margin-bottom:6px; background-color:#f9f9f9;">
                    <strong>👤 {row['Nome']}</strong><br>
                    👥 {row['Número de Pessoas']} pessoas<br>
                    📞 {row['Telefone']}<br>
                    ✉️ {row['Email']}<br>
                    📝 {row['Observações'] or 'Sem observações'}
                </div>
                """, unsafe_allow_html=True)