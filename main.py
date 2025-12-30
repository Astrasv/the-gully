
from db.config import DatabaseConfig
from db.populate import DatabasePopulator
from db.preprocess.preprocess import DataPreprocessor


"""
Only data preprocessing and storing as CSV is done
TODO: Populate in postgres

THIS IS NOT A DATA PREPROCESSING PROJECT
OTHERS IDEAS WILL BE IMPLEMENTED SOON
"""


def main():
    
    # JSON to CSV
    data_prep = DataPreprocessor("ipl_json")
    data_prep.flatten_all_matches()

    # CSV to Postgres
    db_params = DatabaseConfig().as_dict()
    db = DatabasePopulator(db_params, "ipl_data.csv")
    db.upload_csv_to_postgres()

if __name__ == "__main__":
    main()
