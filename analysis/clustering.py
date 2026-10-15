from collections import defaultdict
from sklearn.cluster import KMeans
from analysis import tfidf
from analysis.text_cleaning import sanitize_text

def clustering(
    articles: list[dict],
    n_clusters: int = 2,
    random_state: int = 42,
    n_init: int = 10
) -> list[tuple]:

    articles = [
        article for article in articles
        if article.get("title").strip()
    ]

    titles = [sanitize_text(article["title"]) for article in articles]

    vectorizer = tfidf.TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(titles)

    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=n_init
    )

    labels = model.fit_predict(tfidf_matrix)

    clusters = defaultdict(list)

    for title, label in zip(titles, labels):
        clusters[label].append(title)

    return sorted(clusters.items())