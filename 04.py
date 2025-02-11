import os
import authorization
from langchain import hub
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain_community.utilities import SerpAPIWrapper
from langchain_experimental.utilities import PythonREPL
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

os.environ['OPENAI_API_KEY'] = authorization.apikey
os.environ['SERPAPI_API_KEY'] = authorization.searchkey

model = ChatOpenAI(model="gpt-3.5-turbo")

prompt = '''
Como um assistente pessoal, que responderá a dicas financeiras e de investimento.
Responda tudo em português do brasil
Perguntas: {q}
'''

promtp_template = PromptTemplate.from_template(prompt)

python_repl = PythonREPL()

python_repl_tool = Tool(
    name="Python REPL",
    description="Um shell python. Use para executar comandos criados pela IA."
    "Para visualizar os cálculos faça um Print(...)."
    "Use essa ferramenta para criar e executar cálculos financeiros e responder perguntas de investimento.",
    func=python_repl.run,
)

search = SerpAPIWrapper()
search_tool = Tool(
    name="busca Google",
    description="útil para pesquisar sobre economia e investimentos"
        "você sempre deve pesquisar melhores dicas de investimento na internet"
        "não responda diretamente, mas sua resposta deve conter apenas dados relacionados de investimento pesquisados a serem processados depois",
    func=search.run,
)


react_instructions = hub.pull ('hwchase17/react')

tools = [python_repl_tool, search_tool]

print(react_instructions)

agent = create_react_agent(
    llm=model,
    tools=tools,
    prompt=react_instructions
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)

question = "ganho R$25.000 ao mês, gasto 3k de aluguel. tenho 20k em despesas mensais, como seria atrativo investir e os retornos para 2025?"

output = agent_executor.invoke(
    {'input': promtp_template.format(q=question)}        
)

print(output.get("output"))