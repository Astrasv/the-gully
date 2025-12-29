import json

def file_to_json(match_file):
    with open(match_file, 'r') as f:
        json_data = json.load(f)
    return json_data