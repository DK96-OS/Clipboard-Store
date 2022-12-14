""" File Management Operations and Configuration. """

import json
from os.path import realpath
from pathlib import Path


def get_file_path():
    """
    The path of the Data File.
    The goal is to be independent of working directory
    """
    # The path of this File
    abs_path: Path = Path(realpath(__file__))
    # Go to the Root of the Cliper Project
    project_root: Path = abs_path.parent.parent.parent
    # Locate the Data File in the Project
    file_path = "user_data/data.json"
    # Combine Project Path with Data File Path
    return project_root.joinpath(file_path)


def load() -> dict:
    """
    Read a Dictionary from the Data File
    Note: Numerical keys are loaded as strings
    """
    try:
        # Open the File
        with open(get_file_path()) as file:
            # Assume JSON
            return json.load(file)
    except:
        # Default Empty List
        return {}


def save(data: dict) -> None:
    """
    Write this Dictionary to the Data File
    Note: Will overwrite any existing data
    """
    # Overwrite the Data File
    with open(get_file_path(), 'w') as file:
        # Use JSON
        json.dump(data, file)
    