import enum

class Parametros(enum.Enum):
    ''' Classe de parâmetros para o interceptor '''

    url_api_golang = "http://localhost:8080/api/v1/interceptor"
    url_api_golang_token = "http://localhost:8080/api/v1/login"
    user_api = ""
    password_api = "123456"
    company_id = "aaaaaaa-aaaaaaa-aaaaaaa-aaaaaaa"
