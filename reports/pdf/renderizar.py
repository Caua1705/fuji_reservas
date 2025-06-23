from jinja2 import FileSystemLoader,Environment

def renderizar_tamplate(pasta_template,variaveis_template):
    carregamento_pasta_template=FileSystemLoader(pasta_template)
    env=Environment(loader=carregamento_pasta_template)
    template=env.get_template("template_reservas.jinja")
    template_renderizado=template.render(**variaveis_template)
    return template_renderizado
