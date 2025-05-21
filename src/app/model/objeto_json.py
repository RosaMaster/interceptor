import json

class CreateObjeto:
    """ Classe que cria um objeto JSON para armazenar informações de placa de veículo, data e status. """

    def __init__(self, board: str, date: str, event: int, company_id: str, token: str):
        """ Construtor da classe ObjetoJson.
        Args:
            board (str): Placa do veículo.
            date (str): Data e hora do evento.
            event (int): Status do evento (entrada ou saída).
        """

        self.board = board
        self.date = date
        self.event = event
        self.company_id = company_id
        self.token = token


    def to_dict(self):
        """ Converte o objeto em um dicionário.
        Returns:
            dict: Dicionário com os atributos do objeto.
        """

        return {
            "board": self.board,
            "date": self.date,
            "event": self.event,
            "company_id": self.company_id,
            "token": self.token
        }
    

    def to_json(self):
        """ Converte o objeto em uma string JSON.
        Returns:
            str: String JSON com os atributos do objeto.
        """

        return json.dumps(self.to_dict(), indent=4)


    @classmethod
    def from_dict(cls, data):
        """ Cria um objeto a partir de um dicionário.
        Args:
            data (dict): Dicionário com os dados do objeto.
        Returns:
            ObjetoJson: Instância da classe ObjetoJson.
        """

        return cls(
            board=data.get("board"),
            date=data.get("date"),
            event=data.get("event"),
            company_id=data.get("company_id"),
            token=data.get("token")
        )
    

    # Converte o objeto em uma string JSON
    def to_json(self):
        """ Converte o objeto em uma string JSON.
        Returns:
            str: String JSON com os atributos do objeto.
        """

        return json.dumps(self.to_dict(), indent=4)
