import sqlite3
from datetime import datetime

placas_vistas = {}  # Dicionário para armazenar últimas placas detectadas e tempos

class DatabaseConexao:
    """  Classe para gerenciar a conexão com o banco de dados SQLite LOCAL. """

    def __init__(self, db_path='placas.db'):
        """ Inicializa a conexão com o banco de dados.
        Args:
            db_path (str): Caminho para o arquivo do banco de dados SQLite.
        """

        self.conn = sqlite3.connect(db_path)        # Conecta ao banco de dados SQLite
        self.cursor = self.conn.cursor()            # Cria um cursor para executar comandos SQL
        # Cria a tabela de registros se não existir
        self.execute('''CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            placa TEXT,
            data_hora TEXT,
            status INTEGER)''')
        self.conn.commit()                          # Confirma as alterações no banco de dados


    def salvar_no_banco(self, placa, status):
        """ Salva os dados no banco de dados local.
        Args:
            placa (str): Placa do veículo.
            status (int): Status do evento (entrada ou saída).
        """

        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')    # Coleta a data e hora atual

        # Filtrar placas repetidas em menos de 5 minutos (300 segundos)
        if placa in placas_vistas:
            tempo_passado = (datetime.now() - placas_vistas[placa]).seconds
            
            # Ignorar placas repetidas antes de 5 min
            if tempo_passado < 300:
                return  
        
        # Atualiza o dicionário com a nova data e hora
        self.cursor.execute("INSERT INTO registros (placa, data_hora, status) VALUES (?, ?, ?)",(placa, data_hora, status))
        self.conn.commit()      # Confirma as alterações no banco de dados
        self.conn.close()       # Fecha a conexão com o banco de dados
