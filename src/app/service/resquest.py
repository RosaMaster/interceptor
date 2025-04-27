# Criar requisição POST

import requests
import json
import os
from requests.auth import HTTPBasicAuth
from settings import parameters

class CallApiEndpoint:
    ''' Classe para realizar chamadas de API para o Golang '''


    # []TODO: A cada 24  horas renovar o token de autenticação

    def post_request(url, body, headers=None):
        
        # Converte os dados em JSON
        json_body = json.dumps(body)
        
        # Envia a requisição POST
        response = requests.post(url, data=json_body, headers=headers)
        
        return response
    

    def get_token():
        ''' Gera o token de autenticação '''
        
        # Define os parâmetros de autenticação
        url = parameters.Parametros.url_api_golang.value + "/token"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        # Define o corpo da requisição
        body = {
            "user": parameters.Parametros.user_api.value,
            "password": parameters.Parametros.password_api.value
        }
        
        # Envia a requisição POST para gerar o token
        response = CallApiEndpoint.post_request(url, body, headers)
        
        # Retorna o token se a requisição for bem-sucedida
        if response.status_code == 200:
            return response.json().get('token')
        
        return None

