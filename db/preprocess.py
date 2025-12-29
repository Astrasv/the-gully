import json
import psycopg2
from psycopg2 import extras
from db.ball_logics import BallLogics
import os
from utils.file_to_json import file_to_json
from utils.save_to_csv import save_to_csv


class DataPreprocessor:
    def __init__(self, data_path):
        self.data_path = data_path
        self.rows = []

    def flatten_match(self, data):
        info = data.get("info", {})
        logics = BallLogics(info, data)

        # Iterate through innings
        for innings_idx, innings in enumerate(data.get("innings", [])):
            batting_team = innings.get("team")

            # Iterate through overs
            for over_data in innings.get("overs", []):
                current_ball = 0
                over_num = over_data.get("over")

                # Iterate through deliveries
                for delivery in over_data.get("deliveries", []):

                    review = delivery.get("review", {})

                    # Handle extras and reball
                    extras = delivery.get("extras", {})
                    is_rebowl = "wides" in extras or "noballs" in extras
                    current_ball += 1
                    ball = current_ball
                    if is_rebowl: current_ball -= 1

                    # Combine all data into one flat dictionary
                    row = {
                        **logics.match_meta(),
                        "innings_val": innings_idx + 1,
                        "batting_team": batting_team,
                        "over": over_num,
                        "ball": ball,
                        **logics.handle_ball_details(delivery),
                        **logics.handle_extras(delivery),
                        **logics.handle_wickets(delivery),
                        **logics.handle_reviews(review),
                        **logics.handle_replacements(delivery),
                    }
                    self.rows.append(row)
            

    def flatten_all_matches(self):
        num = 1
        for match_file in os.listdir(self.data_path):
            match_file = os.path.join(self.data_path, match_file)
            data = file_to_json(match_file)
            self.flatten_match(data)
            print(f"Match {num} populated ")
            num += 1
        save_to_csv(self.rows)


if __name__ == "__main__":
    data_prep = DataPreprocessor("ipl_json")
    data_prep.flatten_all_matches()
    
