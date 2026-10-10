import sqlite3

with sqlite3.connect("../test.db") as conn:
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