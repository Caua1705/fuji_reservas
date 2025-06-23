def get_variaveis_template(dados_filiais,data_relatorio,caminho_css):
    variaveis_template={
    "data_relatorio":data_relatorio.strftime("%d/%m/%Y"),
}
    for filial,dados in dados_filiais.items():
        variaveis_template[f"Tabela_{filial}"]=dados["tabela"].to_html(index=False)
        variaveis_template[f"Total_reservas_{filial}"]=dados["total_reservas"]
        variaveis_template[f"Total_pessoas_{filial}"]=dados["total_pessoas"]

    with open(caminho_css,"r") as style:
        css=style.read()
    variaveis_template["stylesheet"]=css
    return variaveis_template
