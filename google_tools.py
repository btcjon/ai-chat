from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import httpx

# Load .env file
load_dotenv()

# Get Google Search API and Google Custom Web Search keys from .env file
google_search_api_key = os.getenv('GOOGLE_SEARCH_API_KEY')
google_cse_id = os.getenv('GOOGLE_CSE_ID')

if not google_search_api_key or not google_cse_id:
    raise ValueError("Google API keys not found in .env file")

async def google_search(query):
    """
    This function performs an internet search using Google Search. It can be triggered by queries such as:
    - "search the web for {query}"
    - "find {query} on the internet"
    - "google this: {query}"
    """

    service = build("customsearch", "v1", developerKey=google_search_api_key)
    res = await service.cse().list(q=query, cx=google_cse_id).execute()
    results = [item['title'] for item in res['items']]
    return {"context": ", ".join(results), "titles": results}

async def google_custom_search(query):
    """Perform a custom web search using Google Custom Web Search."""
    service = build("customsearch", "v1", developerKey=google_search_api_key)
    res = await service.cse().list(q=query, cx=google_cse_id).execute()
    results = [item['snippet'] for item in res['items']]
    return {"context": ", ".join(results)}
