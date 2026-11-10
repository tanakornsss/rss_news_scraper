import sqlite3
from contextlib import closing
from src.config.setting import CONFIG
from root_dir import BASE_DIR

class Database:

    # Database init code, will only create tables if one does not exist
    def __init__(self):
        name = CONFIG["DATABASE"]["name"]

        self.db_name = str(BASE_DIR/name)
        self._create_article_table()
        self._create_summary_table()

    def _get_connection(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        return connection

    def _create_article_table(self) -> None:
        with closing(self._get_connection()) as connection:
            with connection:
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS articles 
                    (
                        article_id   INTEGER PRIMARY KEY,
                        
                        title        TEXT NOT NULL,
                        url          TEXT NOT NULL UNIQUE,
                        
                        content_hash TEXT,
                        
                        pub_date     TEXT,
                        scraped_date TEXT NOT NULL,
                        source       TEXT NOT NULL
                    )
                    """
                )

    def _create_summary_table(self) -> None:
        with closing(self._get_connection()) as connection:
            with connection:
                connection.execute(
                    """
                    CREATE TABLE IF NOT EXISTS summary
                    (
                        summary_id   INTEGER PRIMARY KEY,
                        article_id   INTEGER,
                        
                        pair_id      INTEGER[],
                        similarity   FLOAT[],
                        cluster_id   INTEGER,

                        title        TEXT NOT NULL,
                        url          TEXT NOT NULL UNIQUE,

                        content_hash TEXT,

                        pub_date     TEXT,
                        scraped_date TEXT NOT NULL,
                        source       TEXT NOT NULL,
                        
                        FOREIGN KEY (article_id) REFERENCES articles(article_id)
                    )
                    """
                )

    def write_articles(self, news: list[dict]) -> int:
        # Will return 0 news if data sent was not type of news
        if not news:
            return 0

        rows = [
            (
                item["title"],
                item["url"],
                item["content_hash"],
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
                        (title, url, content_hash, pub_date, scraped_date, source)
                    VALUES (?, ?, ?, ?, ?, ?)
                    ON CONFLICT(url) DO NOTHING
                    """,
                    rows
                )
            return cursor.rowcount

    def get_articles(self, limit: int = 20) -> list[dict]:
        with closing(self._get_connection()) as connection:
            rows = connection.execute(
                """
                SELECT title, url, content_hash, pub_date, scraped_date, source
                FROM articles
                ORDER BY scraped_date DESC
                LIMIT ?
                """,
                (limit,)
            ).fetchall()

            return [dict(row) for row in rows]

    def search_articles(self, keyword: str) -> list[dict]:
        keyword = keyword.strip()

        if not keyword:
            return []

        with closing(self._get_connection()) as connection:
            rows = connection.execute(
                """
                SELECT title, url, content_hash, pub_date, scraped_date, source 
                FROM articles
                WHERE title LIKE ?
                ORDER BY scraped_date DESC
                """,
                (f"%{keyword}%",)
            ).fetchall()

            return [dict(row) for row in rows]

    def write_summary(self, summary: list[dict]) -> int:

        if not summary:
            return 0

        rows = [
            (
                item["pair_id"],
                item["similarity"],
                item["cluster_id"],

                item["title"],
                item["url"],

                item["content_hash"],

                item.get("pub_date"),  # Null handling
                item["scraped_date"],
                item["source"]
            )
            for item in summary
        ]

        with closing(self._get_connection()) as connection:
            with connection:
                cursor = connection.executemany(
                    """
                    INSERT INTO summary
                        (pair_id, similarity, cluster_id, title, url, content_hash, pub_date, scraped_date, source)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(url) DO NOTHING
                    """,
                    rows
                )
            return cursor.rowcount
