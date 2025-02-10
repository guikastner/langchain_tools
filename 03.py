import os
import authorization
from langchain.agents import Tool
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_python_agent
from langchain_experimental.utilities import PythonREPL

os.environ['OPENAI_API_KEY'] = authorization.apikey

model = ChatOpenAI(model="gpt-3.5-turbo")

python_repl = PythonREPL()

python_repl_tool = Tool(
    name="Python REPL",
    description="Um shell python. Use para executar comandos criados pela IA."
    "Para visualizar os cálculos faça um Print(...).",
    func=python_repl.run,
)

agent_executor = create_python_agent(
    llm=model,
    tool=python_repl_tool,
    verbose=True
)

prompt_template = PromptTemplate(
    input_variables=["numero1", "numero2"],
    template='''
    Faça uma operação de somas com os números {numero1} e {numero2}
    imprima o código python usado no processo no ecrã
    '''
)

numero1 = 10
numero2 = 20

prompt = prompt_template.format(numero1=numero1, numero2=numero2)

result = agent_executor.invoke(prompt)

print(result.get("output"))
