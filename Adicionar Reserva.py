import streamlit as st
import smtplib
from src.config.settings import MSG_SUCESSO_RESERVA, MSG_INFO_EMAIL_ENVIADO
from src.services.validacoes import validar_campos_nova_reserva
from src.services.inicializacao import inicializar_abas_planilha,inicializar_dados
from src.view.entrada_reserva import obter_dados_reserva
from src.controller.reservas_controller import controlar_nova_reserva,controlar_reservas_por_dia

st.set_page_config(page_title="Fuji Lounge – Reservas", layout="wide", page_icon="🍣")
 
st.markdown("## 📝 Nova Reserva")

# Inicializa Planilha e Dados
aba_reservas, aba_resumo_aldeota,aba_resumo_cambeba = inicializar_abas_planilha()
df_reservas = inicializar_dados(aba_reservas)

# 📝 Formulário de nova reserva 
with st.form("nova_reserva", border=True):
    dict_dados = obter_dados_reserva()
    enviado = st.form_submit_button("✅ Adicionar Reserva")

    if enviado:
        try:
            validar_campos_nova_reserva(dict_dados)
            df_atualizado = controlar_nova_reserva(
                st.session_state.df_reservas,
                dict_dados["Data"],
                dict_dados,
                aba_reservas
            )
            controlar_reservas_por_dia(st.session_state.df_reservas,
                                        dict_dados["Unidade"],
                                        aba_resumo_aldeota,
                                        aba_resumo_cambeba)
            
            st.session_state.df_reservas=df_atualizado
            
            st.success(MSG_SUCESSO_RESERVA.format(nome=dict_dados["Nome"]))
            st.info(MSG_INFO_EMAIL_ENVIADO)

        #Campos não preenchidos corretamente
        except ValueError as e:
            st.warning(e)
        # Excesso de reservas
        except ValueError as e:
            st.error(e)  
        # Não foi possível enviar o email
        except smtplib.SMTPException as e:
            st.error(e)
    