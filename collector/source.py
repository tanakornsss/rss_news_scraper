import requests
from collector.parser import parse

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
        parse(response.text)
    else:
        print("Failed to connect")