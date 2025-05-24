import enum

class Parametros(enum.Enum):
    ''' Classe de parâmetros para o interceptor '''

    url_api_golang = "http://localhost:8080/api/v1/interceptor"
    company_id = "0d0c1a67-503f-4fa5-a2e4-40b945339f20"

    # TOKEN DE AUTENTICAÇÃO
    url_api_golang_token = "http://localhost:8080/api/v1/login/token"
    user_token_api = "user_token_api"
    password_toke_api = "senha123"

    # TESTES
    status_teste = 1
    token_teste = "aaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"
    feature_toggle_object = True
    feature_toggle_call_api = True
