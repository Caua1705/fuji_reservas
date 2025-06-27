from src.model.reservas_model import registrar_reservas_por_dia
from src.services.filtrar import filtrar_por_filial
from src.utils.formatadores import formatar_coluna_data_para_string, formatar_linhas_agrupadas
from src.services.agrupar import agrupar_por_dia

def gerar_resumo_reservas(df_reservas,filial):
    df_filtrado=filtrar_por_filial(df_reservas,filial)
    df_agrupado=agrupar_por_dia(df_filtrado)
    df_agrupado=formatar_coluna_data_para_string(df_agrupado,"Data")
    linhas_resumo = formatar_linhas_agrupadas(df_agrupado)
    return linhas_resumo


def salvar_resumo_reservas(df_reservas, filial, mapa_filial, abas_no_session_state):
    linhas = gerar_resumo_reservas(df_reservas, filial)
    registrar_reservas_por_dia(linhas, filial, mapa_filial, abas_no_session_state)


# def exibir_resumo(df_reservas, ambiente):
#     if df_reservas.empty:
#         st.info(f"Nenhuma reserva no ambiente **{ambiente}** para esta data.")
#         return

#     horarios_unicos = df_reservas["Horário"].unique()

#     for horario in horarios_unicos:
#         df_horario = df_reservas.loc[df_reservas["Horário"]==horario]
#         total_pessoas = df_horario["Número de Pessoas"].sum()
#         qtd_reservas = len(df_horario)

#         with st.expander(f"🕒 {horario} – {qtd_reservas} reserva(s), {total_pessoas} pessoa(s)"):
#             for _, row in df_horario.iterrows():
#                 st.markdown(f"""
#                 <div style="border:1px solid #DDD; border-radius:10px; padding:10px; margin-bottom:6px; background-color:#f9f9f9;">
#                     <strong>👤 {row['Nome']}</strong><br>
#                     👥 {row['Número de Pessoas']} pessoas<br>
#                     📞 {row['Telefone']}<br>
#                     ✉️ {row['Email']}<br>
#                     📝 {row['Observações'] or 'Sem observações'}
#                 </div>
#                 """, unsafe_allow_html=True)