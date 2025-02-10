from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia = WikipediaQueryRun(
    api_wrapper = WikipediaAPIWrapper(
        #lang="pt"
    )
)




wikipedia_results = wikipedia.run("Solidworks")
print(wikipedia_results)





