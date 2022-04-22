# File Management Operations and Configuration
import json

# The path of the Data File
file_path = "cliper_data.json"

# Load from the Data File
def load() -> dict:
    try:
        # Open the File
        with open(file_path) as file:
            # Assume JSON
            return json.load(file)
    except:
        # Default Empty List
        return {}

# Save the Data File
def save(data):
    # Overwrite the Data File
    with open(file_path, 'w') as file:
        # Use JSON
        json.dump(data, file)
    