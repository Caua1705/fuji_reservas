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
COLUNAS_PLANILHA_RESERVAS = ["Data", "Horário", "Nome", "Telefone", "Email", "Número de Pessoas", "Unidade", "Área do Restaurante", "Observações"]
CAMPOS_OBRIGATORIOS_FORMULARIO = ["Data", "Nome", "Email", "Telefone", "Horário", "Unidade"]
HORARIOS_RESERVAS = [
    "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", 
    "20:00", "20:30", "21:00", "21:30", "22:00"
]
MAXIMO_RESERVAS = 50
TEMPLATE_EMAIL_CLIENTE = "email_cliente.jinja"
ASSUNTO_EMAIL_CLIENTE = "🥢 Sua experiência exclusiva no Fuji Lounge está confirmada"
MSG_ERRO_EXCESSO_RESERVAS = "⚠️ Limite de reservas excedido para esse horário. Tente escolher outro horário ou data."
MSG_ERRO_CAMPOS_OBRIGATORIOS = "⚠️ Preencha todos os campos obrigatórios marcados com *."
MSG_ERRO_EMAIL_CLIENTE = "❌ Não foi possível enviar o e-mail para o destinatário. Verifique se o endereço está correto."
MSG_SUCESSO_RESERVA = "✅ Reserva para {nome} adicionada com sucesso!"
MSG_INFO_EMAIL_ENVIADO = "📩 Um e-mail de confirmação foi enviado ao cliente."