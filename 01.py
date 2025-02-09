from langchain_community.tools import DuckDuckGoSearchRun

ddg_search = DuckDuckGoSearchRun()

search_results = ddg_search.run("Guilherme Kastner Dassault Systemes")

print(search_results)