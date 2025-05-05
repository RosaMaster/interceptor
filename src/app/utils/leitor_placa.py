import cv2
import pytesseract
import os

# Certifique-se de ter o Tesseract OCR instalado e configurado no seu sistema.
# Você pode precisar especificar o caminho para o executável do Tesseract.
# Exemplo:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_texto_placa_video(video_path, output_file="placas_detectadas.txt", frame_interval=30):
    """
    Lê um vídeo MP4, extrai texto de possíveis placas de carro em intervalos de frames
    e armazena os resultados em um arquivo de texto.

    Args:
        video_path (str): O caminho para o arquivo de vídeo MP4.
        output_file (str): O nome do arquivo de texto para armazenar as placas detectadas.
        frame_interval (int): O intervalo em frames para processar (ex: processar a cada 30 frames).
    """
    if not os.path.exists(video_path):
        print(f"Erro: O arquivo de vídeo '{video_path}' não foi encontrado.")
        return

    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Erro: Não foi possível abrir o vídeo '{video_path}'.")
            return

        frame_count = 0
        placas_detectadas = set()  # Usar um conjunto para evitar duplicatas

        with open(output_file, "w") as f:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break  # Fim do vídeo

                if frame_count % frame_interval == 0:
                    # Converter o frame para escala de cinza para melhor detecção de texto
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Aplicar algum pré-processamento para melhorar a leitura do texto (opcional)
                    # Exemplo: binarização, filtro de ruído
                    # thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
                    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)

                    # Usar o Tesseract para extrair texto da imagem
                    texto = pytesseract.image_to_string(gray, lang='por', config='--psm 8') # 'por' para português, psm 8 para placa

                    # Filtrar o texto extraído para identificar possíveis placas (heurística básica)
                    possiveis_placas = [t.strip() for t in texto.split('\n') if len(t.strip()) >= 7 and any(c.isalnum() for c in t)]

                    for placa in possiveis_placas:
                        placas_detectadas.add(placa)

                frame_count += 1

            if placas_detectadas:
                f.write("Placas de carro possivelmente detectadas:\n")
                for placa in sorted(list(placas_detectadas)):
                    f.write(placa + "\n")
                print(f"Texto de possíveis placas de carro extraído e armazenado em '{output_file}'.")
            else:
                print("Nenhuma placa de carro possivelmente detectada no vídeo.")

        cap.release()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    video_arquivo = "seu_video.mp4"  # Substitua pelo caminho do seu arquivo de vídeo
    extrair_texto_placa_video(video_arquivo)