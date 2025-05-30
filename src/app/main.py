import os
from model.objeto_json import CreateObjeto
from utils.gerador_data_hora import GeradorDataHora
from utils.info_sistema import InfoSistemaInterceptor
from service.resquest import CallApiEndpoint
from service.database import DatabaseConexao
from settings.parameters import Parametros
import random
import json
import cv2
import pytesseract

def main():
    '''Função principal do programa'''

    # [x] TODO: Cabecalho do programa
    print(InfoSistemaInterceptor.cabecacho)         # Início do programa -> Informações do sistema

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'     # Caminho do executável do Tesseract OCR

    # [x] TODO: Coletar data e hora do sistema
    today = GeradorDataHora.gerador_data_hora()     # Data e hora atual do sistema format: 2025-04-05T23:39:04.085Z

    # [x] TODO: Capturar imagens da câmera
    if Parametros.feature_toggle_object.value == False:
        caminho_video = os.path.join(os.path.dirname(__file__), 'video', 'video_entrada_carro.mp4')  # Caminho do vídeo 
        cap = cv2.VideoCapture(caminho_video)       # Troque '0' pelo caminho do vídeo

        placa_anterior_x = None                     # Para rastrear a posição da placa

    else:
        print("Simulação de vídeo")


    #while True:
    for i in range(2):
        if Parametros.feature_toggle_object.value == False:
            ret, frame = cap.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     # Converte para escala de cinza

            # Aplica OCR com Tesseract
            placa_detectada = pytesseract.image_to_string(gray, config='--psm 8')

            # Lógica de aproximação/afastamento baseada na posição X da placa
            x_atual = cap.get(cv2.CAP_PROP_POS_FRAMES)  # Simulação de posição da placa
        else:
            placa_detectada = random.choice(Parametros.placa_teste.value)  # Simulação de placas para teste
            print("Simulação extração de placa")

        print(f'Placa detectada: {placa_detectada}')

        if Parametros.feature_toggle_database.value == False:
            if placa_anterior_x is not None:
                status = 1 if x_atual > placa_anterior_x else 0
                DatabaseConexao.salvar_no_banco(placa_detectada.strip(), status)
        else:
            print("Simulação de salvamento no banco de dados")

        # [x] TODO: Criar um dict [objeto JSON]  com a strings extraídas
        if Parametros.feature_toggle_object.value == False:
            objeto_json = CreateObjeto(
                placa_detectada,                 # Valor da placa do veículo extraído do vídeo - STRING
                today,                           # Data e hora do extraído do sistema - STRING
                status,                          # Status de entrada e saída - INTEGER
                Parametros.company_id.value,     # ID da empresa - STRING
                CallApiEndpoint.get_token()      # Token de autenticação - STRING
            )

        else:
            objeto_json = CreateObjeto(
                placa_detectada,                                # Valor da placa do veículo extraído TESTE
                today,                                          # Data e hora do extraído do sistema TESTE
                random.choice(Parametros.status_teste.value),   # Status TESTE
                Parametros.company_id.value,                    # ID da empresa TESTE
                Parametros.token_teste.value                    # Token TESTE
            )

            print("Simulação criação objeto JSON")

        # objeto_json = objeto_json.to_dict()   # Converte o objeto em dicionário
        objeto_json = objeto_json.to_json()     # Converte o objeto em JSON

        print(objeto_json)

        # [x] TODO: Enviar o dict [objeto JSON] para API com: PLACA, DATA_HORA, STATUS
        if Parametros.feature_toggle_call_api.value == False:

            url = Parametros.url_api_golang.value

            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }

            result = CallApiEndpoint.post_request(url, objeto_json, headers)

            if result.status_code == 200:
                print("Requisição enviada com sucesso!")
            else:
                print(f"Erro ao enviar requisição: {result.status_code}")

            placa_anterior_x = x_atual          # Atualiza posição da placa

            cv2.imshow('Detecção de Placas', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            cap.release()
            cv2.destroyAllWindows()
        
        else:
            json_path = 'data/objeto_json.json'
            try:
                with open(json_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = []
            data.append(json.loads(objeto_json))  # objeto_json é string JSON, converte para dict
            with open(json_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)

            print("Objeto JSON salvo em data/objeto_json.json")

    # [x] TODO: Rodapé do programa
    print(InfoSistemaInterceptor.rodape)        # Fim do programa

if __name__ == "__main__":
    main()
