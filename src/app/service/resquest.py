# Criar requisição POST

import requests
import json
import os
from requests.auth import HTTPBasicAuth
from settings import parameters

class CallApiEndpoint:
    ''' Classe para realizar chamadas de API para o Golang '''

    def post_request(url, body, headers=None):
        
        # Converte os dados em JSON
        json_body = json.dumps(body)
        
        # Envia a requisição POST
        response = requests.post(url, data=json_body, headers=headers)
        
        return response

