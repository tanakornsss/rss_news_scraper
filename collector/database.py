import sqlite3
from contextlib import closing
from config import DB_PATH

class Database:

    # Database init code, will only create tables if one does not exist
    def __init__(self):
        self.db_name = str(DB_PATH)
        self._create_tables()

    def _get_connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        return connection

    def _create_tables(self) -> None:
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

    def write_to_db(self, news: list[dict]) -> int:
        # Will return 0 news if data sent was not type of news
        if not news:
            return 0

        rows = [
            (
                item["title"],
                item["url"],
                item.get("pub_date"), # Null handling
                item["scraped_date"],
                item["source"]
            )
            for item in news
        ]

        with closing(self._get_connection()) as connection:
            with connection:
                cursor = connection.executemany(
                    """
                    INSERT INTO articles
                        (title, url, pub_date, scraped_date, source)
                    VALUES (?, ?, ?, ?, ?)
                    ON CONFLICT(url) DO NOTHING
                    """,
                    rows
                )
            return cursor.rowcount

    def get_articles(self, limit: int = 20) -> list[dict]:
        with closing(self._get_connection()) as connection:
            rows = connection.execute(
                """
                SELECT id, title, url, pub_date, scraped_date, source
                FROM articles
                ORDER BY scraped_date DESC
                LIMIT ?
                """,
                (limit,)
            ).fetchall()

            return [dict(row) for row in rows]
