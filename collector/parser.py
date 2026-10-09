from bs4 import BeautifulSoup

from collector.database import Database


def parse(response: str):
    soup = BeautifulSoup(response, 'lxml-xml')
    news_list = soup.find_all("item")

    print(f"Found {len(news_list)} news\n")

    db = Database("test.db")

    for index, news in enumerate(news_list):
        title = news.find("title").text.strip()
        url = news.find("link").text.strip()
        pub_date = news.find("pubDate").text.strip()
        source = news.find("source").get("url")

        print(f"Title: {title}")
        print(f"Link: {url}")
        print(f"Published on: {pub_date}")
        print(f"Source: {source}")
        print("*" * 40)