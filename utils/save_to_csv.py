import csv

def save_to_csv(rows, filename="ipl_data.csv"):
        if not rows:
            print("No data to write.")
            return

        headers = rows[0].keys()

        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=headers, restval='')
                writer.writeheader()
                writer.writerows(rows)
            print(f"Successfully saved {len(rows)} rows to {filename}")
        except IOError as e:
            print(f"Error writing to CSV: {e}")