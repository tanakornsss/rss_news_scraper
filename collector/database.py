import sqlite3

class Database:

    def __init__(self, db_name: str):
        self.db_name = db_name

    def _get_connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        return connection

