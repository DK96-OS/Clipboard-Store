# File Management Operations and Configuration


def getFilePath():
    """
    The path of the Data File.
    The goal is to be independent of working directory
    """
    from os.path import realpath
    from pathlib import Path
    # The path of this File
    absPath: Path = Path(realpath(__file__))
    # Go to the Root of the Cliper Project
    project_root: Path = absPath.parent.parent.parent
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
        with open(getFilePath()) as file:
            # Assume JSON
            import json
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
    with open(getFilePath(), 'w') as file:
        # Use JSON
        import json
        json.dump(data, file)
    