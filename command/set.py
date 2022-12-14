""" The Set Command """

from pyperclip import paste

from program_io.files import data_file
from program_io.validate import keys


def run(args: list) -> bool:
    """Initializes the Set Command

    Validates Arguments, executes the Set Command
    If Key is invalid, Prints Invalid Key Message
    Returns true if the Set Command Succeeded
    """
    if len(args) < 1:
        print("Set Command Requires Key")
        return False
    key = str(args[0])
    # Validate Key
    if not keys.is_valid(key):
        return False
    # Perform Set Operation
    return _cmd_set(key)


def _cmd_set(key: str) -> bool:
    """Performs the Set operation on a Valid Key."""
    # Get From the Clipboard
    clip_content = str(paste())
    # Validate Clipboard Content
    if len(clip_content) == 0:
        print("Nothing Found On Clipboard")
        return False
    # Load Existing Data
    data = data_file.load()
    # Save Clip using Key
    data[key] = clip_content
    # Save the Data File
    data_file.save(data)
    # Task Completion Message
    print("Copied From Clipboard To Key (" + key + ")")
    return True
