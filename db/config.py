import os
from dotenv import load_dotenv

class DatabaseConfig:
    def __init__(self):
        load_dotenv()
        self.host = "localhost"
        self.database = "ipl_database"
        self.user = os.getenv("database_username")
        self.password = os.getenv("database_password")

        if not all([self.user, self.password]):
            raise ValueError("Database credentials not set in environment variables")

    def as_dict(self):
        return vars(self)
