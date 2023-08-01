import os
import httpx
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get Browserless API key from .env file
browserless_api_key = os.getenv('BROWSERLESS_API_KEY')

if not browserless_api_key:
    raise ValueError("BROWSERLESS_API_KEY not found in .env file")

def scrape_website(url: str) -> str:
    """Scrape a website using the Browserless API."""
    BROWSERLESS_API_URL = "https://chrome.browserless.io/content"
    headers = {"Authorization": f"Bearer {browserless_api_key}"}
    json = {"url": url, "waitForSelector": ".mw-parser-output"}
    response = httpx.post(BROWSERLESS_API_URL, headers=headers, json=json)
    return {"context": response.text}
