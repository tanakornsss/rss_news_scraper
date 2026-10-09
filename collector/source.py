import requests
from collector.parser import parse

def find_from_keyword(keyword: str) -> int:
    url = "https://news.google.com/rss"

    # Extra parameters
    query_params = {
        "q": keyword,
        "hl": "en-US",   # language
        "gl": "US",      # location
        "ceid": "US:en"  # country edition ID
    }

    print("Please wait...")

    try:
        response = requests.get(
            url,
            params=query_params,
            timeout=15
        )
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Failed to fetch RSS: {error}")
        return 0

    inserted = parse(response.text)
    return inserted