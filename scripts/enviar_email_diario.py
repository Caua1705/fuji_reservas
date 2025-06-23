from pathlib import Path
import smtplib
from email.message import EmailMessage
from datetime import date
from reports.pdf.gerar_pdf import gerar_pdf
from reports.pdf.estilizar_pdf import estilizar_pdf
from src.data.credenciais import carregar_credenciais_email


def enviar_relatorio_diario_por_email(email_origem,
                         email_destinatario,
                         senha_app,
                         nome_pessoa,
                         data_relatorio,
                         pasta_template_pdf,
                         nome_template,
                         caminho_relatorio_pdf,
                         caminho_css,
                         caminho_layout_pdf):

    try:
        msg = EmailMessage()
        msg["Subject"] = f"Relatório Diário de Reservas - Fuji Lounge - {data_relatorio} - Para {nome_pessoa}"
        msg["From"] = email_origem
        msg["To"] = email_destinatario

        gerar_pdf(caminho_relatorio_pdf,caminho_css,pasta_template_pdf,nome_template,data_relatorio)
        estilizar_pdf(caminho_relatorio_pdf,caminho_layout_pdf)

        html_content = f"""
                <html>
                <body>
                    <p>Olá Carlos,</p>
                    <p>Segue em anexo o <strong>Relatório Diário</strong> do <strong>Fuji Lounge</strong> referente a <b>23/06/2025</b>.</p>
                    <p>Atenciosamente,<br>Equipe Fuji Lounge</p>
                </body>
                </html>
                """

        msg.add_alternative(html_content, subtype="html")

        with open(caminho_relatorio_pdf,"rb") as leitor_pdf:
            pdf=leitor_pdf.read()
            msg.add_attachment(
               pdf,
               maintype="application",
               subtype="pdf",
               filename=caminho_relatorio_pdf.name
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_origem, senha_app)
            smtp.send_message(msg)

    except smtplib.SMTPRecipientsRefused:
        raise smtplib.SMTPException(f"Não foi possível enviar o e-mail para **{email_destinatario}**. Verifique se o endereço está correto.")
    
email_origem,senha_app=carregar_credenciais_email()
pasta_template_pdf=Path(__file__).parents[1] / "templates" / "pdf"
nome_template_pdf=pasta_template_pdf / "template_reservas"
caminho_css=Path(__file__).parents[1] / "static" / "css" / "reservas_diarias.css"
caminho_layout_pdf=pasta_template_pdf / "layout.pdf"
email_destinatario="cauaccarvalho10@gmail.com"
nome_pessoa="Cauã"
data_relatorio=date.today()
caminho_relatorio_pdf=Path(__file__).parents[1] / "output" / f"Relatório Diário - {data_relatorio}.pdf"

enviar_relatorio_diario_por_email(email_origem,
                         email_destinatario,
                         senha_app,
                         nome_pessoa,
                         data_relatorio,
                         pasta_template_pdf,
                         nome_template_pdf,
                         caminho_relatorio_pdf,
                         caminho_css,
                         caminho_layout_pdf)

