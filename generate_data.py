import json
from datetime import datetime

def time_json(filename:str):
    # Get the current time
    current_time = datetime.now().isoformat()

    # Data to write into the JSON file
    data = {"current_time": current_time}

    # Write the data to a JSON file
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Current time written to {filename}: {current_time}")