from src.analysis.clustering import clustering
from src.analysis.tfidf import find_similar_articles
from src.collector.database import Database
from src.config.setting import CONFIG


def analyze():
    db = Database()

    articles = db.get_articles()

    if len(articles) < 1:
        print("No data found")
        return

    lang = CONFIG.get("REGION", "hl")

    supported_lang = ["en-US", "th-TH"]

    if lang not in supported_lang:
        print("Unsupported language")
        return

    is_thai = lang is supported_lang[1]

    pairs = find_similar_articles(
        articles=articles,
        threshold=CONFIG.getfloat("SIMILARITY", "threshold"),
        top_k=CONFIG.getint("SIMILARITY", "top_k"),
        is_thai=is_thai
    )

    clusterings = clustering(
        articles=articles,
        n_clusters=CONFIG.getint("CLUSTERINGS", "n_clusters"),
        random_state=CONFIG.getint("CLUSTERINGS", "random_state"),
        n_init=CONFIG.getint("CLUSTERINGS", "n_init")
    )

    print_summary(pairs, clusterings)

def print_summary(pairs: list[dict], clusterings: list[tuple]):
    print(("=" * 40) + " SIMILARITY " + ("=" * 40))
    for score, article_a, article_b in pairs:
        print(f"Article A: {article_a["title"]}")
        print(f"Article B: {article_b["title"]}")
        print(f"Similarity: {score: .3f}")
        print("-" * 40)

    print(("=" * 40) + " CLUSTERING " + ("=" * 40))
    for label, titles in clusterings:
        print(f"Cluster {label}")

        for title in titles:
            print(f"Title: {title}")