from email.message import EmailMessage
import smtplib

def enviar_email_cliente(email_origem, email_cliente, senha_app, nome_cliente, data, hora, unidade):
    msg = EmailMessage()
    msg["Subject"] = "🥢 Sua experiência exclusiva no Fuji Lounge está confirmada"
    msg["From"] = email_origem
    msg["To"] = email_cliente

    html_content = f"""
    <html>
    <body>
        <p>Olá, <strong>{nome_cliente}</strong> 👋,</p>

        <p>Sua reserva para o dia <strong>{data}</strong> às <strong>{hora}</strong> na unidade <strong>{unidade}</strong> do <strong>Fuji Lounge</strong> está confirmada! 🍣✨</p>

        <p>Prepare-se para uma experiência gastronômica exclusiva, onde cada detalhe é pensado para encantar seu paladar e criar momentos inesquecíveis. 🥢🎌</p>

        <p>Se precisar alterar alguma coisa, estamos à disposição para ajudar. 📞📧</p>

        <p>Aguardamos ansiosos a sua visita! 🙌</p>

        <p>Com apreço,<br>Equipe <strong>Fuji Lounge</strong> 🍱</p>
    </body>
    </html>
    """

    msg.add_alternative(html_content, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_origem, senha_app)
        smtp.send_message(msg)