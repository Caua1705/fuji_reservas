def variaveis_template_relatorio_diario(dados_filiais,data_relatorio,caminho_css):
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

def variaveis_template_email_cliente(nome_cliente,data,hora,unidade,caminho_css):
    variaveis_template={"nome_cliente":nome_cliente,
               "data":data,
               "hora":hora,
               "unidade":unidade
               }
    with open(caminho_css,"r") as style:
        css=style.read()
    variaveis_template["stylesheet"]=css
    return variaveis_template