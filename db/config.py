import os
from dotenv import load_dotenv

class DatabaseConfig:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv("POSTGRES_SERVER")
        self.database = os.getenv("POSTGRES_DB")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")

        if not all([self.user, self.password]):
            raise ValueError("Database credentials not set in environment variables")

    def as_dict(self):
        return vars(self)
