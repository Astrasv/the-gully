
from db.preprocess import DataPreprocessor


"""
Only data preprocessing and storing as CSV is done
TODO: Populate in postgres

THIS IS NOT A DATA PREPROCESSING PROJECT
OTHERS IDEAS WILL BE IMPLEMENTED SOON
"""


def main():
    print("Hello")
    data_prep = DataPreprocessor("ipl_json")
    data_prep.flatten_all_matches()

if __name__ == "__main__":
    main()
