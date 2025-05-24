from datetime import datetime, timezone

class GeradorDataHora:
    '''Classe para gerar data e hora '''

    def gerador_data_hora():
        '''Função para gerar data e hora atual. Formato ISO 8601 -> 2025-04-05T23:39:04.085Z '''

        # today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")       # Gera data e hora atual ja formatado
        # today = datetime.datetime.strptime(today, "%Y-%m-%d %H:%M:%S")      # Converte string em datetime
        today = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')

        return today
