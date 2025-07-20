# web_scraper.py

import requests
from bs4 import BeautifulSoup
from typing import List

# Headers for scraping
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}

class Website:
    url: str
    title: str
    body: bytes
    links: List[str]
    text: str

    def __init__(self, url: str):
        self.url = url
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except Exception as e:
            self.title = "No title"
            self.text = f"Error fetching {url}: {e}"
            self.links = []
            return

        self.body = response.content
        soup = BeautifulSoup(self.body, "html.parser")
        self.title = soup.title.string if soup.title else "No title found"

        if soup.body:
            for tag in soup.body(["script", "style", "img", "input"]):
                tag.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""

        raw_links = [link.get("href") for link in soup.find_all("a")]
        self.links = [link for link in raw_links if link]

    def get_content(self):
        return f"Website Title:\n{self.title}\n\nWebsite Content:\n{self.text}"
