import os
import authorization
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = authorization.apikey

model = ChatOpenAI(model="gpt-3.5-turbo")

wikipedia_tool = WikipediaQueryRun(
    api_wrapper = WikipediaAPIWrapper(
        #lang="pt"
    )
)

agent_executor = create_python_agent(
    llm=model,
    tool=wikipedia_tool,
    verbose=True
)

prompt_template = PromptTemplate(
    input_variables=["query"],
    template='''
    Pesquise na web sobre {query} e resuma sobre o assunto
    Responda tudo em português brasileiro
    '''
)

query = "Solidworks"

prompt = prompt_template.format(query=query)

result = agent_executor.invoke(prompt)

print(result.get("output"))
