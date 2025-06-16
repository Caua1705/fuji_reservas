import streamlit as st
from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from services.carregar_dados import carregar_dataframe
from controller.reservas_controller import controlar_nova_reserva

# Configuração da página
st.set_page_config(layout="wide")
st.markdown("""
    <style>
        .titulo-principal {
            text-align: center;
            font-size: 2.5em;
            color: #d62828;
            margin-bottom: 0.2em;
        }

        .subtitulo {
            text-align: center;
            font-size: 1.2em;
            color: #333;
        }

        .caixa-form {
            background-color: #f9f9f9;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 0 8px rgba(0,0,0,0.08);
            margin-top: 20px;
        }

        .stButton > button {
            background-color: #d62828;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho centralizado
col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    st.markdown("<div class='titulo-principal'>📅 Sistema de Reservas Fuji</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitulo'>Organize, registre e acompanhe suas reservas de forma prática e segura.</div>", unsafe_allow_html=True)

st.divider()

# Inicialização do estado
if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

aba = st.session_state.aba

# Formulário dentro de um container estilizado
with st.container():
    st.markdown("<div class='caixa-form'>", unsafe_allow_html=True)

    with st.form("form_reserva"):
        st.subheader("➕ Adicionar Nova Reserva")
        dict_dados = obter_dados_reserva()
        enviado = st.form_submit_button("✅ Adicionar Reserva")

        if enviado:
            controlar_nova_reserva(st.session_state.df_reservas, dict_dados["Data"], dict_dados, aba)
            st.session_state.df_reservas = carregar_dataframe()
            st.success("✅ Reserva adicionada com sucesso!")
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

# Exibição das últimas reservas
st.divider()
st.subheader("📋 Reservas Recentes")
st.dataframe(st.session_state.df_reservas.tail(10), use_container_width=True)