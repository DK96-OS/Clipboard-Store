# File Management Operations and Configuration
import json

# The path of the Data File
file_path = "./user_data/data.json"

# Load from the Data File
def load() -> dict:
    """ Read a Dictionary from the Data File
    Note: Numerical keys are loaded as strings
    """
    try:
        # Open the File
        with open(file_path) as file:
            # Assume JSON
            return json.load(file)
    except:
        # Default Empty List
        return {}

# Save the Data File
def save(data: dict) -> None:
    """ Write this Dictionary to the Data File
    Note: Will overwrite any existing data
    """
    # Overwrite the Data File
    with open(file_path, 'w') as file:
        # Use JSON
        json.dump(data, file)
    