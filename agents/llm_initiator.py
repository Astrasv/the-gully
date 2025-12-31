from langchain_groq import ChatGroq
from agents.config import AgentsConfig

class LLMInitiator:
    def __init__(self):
        
        self.config = AgentsConfig()
        
        self.llm = ChatGroq(
            model = self.config.model,
            temperature = self.config.temperature,
            max_tokens = self.config.max_tokens,
            reasoning_format = self.config.reasoning_format,
            timeout = self.config.timeout,
            max_retries = self.config.max_retries,
            api_key=self.config.groq_api_key
        )
