from src.services.carregar_dados import carregar_todas_as_reservas
from src.services.filtrar import filtrar_filial_e_data
from src.utils.formatadores import formatar_data

def obter_reservas_do_dia_por_filial(data_relatorio):
    df_reservas=carregar_todas_as_reservas()
    filiais=["Aldeota","Cambeba"]
    
    dados_filiais = {}
    for filial in filiais:
        df_filial=filtrar_filial_e_data(df_reservas,filial,data_relatorio)
        df_filial=formatar_data(df_filial,"Data")
        df_filial=df_filial[["Data","Horário","Nome","Telefone","Número de Pessoas","Área do Restaurante"]]

        dados_filiais[filial.lower()] = {
            "tabela" : df_filial,
            "total_reservas" : len(df_filial),
            "total_pessoas" : df_filial["Número de Pessoas"].sum()
        }

    return dados_filiais,data_relatorio