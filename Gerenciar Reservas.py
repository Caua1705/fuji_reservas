import streamlit as st
from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from services.carregar_dados import carregar_dataframe
from controller.reservas_controller import controlar_nova_reserva

st.set_page_config(layout="wide")

# Estilo visual
st.markdown("""
    <style>
        .titulo {
            text-align: center;
            font-size: 2.2em;
            color: #d62828;
            margin-bottom: 10px;
        }
        .subtitulo {
            text-align: center;
            font-size: 1.1em;
            color: #444;
            margin-bottom: 30px;
        }
        .form-card {
            background-color: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        .stButton > button {
            background-color: #d62828;
            color: white;
            border-radius: 6px;
            padding: 10px 20px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("<div class='titulo'>🍣 Sistema de Reservas Fuji</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitulo'>Organize, registre e acompanhe suas reservas de forma prática e segura em tempo real.</div>", unsafe_allow_html=True)

# Estado inicial
if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

aba = st.session_state.aba

# Formulário em card
st.markdown("<div class='form-card'>", unsafe_allow_html=True)

with st.form("form_reserva"):
    st.subheader("➕ Nova Reserva")
    dict_dados = obter_dados_reserva()
    enviado = st.form_submit_button("Adicionar Reserva")
    
    if enviado:
        controlar_nova_reserva(st.session_state.df_reservas, dict_dados["Data"], dict_dados, aba)
        st.session_state.df_reservas = carregar_dataframe()
        st.success("✅ Reserva adicionada com sucesso!")
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)