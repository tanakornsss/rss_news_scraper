import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.google.com/rss")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml-xml')
    news = soup.find_all("item")

    print(f"Found {len(news)} news")
else:
    print("Server unreachable")
