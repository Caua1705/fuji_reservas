import smtplib
from src.config.paths import CAMINHOS
from src.config.settings import SMTP_SERVER, SMTP_PORT, ASSUNTO_EMAIL_CLIENTE, TEMPLATE_EMAIL_CLIENTE, MSG_ERRO_EMAIL_CLIENTE
from email.message import EmailMessage
from src.services.variaveis_template import variaveis_template_email_cliente
from src.services.renderizar import renderizar_tamplate

def montar_email_cliente(email_origem, email_cliente, nome_cliente, data, hora, unidade):
    msg = EmailMessage()
    msg["Subject"] = ASSUNTO_EMAIL_CLIENTE
    msg["From"] = email_origem
    msg["To"] = email_cliente

    variaveis_template=variaveis_template_email_cliente(nome_cliente,data,hora,unidade,CAMINHOS["Css_email_clientes"])
    template_renderizado=renderizar_tamplate(CAMINHOS["Pasta_templates"],
                                             TEMPLATE_EMAIL_CLIENTE,
                                             variaveis_template)

    msg.add_alternative(template_renderizado, subtype="html")
    return msg


def enviar_email_cliente(email_origem, senha_app, email_cliente, nome_cliente, data, hora, unidade): 
    try:
        msg = montar_email_cliente(email_origem, email_cliente, nome_cliente, data, hora, unidade)
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(email_origem, senha_app)
            smtp.send_message(msg)
    except smtplib.SMTPRecipientsRefused:
        raise smtplib.SMTPException(
    f"{MSG_ERRO_EMAIL_CLIENTE} (**{email_cliente}**)"
)