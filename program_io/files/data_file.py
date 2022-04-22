# File Management Operations and Configuration

# The path of the Data File
import os.path
file_path = os.path.abspath("user_data/data.json")


def getPath():
    from os.path import abspath
    abspath("user_data/data.json")


def load() -> dict:
    """ Read a Dictionary from the Data File
    Note: Numerical keys are loaded as strings
    """
    try:
        # Open the File
        with open(file_path) as file:
            # Assume JSON
            import json
            return json.load(file)
    except:
        # Default Empty List
        return {}


def save(data: dict) -> None:
    """ Write this Dictionary to the Data File
    Note: Will overwrite any existing data
    """
    # Overwrite the Data File
    with open(file_path, 'w') as file:
        # Use JSON
        import json
        json.dump(data, file)
    