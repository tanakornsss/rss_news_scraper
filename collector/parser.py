from datetime import datetime, timezone
from bs4 import BeautifulSoup
from collector.database import Database


def parse(response: str) -> int:
    soup = BeautifulSoup(response, 'lxml-xml')
    news_list = soup.find_all("item")

    print(f"Found {len(news_list)} news\n")

    db = Database("test.db")
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
            "pub_date": pub_date,
            "scraped_date": datetime.now(timezone.utc).isoformat(),
            "source": source
        }
        db_list.append(item)

    # Returns news that was written
    inserted = db.write_to_db(db_list)

    print(f"Parsed: {len(db_list)}")
    print(f"Inserted: {inserted}")
    print(f"Skipped or already stored: {len(db_list) - inserted}")

    return inserted
