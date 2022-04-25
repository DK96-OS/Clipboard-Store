""" The Delete Command """


def run(args: list) -> bool:
    """Initiate the Delete Command.

    Validates that Arguments are valid keys
    Returns True if a Key was deleted
    """
    # Ensure that args is not empty
    if len(args) < 1:
        return False
    # Load Data File once
    from program_io.files import data_file
    data = data_file.load()
    # Data needs to be saved only if a Key is deleted
    data_updated = False
    #
    for key in args:
        # Check if the Delete Operation succeeds
        if _cmd_del(data, key):
            data_updated = True
            print("Successfully Deleted Key (" + key + ")")
        else:
            print("Could not Delete Key (" + key + ")")
    # 
    if data_updated:
        # Save the updated Data File
        data_file.save(data)
        return True
    # If no Keys were deleted
    return False


def _cmd_del(data: dict, key: str) -> bool:
    """Performs the Delete Operation on a single Key

    Returns True if the Key was deleted
    """
    # Validate Key
    from program_io.validate import keys
    if not keys.isValid(key):
        return False
    # Check if Key exists
    if key not in data:
        return False
    # Delete Key
    del data[key]
    return True
