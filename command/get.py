""" The Get Command """


def run(args: list) -> bool:
    """
    Validates Arguments, executes the Get Command
    Args must start with the Get Command's Key
    """
    if len(args) < 1:
        print("Get Command Requires Key")
        return False
    key = str(args[0])
    # Validate Key
    from program_io.validate import keys
    if not keys.isValid(key):
        return False
    # Perform Get Operation
    return _cmd_get(key)


def _cmd_get(key: str) -> bool:
    """
    Performs the Get Command on a Valid Key.
    The Key may not exist, in which case a message is printed
    """
    # Load any existing data
    from program_io.files import data_file
    data = data_file.load()
    # Check if Key is valid
    if key in data:
        # Obtain Value of Key
        value = str(data[key])
        try:
            import pyperclip
            pyperclip.copy(value)
            print("Copied To Clipboard (" + key + ")")
            return True
        except:
            print("Could Not Copy To Clipboard")
            return False
    else:
        print("Key Not Found (" + key + ")")
        return False
