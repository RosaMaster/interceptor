import enum
import uuid

class Parametros(enum.Enum):
    ''' Classe de parâmetros para o interceptor '''

    url_api_golang = "http://localhost:8080/api/v1/interceptor"
    company_id = "0d0c1a67-503f-4fa5-a2e4-40b945339f20"

    # TOKEN DE AUTENTICAÇÃO
    url_api_golang_token = "http://localhost:8080/api/v1/login/token"
    user_token_api = "user_token_api"
    password_toke_api = "senha123"

    # TESTES
    placa_teste = ["ABC1D23", "EFG4H56", "IJK7L89", "MNO0P12", "QRS3T45", "UVW6X78", "YZA9B01", "CDE2F34", "GHI5J67", "JKL8M90", "MNO1P23", "QRS4T56", "UVW7X89", "YZA0B12", "CDE3F45", "GHI6J78", "JKL9M01", "ABC2D34", "EFG5H67", "IJK8L90", "MNO2P12", "QRS5T45", "UVW8X78", "YZA1B01", "CDE4F34", "GHI7J67", "JKL0M90", "MNO3P23", "QRS6T56", "UVW9X89", "YZA2B12", "CDE5F45", "GHI8J78", "JKL1M01"]
    status_teste = [0, 1]  # 0 = Entrada, 1 = Saída
    token_teste = str(uuid.uuid4())
    feature_toggle_database = True
    feature_toggle_object = True
    feature_toggle_call_api = True