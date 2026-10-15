from analysis.clustering import clustering
from analysis.tfidf import find_similar_articles
from collector.database import Database
from config.setting import CONFIG


def analyze():
    db = Database()

    articles = db.get_articles()

    if len(articles) < 1:
        print("No data found")
        return

    pairs = find_similar_articles(
        articles=articles,
        threshold=CONFIG.getfloat("SIMILARITY", "threshold"),
        top_k=CONFIG.getint("SIMILARITY", "top_k")
    )

    clusterings = clustering(articles)

    print(("=" * 40) + " SIMILARITY " + ("=" * 40))
    for score, article_a, article_b in pairs[:10]:
        print(f"Article A: {article_a["title"]}")
        print(f"Article B: {article_b["title"]}")
        print(f"Similarity: {score: .3f}")
        print("-" * 40)

    print(("=" * 40) + " CLUSTERING " + ("=" * 40))
    for label, titles in clusterings:
        print(f"Cluster {label}")

        for title in titles:
            print(f"Title: {title}")
