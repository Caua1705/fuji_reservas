import streamlit as st
from data.conexao import conectar_planilha
from view.entrada_reserva import obter_dados_reserva
from services.carregar_dados import carregar_dataframe
from controller.reservas_controller import controlar_nova_reserva

# Configuração da página
st.set_page_config(
    page_title="Sistema de Reservas Fuji 🍣",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo customizado
st.markdown("""
    <style>
    .main-title {
        font-size: 42px;
        text-align: center;
        color: #d62828;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #444;
        margin-bottom: 30px;
    }
    .form-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
        margin: 0 auto;
    }
    .stButton > button {
        background-color: #d62828;
        color: white;
        border-radius: 6px;
        font-weight: bold;
        padding: 10px 24px;
        font-size: 16px;
    }
    .section-title {
        font-size: 22px;
        color: #222;
        margin-top: 40px;
        margin-bottom: 10px;
    }
    hr {
        border: 1px solid #eee;
        margin: 25px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Título central
st.markdown("<div class='main-title'>🍣 Sistema de Reservas Fuji</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Organize, registre e acompanhe suas reservas de forma prática e segura. Bem-vindo ao sistema do Fuji!</div>", unsafe_allow_html=True)

# Conexão com planilha
if "aba" not in st.session_state:
    st.session_state.aba = conectar_planilha()

if "df_reservas" not in st.session_state:
    st.session_state.df_reservas = carregar_dataframe()

aba = st.session_state.aba

# Formulário de nova reserva
st.markdown("<div class='form-card'>", unsafe_allow_html=True)
st.subheader("➕ Nova Reserva")

with st.form("form_reserva"):
    dict_dados = obter_dados_reserva()
    enviado = st.form_submit_button("🍱 Adicionar Reserva")

    if enviado:
        controlar_nova_reserva(st.session_state.df_reservas, dict_dados["Data"], dict_dados, aba)
        st.session_state.df_reservas = carregar_dataframe()
        st.success("✅ Reserva adicionada com sucesso!")
        st.balloons()

st.markdown("</div>", unsafe_allow_html=True)

# Tabela de últimas reservas
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='section-title'>📋 Últimas Reservas Registradas</div>", unsafe_allow_html=True)
st.dataframe(st.session_state.df_reservas.tail(10), use_container_width=True)