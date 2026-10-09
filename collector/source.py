import requests
from collector.parser import parse

def find_from_keyword(keyword: str):
    url = "https://news.google.com/rss"

    # Extra parameters
    query_params = {
        "q": keyword,
        "hl": "en-US",   # language
        "gl": "US",      # location
        "ceid": "US:en"  # country edition ID
    }

    print("Please wait...")
    response = requests.get(url, params=query_params)

    if response.status_code == 200:
        parse(response.text)
    else:
        print("Failed to connect")