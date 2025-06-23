from weasyprint import HTML
from reports.reservas_diarias import obter_reservas_do_dia_por_filial
from src.services.variaveis_template import variaveis_template_relatorio_diario
from src.services.renderizar import renderizar_tamplate

def gerar_pdf(caminho_relatorio,caminho_css,pasta_template,nome_template,data_relatorio):

    dados_filiais,hoje=obter_reservas_do_dia_por_filial(data_relatorio)
    variaveis_template=variaveis_template_relatorio_diario(dados_filiais,hoje,caminho_css)
    template_renderizado=renderizar_tamplate(pasta_template,nome_template,variaveis_template)

    caminho_relatorio.parent.mkdir(exist_ok=True)

    HTML(string=template_renderizado, base_url=".").write_pdf(caminho_relatorio)

