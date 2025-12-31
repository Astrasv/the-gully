from agents.llm_initiator import LLMInitiator


from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from agents.config import AgentsConfig

from agents.system_prompts.sql_agent_prompt import sql_agent_system_prompt
import os

class SQLAgent:
    def __init__(self):
        self.config = AgentsConfig()
        self.llm_init = LLMInitiator()
        self.db = SQLDatabase.from_uri(self.config.database_url)

        self.toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm_init.llm)

        self.agent = create_sql_agent(
            llm=self.llm_init.llm,
            toolkit=self.toolkit,
            verbose=True, # see thinking steps
            agent_type="openai-tools",      
            prefix=sql_agent_system_prompt
        )

    
    def invoke_agent(self, question):
        response = self.agent.invoke({"input": question})

        return response["output"]

    