from src.services.session import obter_aba_geral
from src.config.settings import  MAXIMO_RESERVAS
from src.services.reservas import preparar_reserva_para_salvar
from src.model.reservas_model import registrar_reserva
from src.data.credenciais import get_credenciais_email
from src.services.email_cliente import enviar_email_cliente

def controlar_nova_reserva(df_reservas, data, dict_dados):
    """Processa nova reserva, salva no Google Sheets e envia email de confirmação."""
    df_atualizado, nova_linha = preparar_reserva_para_salvar(df_reservas, data, dict_dados, MAXIMO_RESERVAS)
    aba = obter_aba_geral()
    registrar_reserva(aba, nova_linha)

    email_origem, senha_app = get_credenciais_email()
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
    
