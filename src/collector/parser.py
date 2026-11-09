from datetime import datetime, timezone
from bs4 import BeautifulSoup
from src.collector.database import Database
from src.collector.hash import generate_hash
from src.analysis.text_cleaning import sanitize_text


def parse(response: str):
    soup = BeautifulSoup(response, 'lxml-xml')
    news_list = soup.find_all("item")

    db = Database()
    db_list = []

    for news in news_list:
        title_tag = news.find("title")
        url_tag = news.find("link")
        pub_date_tag = news.find("pubDate")
        source_tag = news.find("source")

        if title_tag is None or url_tag is None:
            continue

        title = title_tag.get_text(strip=True)
        url = url_tag.get_text(strip=True)

        pub_date = (
            pub_date_tag.get_text(strip=True)
            if pub_date_tag else None
        )

        source = (
            source_tag.get("url") or source_tag.get_text(strip=True)
            if source_tag else "unknown"
        )

        item = {
            "title": title,
            "url": url,
            "content_hash": generate_hash(sanitize_text(title)),
            "pub_date": pub_date,
            "scraped_date": datetime.now(timezone.utc).isoformat(),
            "source": source
        }
        db_list.append(item)

    # Returns news that was written
    inserted = db.write_articles(db_list)

    return len(news_list), len(db_list), inserted
