import json
import requests
import streamlit as st
from typing import List
from bs4 import BeautifulSoup
from openai import OpenAI
from Brochure_generator_pro.requirments.API_KEY import openai_api_key # secret Key 

# Initialize OpenAI client
client = OpenAI(api_key=openai_api_key)

# Simple check for API key
if openai_api_key and openai_api_key.startswith("sk-proj-"):
    print("API key looks very good")
else:
    print("There might be a problem with the API key")

# Headers for scraping
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}

# Website scraper class
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
            st.error(f"Error fetching {url}: {e}")
            self.title = "No title"
            self.text = ""
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


# Model to use
MODEL = "gpt-4o-mini"

# Prompt to instruct the model to create a brochure
system_prompt = (
    "You are an assistant that analyzes the contents of a company website "
    "and creates a short brochure about the company for prospective customers, investors, and recruits. "
    "Respond in markdown. Include details of company culture, customers, and careers/jobs if you have the information."
)

# Build user prompt with website content
def get_brochure_user_prompt(company_name, url):
    website = Website(url)
    prompt = (
        f"You are looking at a company called: {company_name}\n"
        f"Here is the content of its landing page; use this information to build a short brochure of the company in markdown.\n"
        f"{website.get_content()}"
    )
    # Truncate to avoid huge payloads
    return prompt[:15000]

# Stream brochure chunks to Streamlit
def stream_brochure_streamlit(company_name, url):
    stream = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": get_brochure_user_prompt(company_name, url)}
        ],
        stream=True,
    )

    container = st.empty()
    collected_text = ""
    for chunk in stream:
        delta = chunk.choices[0].delta
        content = delta.content or ""
        collected_text += content
        container.markdown(collected_text)
    return collected_text
