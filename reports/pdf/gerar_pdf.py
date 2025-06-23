from weasyprint import HTML
from reports.reservas_diarias import obter_reservas_do_dia_por_filial
from reports.pdf.variaveis_template import get_variaveis_template
from reports.pdf.renderizar import renderizar_tamplate

def gerar_pdf(caminho_relatorio,caminho_css,pasta_template,data_relatorio):

    dados_filiais,hoje=obter_reservas_do_dia_por_filial(data_relatorio)
    variaveis_template=get_variaveis_template(dados_filiais,hoje,caminho_css)
    template_renderizado=renderizar_tamplate(pasta_template,variaveis_template)

    caminho_relatorio.parent.mkdir(exist_ok=True)

    HTML(string=template_renderizado, base_url=".").write_pdf(caminho_relatorio)

