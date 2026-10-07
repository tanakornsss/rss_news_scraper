import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.google.com/rss")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml-xml')
    news_list = soup.find_all("item")

    print(f"Found {len(news_list)} news\n")

    for news in news_list:
        title = news.find("title").text
        link = news.find("link").text
        pub_date = news.find("pubDate").text
        source = news.find("source").get("url")

        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Published on: {pub_date}")
        print(f"Source: {source}")
        print("*" * 40)
else:
    print("Server unreachable")
