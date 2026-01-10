from fastapi import FastAPI
from agents.sql_agent import SQLAgent

# Self-documenting metadata
app = FastAPI(
    title="SQL Agent API",
    description="An AI-powered API that translates natural language to SQL queries.",
    version="1.0.1",
    docs_url="/docs",  # You can even rename the docs URL here
    redoc_url="/redoc"
)

# Initialize agent globally for performance
agent = SQLAgent()

@app.get("/health", tags=["System"])
async def health_check():
    """Check if the API and SQL Agent are operational."""
    return {"status": "healthy", "version": "1.0.0"}

@app.get("/agents/query", tags=["AI Agent"])
async def run_query(query: str):
    """
    Submit a natural language query to the SQL Agent.
    - **query**: The question you want to ask the database.
    """
    response = agent.invoke_agent(query)
    return {"response": response}