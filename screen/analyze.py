from analysis.tfidf import find_similar_articles
from collector.database import Database

def analyze():
    db = Database()

    articles = db.get_articles()
    pairs = find_similar_articles(
        articles=articles,
        threshold=0.2,
        top_k=100
    )

    for score, article_a, article_b in pairs[:10]:
        print(f"Article A: {article_a["title"]}")
        print(f"Article B: {article_b["title"]}")
        print(f"Similarity: {score: .3f}")
        print("-" * 40)