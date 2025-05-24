from settings.parameters import Parametros

class InfoSistemaInterceptor:
    """ Classe InfoSistema. Contém informações do sistema, como cabeçalho e rodapé. """

    company = Parametros.company_id.value

    cabecacho = f"""
    ########################################################################
    -- Interceptor Project
    -- version 1.0.0
    -- Autor: DRP01-PJI310-SALA-002GRUPO-014
    -- Data: 2025-05-20
    -- Company ID: {company}
    -- Inicializando Programa
    ########################################################################
    """

    rodape = """
    ########################################################################
    -- Finalizando Programa 
    ########################################################################
    """
