from langchain_community.tools import DuckDuckGoSearchRun
from duckduckgo_search import DDGS


with DDGS() as ddgs:
    results = [r for r in ddgs.text("Guilherme Kastner Dassault Systèmes", max_results=5)]

print(results)

