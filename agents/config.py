import os
from dotenv import load_dotenv

class AgentsConfig:
    def __init__(self):
        load_dotenv()
        
        # Environment Variable
        self.groq_api_key = os.getenv("groq_api_key")
        self.database_url = os.getenv("database_url")

        # LLM Configurations
        self.model="qwen/qwen3-32b"
        self.temperature=0
        self.max_tokens=None
        self.reasoning_format="parsed"
        self.timeout=None
        self.max_retries=2
    




    def as_dict(self):
        return vars(self)
