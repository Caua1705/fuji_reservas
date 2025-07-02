from src.services.session import obter_aba_por_filial
from src.services.resumo import gerar_resumo_reservas
from src.model.resumo_model import registrar_reservas_por_dia

def controlar_reservas_por_dia(df_reservas, filial):
    """Gera e salva o resumo das reservas de uma filial específica."""
    linhas = gerar_resumo_reservas(df_reservas, filial)
    aba = obter_aba_por_filial(filial)
    registrar_reservas_por_dia(aba, linhas)