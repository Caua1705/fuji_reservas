from src.services.variaveis_template import variaveis_template_email_cliente
from src.services.renderizar import renderizar_tamplate
from pathlib import Path
from email.message import EmailMessage
import smtplib

def enviar_email_cliente(email_origem, email_cliente, senha_app, nome_cliente, data, hora, unidade):
    try:
        msg = EmailMessage()
        msg["Subject"] = "🥢 Sua experiência exclusiva no Fuji Lounge está confirmada"
        msg["From"] = email_origem
        msg["To"] = email_cliente

        pasta_template=Path(__file__).parents[2] / "templates" 
        nome_template= "email/email_cliente.jinja"
        caminho_css=Path(__file__).parents[2] / "static" / "css" / "email_cliente.css"
        variaveis_template=variaveis_template_email_cliente(nome_cliente,data,hora,unidade,caminho_css)
        template_renderizado=renderizar_tamplate(pasta_template,nome_template,variaveis_template)

        msg.add_alternative(template_renderizado, subtype="html")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_origem, senha_app)
            smtp.send_message(msg)

    except smtplib.SMTPRecipientsRefused:
        raise smtplib.SMTPException(f"❌ Não foi possível enviar o e-mail para **{email_cliente}**. Verifique se o endereço está correto.")