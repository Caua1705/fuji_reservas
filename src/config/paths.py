from pathlib import Path

BASE_DIR=Path(__file__).parents[2]

CAMINHOS={
    "Credenciais_google": BASE_DIR / "credenciais_google.json",
    "Credenciais_email": BASE_DIR / "credenciais_email.json",
    "Pasta_templates": BASE_DIR / "templates",
    "Layout_relatorio": BASE_DIR / "assets" / "layout.pdf",
    "Css_email_clientes": BASE_DIR / "static" / "css" / "email_cliente.css",
    "Css_email_relatorio": BASE_DIR / "static" / "css" / "relatorio.css",
}
