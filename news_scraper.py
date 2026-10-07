from datetime import datetime, timezone
import json
import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.google.com/rss")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml-xml')
    news_list = soup.find_all("item")

    print(f"Found {len(news_list)} news\n")

    json_item_lists = []

    for index, news in enumerate(news_list):
        title = news.find("title").text.strip()
        url = news.find("link").text.strip()
        pub_date = news.find("pubDate").text.strip()
        source = news.find("source").get("url")

        item = {
            "id": index + 1,
            "title": title,
            "url": url,
            "pub_date": pub_date,
            "scraped_date": str(datetime.now(timezone.utc)),
            "source": source
        }
        json_item_lists.append(item)

        print(f"Title: {title}")
        print(f"Link: {url}")
        print(f"Published on: {pub_date}")
        print(f"Source: {source}")
        print("*" * 40)

    date_time = datetime.now(timezone.utc).strftime("%d%m%Y_%H%M%S")
    fname = f"scrape_{date_time}.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(json_item_lists, f, ensure_ascii=False, indent=4)
else:
    print("Server unreachable")
