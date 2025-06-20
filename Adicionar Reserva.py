import streamlit as st
from services.inicializacao import inicializar_abas_planilha,inicializar_dados
from view.entrada_reserva import obter_dados_reserva
from controller.reservas_controller import controlar_nova_reserva,controlar_reservas_por_dia
import smtplib

# Config da página
st.set_page_config(page_title="🍣 Fuji Lounge – Reservas", layout="wide")

# Título
st.markdown(
    """
    <div style='text-align:center; padding: 1rem 0'>
        <h2 style='margin-bottom:0.2em;'>📝 Nova Reserva</h2>
        <p style='color:gray; font-size:1.1em;'>Preencha o formulário abaixo para registrar uma nova reserva</p>
    </div>
    """, unsafe_allow_html=True
)

# Inicializa Planilha e Dados
aba,aba2,aba3=inicializar_abas_planilha()
df_reservas=inicializar_dados()

# 📝 Formulário de nova reserva 
with st.form("form_reserva", border=True):
    dict_dados = obter_dados_reserva()

    enviado = st.form_submit_button("✅ Adicionar Reserva")

    if enviado:
        campos_obrigatorios = ["Nome", "Email", "Data", "Horário", "Unidade"]
        if not all([dict_dados.get(campo) for campo in campos_obrigatorios]):
            st.warning("⚠️ Preencha todos os campos obrigatórios marcados com *.")
        else:
            try:
                df_atualizado = controlar_nova_reserva(
                    st.session_state.df_reservas,
                    dict_dados["Data"],
                    dict_dados,
                    aba
                )
                st.session_state.df_reservas=df_atualizado
                controlar_reservas_por_dia(st.session_state.df_reservas,
                                            dict_dados["Unidade"],
                                            aba2,
                                            aba3)
                st.success(f"✅ **Reserva para {dict_dados['Nome']} adicionada com sucesso!**")
                st.info("📩 Um e-mail de confirmação foi enviado ao cliente.")
            # Excesso de reservas
            except ValueError as e:
                st.error(e)  
            # Não foi possível enviar o email
            except smtplib.SMTPException as e:
                st.error(e)
        