from db.config import DatabaseConfig
from utils.clean_list_string import clean_list_string

import pandas as pd
import psycopg2

import numpy as np
from psycopg2.extras import execute_values
import utils.columns as cols


class DatabasePopulator:
    def __init__(self, db_params, csv_file_path):
        self.db_params = db_params
        self.csv_file_path = csv_file_path

    def clean_rows(self, df):
        print("Preprocessing rows for database...")
        values = []
        for row in df.to_numpy():
            clean_row = []
            for x in row:
                if x is None:
                    clean_row.append(None)
                elif isinstance(x, (list, np.ndarray)):
                    clean_row.append(x)
                elif pd.isna(x) or str(x).lower() == "nan":
                    clean_row.append(None)
                else:
                    clean_row.append(x)

            values.append(tuple(clean_row))

        return values

    def upload_csv_to_postgres(self):
        print(f"Loading {self.csv_file_path}...")

        df = pd.read_csv(self.csv_file_path, dtype=str, low_memory=False)

        # Convert list-like strings into actual Python lists for Postgres Array types
        list_columns = ["dates", "player_of_match", "wicket_fielders", "season"]
        for col in list_columns:
            df[col] = df[col].apply(clean_list_string)

        conn = None
        try:

            conn = psycopg2.connect(**self.db_params)
            cur = conn.cursor()

            columns = cols.columns

            values = self.clean_rows(df)

            # Prepare Template with Casts
            placeholders = ["%s"] * len(columns)
            placeholders[2] = "%s::DATE[]"  # 'dates'
            placeholders[4] = "%s::INTEGER[]"  # 'season'
            placeholders[13] = "%s::TEXT[]"  # 'player_of_match'
            placeholders[33] = "%s::TEXT[]"  # 'wicket_fielders'

            template = "(" + ",".join(placeholders) + ")"
            query = f"INSERT INTO ipl_ball_by_ball ({','.join(columns)}) VALUES %s"

            print(f"Uploading {len(values)} rows to Postgres...")
            execute_values(cur, query, values, template=template)

            conn.commit()
            print("Successfully uploaded all data.")

        except Exception as e:
            print(f"Error: {e}")
            if conn:
                conn.rollback()
        finally:
            if conn:
                cur.close()
                conn.close()


if __name__ == "__main__":
    db_params = DatabaseConfig().as_dict()
    db = DatabasePopulator(db_params, "ipl_data.csv")
    db.upload_csv_to_postgres()
