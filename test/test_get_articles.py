from collector.database import Database

db = Database()

articles = db.get_articles(limit=5)

print(f"Found {len(articles)} articles\n")

for article in articles:
    print(f"ID: {article['id']}")
    print(f"Title: {article['title']}")
    print(f"URL: {article['url']}")
    print(f"Published: {article['pub_date']}")
    print(f"Scraped: {article['scraped_date']}")
    print(f"Source: {article['source']}")
    print("-" * 40)