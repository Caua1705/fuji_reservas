import pypdf

def estilizar_pdf(caminho_relatorio,caminho_layout_pdf):
    pagina_conteudo=pypdf.PdfReader(caminho_relatorio)
    pagina_layout=pypdf.PdfReader(caminho_layout_pdf).pages[0]
    escritor=pypdf.PdfWriter()
    for pagina in pagina_conteudo.pages:
        pagina.merge_page(pagina_layout,over=True)
        escritor.add_page(pagina)
    escritor.write(caminho_relatorio)