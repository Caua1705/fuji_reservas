import streamlit as st
from datetime import datetime
from src.config.settings import HORARIOS_RESERVAS

def obter_dados_reserva():
    # Estilo CSS customizado
    st.markdown("""
        <style>
        .main {
            background-color: #FAFAFA;
        }
        h1, h2, h3, h4 {
            color: #333;
            font-family: 'Segoe UI', sans-serif;
        }
        input, select, textarea {
            border-radius: 8px !important;
            border: 1px solid #ccc !important;
            padding: 6px !important;
        }
        button[kind="primary"] {
            background-color: #6C63FF !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            font-weight: 600;
        }
        button[kind="secondary"] {
            border-radius: 8px !important;
        }
        textarea::placeholder {
            color: #999 !important;
            font-style: italic;
        }
        .stTextInput, .stSelectbox, .stNumberInput, .stDateInput, .stTextArea {
            padding-top: 4px;
            padding-bottom: 4px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Cabeçalho da página
    st.markdown("## 📝 Nova Reserva")
    st.caption("Formulário para registrar a reserva de um cliente.")

    # Seção 1: Cliente
    st.markdown("#### Informações do Cliente")
    col1, col2 = st.columns(2)

    with col1:
        nome = st.text_input("Nome completo *")
        telefone = st.text_input("Telefone (somente números) *")
        email = st.text_input("E-mail para confirmação *")

    with col2:
        quantidade_pessoas = st.number_input("Número de pessoas *", min_value=1, value=1)
        filial = st.selectbox("Unidade", ["Aldeota", "Cambeba"])
        area = st.selectbox("Área do restaurante *", ["Interno", "Externo"])

    # Seção 2: Agendamento
    st.markdown("#### Agendamento da Mesa")
    col3, col4 = st.columns(2)
    with col3:
        data = st.date_input("Data *", value=datetime.today(), format="DD/MM/YYYY")
    with col4:
        horario = st.selectbox("Horário *", HORARIOS_RESERVAS)

    # Seção 3: Observações
    st.markdown("#### Observações (opcional)")
    observacoes = st.text_area(
        "",
        placeholder="Deseja informar alguma preferência ou pedido especial?"
    )

    return {
        "Data": data,
        "Horário": horario,
        "Nome": nome,
        "Telefone": telefone,
        "Email": email,
        "Número de Pessoas": quantidade_pessoas,
        "Unidade": filial,
        "Área do Restaurante": area,
        "Observações": observacoes
    }