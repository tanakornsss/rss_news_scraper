from analysis.text_cleaning import sanitize_text
from collector.database import Database

db = Database()

articles = db.get_articles()

for article in articles:
    title = article["title"]

    print(f"Original: {title}")
    print(f"Sanitized: {sanitize_text(title)}")
    print("-" * 40)
