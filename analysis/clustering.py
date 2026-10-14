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

for title, label in zip(titles, labels):
    print(f"Cluster {label}: {title}")