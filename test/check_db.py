import sqlite3
from config import DB_PATH

with sqlite3.connect(DB_PATH) as conn:
    count = conn.execute(
        "SELECT COUNT(*) FROM articles"
    ).fetchone()[0]

    print("Total articles:", count)

    rows = conn.execute("""
        SELECT id, title, pub_date, scraped_date, source
        FROM articles
        ORDER BY id DESC
        LIMIT 5
    """).fetchall()

    for row in rows:
        print(row)