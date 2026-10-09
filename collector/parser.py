from datetime import datetime, timezone
from bs4 import BeautifulSoup
from collector.database import Database


def parse(response: str):
    soup = BeautifulSoup(response, 'lxml-xml')
    news_list = soup.find_all("item")

    print(f"Found {len(news_list)} news\n")

    db = Database("test.db")

    db_list = []
    for index, news in enumerate(news_list):
        title = news.find("title").text.strip()
        url = news.find("link").text.strip()
        pub_date = news.find("pubDate").text.strip()
        source = news.find("source").get("url")

        news = {
            "title": title,
            "url": url,
            "pub_date": pub_date,
            "scraped_date": str(datetime.now(timezone.utc)),
            "source": source
        }
        db_list.append(news)

        print(f"Title: {title}")
        print(f"Link: {url}")
        print(f"Published on: {pub_date}")
        print(f"Source: {source}")
        print("*" * 40)

    db.write_to_db(db_list)