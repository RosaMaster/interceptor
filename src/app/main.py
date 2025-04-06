import os
from utils.status import Status
from utils.gerador_data_hora import GeradorDataHora
from service.resquest import CallApiEndpoint
from settings import parameters
import cv2
import pytesseract

objeto_registro = {}

def main():
    '''Função principal do programa'''

    print("\n\n\n--------- Interceptor Project                    ---------")
    print("--------- Versão 1.0.0                           ---------")
    print("--------- Autor: DRP01-PJI310-SALA-002GRUPO-014  ---------")
    print("--------- Data: 2025-05-20                       ---------")
    print("--------- Inicializando Programa                 ---------\n")

    # Exemplo e teste de uso de enum
    #print(f"Status Enum Value: {Status.entrada.value}")
    
    # [ ] TODO: Capturar imagens da câmera

    # [ ] TODO: Extração de strings de imagens
    #placa_veiculo = cv2.imread(os.path.join('src', 'resources', 'placa_veiculo.jpg'))
    placa_veiculo = 'AAA-0A00'
    
    # [x] TODO: Coletar data e hora do sistema
    today = GeradorDataHora.gerador_data_hora()

    # [x] TODO: Criar um dict [objeto JSON]  com a strings extraídas
    objeto_registro['placa'] = placa_veiculo                # Valor da placa do veículo extraído do vídeo - STRING
    objeto_registro['data_hora'] = today                    # Data e hora do extraído do sistema - STRING
    objeto_registro['evento'] = Status.entrada.value        # Status de entrada e saída - INT
    
    print(objeto_registro)
    print(type(objeto_registro))

    # [x] TODO: Enviar o dict [objeto JSON] para API com: PLACA, DATA_HORA, STATUS
    # url_post = parameters.Parametros.url_api_golang.value
    # result = CallApiEndpoint.post_request(url_post, objeto_registro)

    # if result.status_code == 200:
    #     print("Requisição enviada com sucesso!")
    # else:
    #     print(f"Erro ao enviar requisição: {result.status_code}")


    print("\n--------- Finalizando Programa                   ---------\n\n\n")

if __name__ == "__main__":
    main()
