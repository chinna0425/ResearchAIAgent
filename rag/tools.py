import json
import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()
from tavily import TavilyClient


class HybridRetriever:

    def __init__(self, vector_store):
        self.vector_store = vector_store

        tavily_api_key = os.getenv("TAVILY_API_KEY")

        self.tavily = TavilyClient(api_key=tavily_api_key)

    def search_pdf(self, query, k=3):

        docs = self.vector_store.similarity_search(
            query=query,
            k=k,
        )

        context = ""

        for doc in docs:

            page = doc.metadata.get("page", "Unknown")

            context += f"\n[Page {page}]\n"

            context += doc.page_content

            context += "\n"

        return context, docs

    def search_web(self, query):

        response = self.tavily.search(
            query=query,
            search_depth="advanced",
            max_results=3,
        )

        results = response.get("results", [])

        web_context = ""

        for result in results:

            web_context += f"""
Title: {result.get('title')}

Content:
{result.get('content')}

URL:
{result.get('url')}

"""

        return web_context