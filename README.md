<!-- HEADER -->
<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=211C84&height=140&section=header" alt="header"/>


<!-- TITLE -->
<div align="center">
  <h1 align="center" alt="title">

  I  N  T  E  R  C  E  P  T  O  R

  </h1>
</div>

### Objetivo

Sistema responsável por realizar o monitoramento e extração da placa do veículo de entrada e saída de veículos do estacionamento, realizando request **POST** via api, para inserção dos dados no banco de dados **SQL**.

Esse sistema foi desenvolvido em linguagem python, versão **Python 3.12.2**


### Documentação e links úteis

<details><summary><b>Mostrar links</b></summary>

| **LINKS**                                                                   | **TIPO**     |
| --------------------------------------------------------------------------- | ------------ |
| [python.org](https://www.python.org/)                                       | `DOC`        |
| [opencv-python](https://pypi.org/project/opencv-python/)                    | `LIB`        | 
| [OpenCV Tutorial](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) | `DOC`        |
| [mediapipe](https://pypi.org/project/mediapipe/)                            | `LIB`        | 
| [pytesseract](https://pypi.org/project/pytesseract/)                        | `LIB`        | 
| [datetime](https://docs.python.org/3/library/datetime.html)                 | `LIB`        | 
| [json](https://www.w3schools.com/python/python_json.asp)                    | `LIB`        | 
| [requests](https://pypi.org/project/requests/)                              | `LIB`        | 
| [enum](https://docs.python.org/3/library/enum.html)                         | `LIB`        | 
| [github](https://docs.github.com/pt)                                        | `DOC`        |
| [observer-pi3](https://github.com/mediapraise/observer-pi3)                 | `REPOSITORY` |

</details>

<br>

### Metodologia

1. **Importar Bibliotecas Essenciais**

| **LIB's**   | **Descição**                                                                   |
| ----------- | ------------------------------------------------------------------------------ |
| OpenCV      | Usada para processamento de imagem, detecção de objetos e manipulação de vídeo |
| PyTesseract | Interface para o Tesseract OCR, um mecanismo de reconhecimento de caracteres   |
| datetime    | O módulo datetime fornece classes para manipular datas e horas                 |

<br>

2. **Fluxo de Trabalho**

> Captura texto da Imagem
- Iremos capturar a imagem da placa usando uma câmera conectada ao computador, a lib OpenCV será utilizada ideal para essa etapa.

> Pré-processamento da Imagem
- O pré-processamento melhora a qualidade da imagem para o OCR. Como: Conversão para escala de cinza, Ajuste de brilho e contraste, Remoção de ruído e Binarização (conversão para preto e branco).

> Detecção da Placa
- Usando o OpenCV, você pode detectar a região da placa na imagem. Isso pode envolver o uso de algoritmos de detecção de contornos ou classificadores pré-treinados.

> Reconhecimento de Caracteres (OCR)
- O PyTesseract extrai o texto da região da placa detectada.

> Armazenamento dos Dados
Use a biblioteca datetime para obter a data e hora atuais.
Salve a informação da placa, data e hora em um arquivo de texto ou banco de dados.

<br>

3. **Exemplo de Código**

<details><summary>Mostrar exemplo de utilização</summary>

~~~Python
import cv2
import pytesseract
from datetime import datetime
import os


# Caminho para o executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capturar_placa(caminho_imagem):
    # Ler a imagem
    imagem = cv2.imread(caminho_imagem)

    # Pré-processamento (exemplo básico)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Reconhecimento de caracteres
    texto_placa = pytesseract.image_to_string(imagem_cinza)

    # Limpar o texto (remover caracteres indesejados)
    texto_placa = ''.join(filter(str.isalnum, texto_placa))

    # Obter data e hora atuais
    agora = datetime.now()
    data_hora = agora.strftime("%Y-%m-%d %H:%M:%S")

    # Salvar os dados em um arquivo
    nome_arquivo = "placas_capturadas.txt"
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(f"Placa: {texto_placa}, Data/Hora: {data_hora}\n")

    print(f"Placa: {texto_placa}, Data/Hora: {data_hora}")

# Exemplo de uso
capturar_placa("caminho/para/sua/imagem.jpg")
~~~

</details>

<br>

4. **Informações**

- A precisão do reconhecimento de placas depende da qualidade da imagem, iluminação e outros fatores.<br>
- O pré-processamento adequado é crucial para obter bons resultados com o OCR.<br>
