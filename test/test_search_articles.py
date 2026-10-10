from collector.database import Database

db = Database()

keyword = str(input("Enter search keyword: "))
articles = db.search_articles(keyword)

print(f"Found {len(articles)} articles\n")

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Source: {article['source']}")
    print(f"URL: {article['url']}")
    print("-" * 40)