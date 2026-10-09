import sqlite3
from contextlib import closing

class Database:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.create_tables()

    def _get_connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        return connection

    def create_tables(self) -> None:
        with closing(self._get_connection()) as connection:
            with connection:
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS articles (
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        url TEXT NOT NULL UNIQUE,
                        pub_date TEXT,
                        scraped_date TEXT NOT NULL,
                        source TEXT NOT NULL
                    )
                    """
                )

