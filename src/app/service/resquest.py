# Criar requisição POST

import os
import requests
from requests.auth import HTTPBasicAuth
from settings.parameters import Parametros

class CallApiEndpoint:
    ''' Classe para realizar chamadas de API para o Golang '''

    def post_request(body):
        ''' Envia uma requisição POST para a API Golang '''
        
        # Define os parâmetros da requisição
        url = Parametros.url_api_golang.value

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Envia a requisição POST
        response = requests.post(url, data=body, headers=headers)
        
        return response
    

    def get_token():
        ''' Gera o token de autenticação '''
        
        # Define os parâmetros de autenticação
        url = Parametros.url_api_golang_token.value + "/token"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Define o corpo da requisição
        body = {
            "user": Parametros.user_api.value,
            "password": Parametros.password_api.value
        }
        
        # Envia a requisição POST para gerar o token
        response = CallApiEndpoint.post_request(url, body, headers)
        
        # Retorna o token se a requisição for bem-sucedida
        if response.status_code == 200:
            return response.json().get('token')
        else:
            print(f"Erro ao obter token: {response.status_code} - {response.text}")
            return None
