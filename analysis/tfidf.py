from itertools import combinations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from analysis.text_cleaning import sanitize_text

def find_similar_articles(
    articles: list[dict],
    top_k: int = 20,
    threshold: float = 0.5
) -> list[dict]:

    articles = [
        article for article in articles
        if article.get("title", "").strip()
    ]

    titles = [sanitize_text(article["title"]) for article in articles]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(titles)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    pairs = []

    for i, j in combinations(range(len(articles)), 2):
        score = similarity_matrix[i, j]

        if score > threshold:
            pairs.append((
                score,
                articles[i],
                articles[j]
            ))

    pairs.sort(key=lambda item: item[0], reverse=True)

    return pairs[:top_k]
