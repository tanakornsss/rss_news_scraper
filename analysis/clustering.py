from collections import defaultdict

from sklearn.cluster import KMeans
from analysis import tfidf
from analysis.text_cleaning import sanitize_text
from collector.database import Database

db = Database()
articles = db.get_articles(limit=100)

titles = [sanitize_text(article["title"]) for article in articles]

vectorizer = tfidf.TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(titles)

model = KMeans(
    n_clusters=2,
    random_state=42,
    n_init=10
)

labels = model.fit_predict(tfidf_matrix)

clusters = defaultdict(list)

for title, label in zip(titles, labels):
    clusters[label].append(title)

for cluster_id, cluster_titles in sorted(clusters.items()):
    print(f"\n=== Cluster {cluster_id} ===")

    for title in cluster_titles:
        print(f"- {title}")