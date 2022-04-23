""" The Delete Command """


def run(args: list) -> bool:
    """
    Validates Delete Command Arguments
    Initiates Delete Command Operation
    Returns True if a Key was deleted
    """
    # Ensure that args is not empty
    if len(args) < 1:
        return False
    # Each Argument is a Key to be deleted
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
    # 
    if data_updated:
        # Save the updated Data File
        data_file.save(data)
        return True
    # If no Keys were deleted
    return False


def _cmd_del(data: dict, key: str) -> bool:
    """
    Performs the Delete Command Operation
    Returns True if the Key was deleted
    """
    # Check if Key exists
    if key in data:
        del data[key]
        # Key Deleted, notify caller
        return True
    # Key did not exist, no changes
    return False
