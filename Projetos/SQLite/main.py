
class Database():

    def __init__(self) -> None:
        # Biblioteca
        import sqlite3
        from pathlib import Path

        # PATH
        ROOT_DIR = Path(__file__).parent
        self.DB_NAME = 'db.sqlite3'
        DB_FILE = ROOT_DIR / self.DB_NAME
        self.TABLE_NAME = 'customers'

        # Connection
        self.connection = sqlite3.connect(DB_FILE)
        self.cursor = self.connection.cursor()

        # SQL
        self.cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {self.TABLE_NAME}'
            '('
            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'name TEXT,'
            'weight REAL'
            ')'
        )

        # Registrar valores nas colunas da tabela
        self.sql = (
            f'INSERT INTO {self.TABLE_NAME}'
            '(name, weight)'
            'VALUES'
            '(?, ?)'
        )

    def insert(self, *args, **kwargs):
        self.cursor.executemany(self.sql, *args, **kwargs)
        self.connection.commit()
        print(self.sql)
        self.cursor.close()
        self.connection.close()

    def select(self, comando):
        # all - visualizar todos
        import pandas as pd
        self.connection.cursor()
        comando = comando.upper()
        if comando == 'ALL':
            self.cursor.execute(f'SELECT * FROM {self.TABLE_NAME}')

        elif 'SELECT' not in (comando):
            raise Exception('Exemplo: SELECT * FROM {TABLE_NAME}')

        else:
            self.cursor.execute(comando)

        valor = []
        print(f'Database: {self.DB_NAME} - Table: {self.TABLE_NAME}')
        for row in self.cursor.fetchall():
            valor.append(
                {'ID': row[0], 'NAME': row[1], 'WEIGHT': row[2]})

        tab = pd.DataFrame(valor)
        print(tab)

        self.cursor.close()
        self.connection.close()

    def delete(self, comando):
        comando = comando.upper()
        if 'WHERE' not in comando:
            while True:
                confirmacao = input(
                    'Faltou especificar WHERE! \nIrá deletar todos os dados!\n\
                        Deseja continuar? \nSIM ou NAO').upper()
                if confirmacao == 'NAO':
                    print('CANCELADO!')
                    self.cursor.close()
                    self.connection.close()
                    return
                elif confirmacao == 'SIM':
                    break
        self.cursor.execute(comando)
        self.connection.commit()
        print('DELETADO!')
        self.cursor.close()
        self.connection.close()

    def update(self, comando):
        self.cursor.execute(comando)
        self.connection.commit()
        print('UPDATE')
        self.cursor.close()
        self.connection.close()


class Control_database():
    def __init__(self):
        database = Database()
        self.TABLE_NAME = database.TABLE_NAME

    def insert(self, *args, **kwargs):
        Database().insert(*args, **kwargs)

    def select(self, *args, **kwargs):
        Database().select(*args, **kwargs)

    def delete(self, *args, **kwargs):
        Database().delete(*args, **kwargs)

    def update(self, *args, **kwargs):
        Database().update(*args, **kwargs)
