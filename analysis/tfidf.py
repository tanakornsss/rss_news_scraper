from itertools import combinations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from analysis.text_cleaning import sanitize_text
from collector.database import Database

def find_similar_articles(limit: int = 100):
    db = Database()
    articles = db.get_articles(limit=limit)

    articles = [
        article for article in articles
        if article.get("title", "").strip()
    ]

    if len(articles) < 2:
        print("Need at least 2 articles")
        return

    titles = [sanitize_text(article["title"]) for article in articles]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(titles)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    pairs = []

    for i, j in combinations(range(len(articles)), 2):
        score = similarity_matrix[i, j]

        pairs.append((
            score,
            articles[i],
            articles[j]
        ))

    pairs.sort(key=lambda item: item[0], reverse=True)

    for score, article_a, article_b in pairs[:10]:
        print(f"Similarity: {score:.3f}")
        print(f"A: {article_a['title']}")
        print(f"B: {article_b['title']}")
        print("-" * 60)

if __name__ == "__main__":
    find_similar_articles()