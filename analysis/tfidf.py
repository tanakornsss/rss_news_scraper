from itertools import combinations
from pythainlp import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from analysis.text_cleaning import sanitize_text

def find_similar_articles(
    articles: list[dict],
    is_thai: bool = False,
    top_k: int = 20,
    threshold: float = 0.5
) -> list[dict]:

    # Collect articles which has title in it
    articles = [
        article for article in articles
        if article.get("title", "").strip()
    ]

    # Sanitize text
    titles = [sanitize_text(article["title"]) for article in articles]

    vectorizer = TfidfVectorizer()
    vectorizer_th = TfidfVectorizer(
        tokenizer=thai_tokenizer,
        token_pattern=None,
        lowercase=False
    )

    if is_thai:
        tfidf_matrix = vectorizer_th.fit_transform(titles)
    else:
        tfidf_matrix = vectorizer.fit_transform(titles)

    similarity_matrix = cosine_similarity(tfidf_matrix)

    pairs = []

    # Pick a combination of news titles and access the score vector in similarity matrix
    for i, j in combinations(range(len(articles)), 2):
        score = similarity_matrix[i, j]

        if score > threshold:
            pairs.append((
                score,
                articles[i],
                articles[j]
            ))

    pairs.sort(key=lambda item: item[0], reverse=True)

    # Tail splice
    return pairs[:top_k]

def thai_tokenizer(text: str):
    return word_tokenize(text, engine="newmm")
