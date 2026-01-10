
from db.config import DatabaseConfig
from db.populate import DatabasePopulator
from db.preprocess.preprocess import DataPreprocessor

from agents.sql_agent import SQLAgent

def main():
    
    #  Preprocessing
    # # JSON to CSV
    # data_prep = DataPreprocessor("ipl_json")
    # data_prep.flatten_all_matches()

    # # CSV to Postgres
    # db_params = DatabaseConfig().as_dict()
    # db = DatabasePopulator(db_params, "ipl_data.csv")
    # db.upload_csv_to_postgres()


    agent = SQLAgent()
    question = input("[THE-GULLY] Ask me any IPL related question: ")
    response = agent.invoke_agent(question)
    print(f"[THE-GULLY] Here is what we can conclude: {response}")


if __name__ == "__main__":
    main()