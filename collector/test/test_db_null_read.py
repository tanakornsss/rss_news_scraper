from collector.database import Database

db = Database()

articles = db.get_articles(limit=5)

assert isinstance(articles, list)
print(articles)