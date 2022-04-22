""" The Keys Command """


def run(args: list) -> bool:
    """
    Performs the Keys Command
    No arguments are required, or used at this time
    """
    # Load from Data File
    from program_io.files import data_file
    # Only the Keys are required
    data_keys = data_file.load().keys()
    # Count the Number of Keys
    key_count = len(data_keys)
    # Check if there are no Keys
    if key_count == 0:
        print("No Keys Found")
        return False
    #
    _print_keys(data_keys)
    # Print the key count at the end
    print("\n\tTotal Key Count : " + str(key_count))
    return True


def _print_keys(keys: list):
    """
    Prints a List of Keys
    Applies a Filter on Keys starting with underscore
    """
    for key in keys:
        # Do not show keys starting with underscore
        if not str.startswith(key, '_'):
            print(key)
