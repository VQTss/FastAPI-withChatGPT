from langchain import OpenAI
# from langchain.agents import create_pandas_dataframe_agent # now langchain has been removed
import pandas as pd
import os
from langchain.agents.agent import AgentExecutor
from langchain_experimental.agents import create_pandas_dataframe_agent # new version
API_KEY = os.environ.get('API_KEY')

print(f"API key {API_KEY}")

def create_agent(filename: str) -> AgentExecutor:
    # Create an OpenAI object.
    llm = OpenAI(openai_api_key=API_KEY, temperature=0)

    # Read the CSV file into a Pandas DataFrame.
    df = pd.read_csv(filename)

    # Create a Pandas DataFrame agent.
    return create_pandas_dataframe_agent(llm, df, verbose=False)


def query_agent(agent: AgentExecutor, query: str) -> str:
    # Run the prompt through the agent.
    response = agent.run(query)

    # Convert the response to a string.
    return response