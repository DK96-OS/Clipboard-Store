""" The Set Command """


def run(args: list) -> bool:
    """
    Validates Arguments, executes the Set Command
    Args must start with the Set Command's Key
    If Key is invalid, Prints Invalid Key Message
    """
    if len(args) < 1:
        print("Set Command Requires Key")
        return False
    key = str(args[0])
    # Validate Key
    from program_io.validate import keys
    if not keys.isValid(key):
        return False
    # Perform Set Operation
    return _cmd_set(key)


def _cmd_set(key: str) -> bool:
    """
    Performs the Set operation on a Valid Key
    """
    # Get From the Clipboard
    from pyperclip import paste
    clip_content = str(paste())
    # Validate Clipboard Content
    if len(clip_content) == 0:
        print("Nothing Found On Clipboard")
        return False
    # Load Existing Data
    from program_io.files import data_file
    data = data_file.load()
    # Save Clip using Key
    data[key] = clip_content
    # Save the Data File
    data_file.save(data)
    # Task Completion Message
    print("Copied From Clipboard To Key (" + key + ")")
    return True
