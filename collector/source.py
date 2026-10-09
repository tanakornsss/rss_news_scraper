import requests
from bs4 import BeautifulSoup

def find_from_keyword(keyword: str):
    url = "https://news.google.com/rss"
    query_params = {
        "q": keyword,
        "hl": "en-US",
        "gl": "US",
        "ceid": "US:en"
    }

    print("Please wait...")
    response = requests.get(url, params=query_params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml-xml')
        news_list = soup.find_all("item")

        print(news_list)
    else:
        print("Failed to connect")