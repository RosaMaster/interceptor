

class ObjetoJson:
    """ Classe que cria um objeto JSON para armazenar informações de placa de veículo, data e status. """

    def __init__(self, board: str, date: str, event: int):
        """ Construtor da classe ObjetoJson.
        Args:
            board (str): Placa do veículo.
            date (str): Data e hora do evento.
            event (int): Status do evento (entrada ou saída).
        """

        self.board = board
        self.date = date
        self.event = event


    def to_dict(self):
        """ Converte o objeto em um dicionário.
        Returns:
            dict: Dicionário com os atributos do objeto.
        """

        return {
            "board": self.board,
            "nome": self.nome,
            "valor": self.valor
        }


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
            nome=data.get("nome"),
            valor=data.get("valor")
        )
