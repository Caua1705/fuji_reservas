SCOPES = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
MAPA_FILIAL_PARA_ABA = {
    None: "aba_reservas",
    "Aldeota": "aba_resumo_aldeota",
    "Cambeba": "aba_resumo_cambeba",
}
COLUNAS_RESERVA = ["Data", "Horário", "Nome", "Telefone", "Email", "Número de Pessoas", "Unidade", "Área do Restaurante", "Observações"]
ASSUNTO_EMAIL_CLIENTE = "🥢 Sua experiência exclusiva no Fuji Lounge está confirmada"
TEMPLATE_EMAIL_CLIENTE = "email_cliente.jinja"
MSG_ERRO_EXCESSO_RESERVAS = "⚠️ Limite de reservas excedido para esse horário. Tente escolher outro horário ou data."
MSG_ERRO_EMAIL_CLIENTE = "❌ Não foi possível enviar o e-mail para o destinatário. Verifique se o endereço está correto."
MAXIMO_RESERVAS = 50