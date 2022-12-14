""" Process Command Line Arguments """

import sys


def get_arguments() -> list:
    """
    Get the Arguments for this run
    If there are no arguments, returns None
    """
    arguments = sys.argv[1:]
    # Must have at least one Argument
    if len(arguments) < 1:
        return None
    # The Command is the first argument
    return arguments


def process_arguments(args: list) -> bool:
    """
    Process the Command Arguments provided
    """
    if args is None:
        print("Missing Command")
        return False
    # Command is the first Argument
    command = args[0].lower()
    # Identify the Command
    if command == "set":
        from command import set
        return set.run(args[1:])
    #
    if command == "get":
        from command import get
        return get.run(args[1:])
    #
    if command == "keys":
        from command import keys
        return keys.run(args[1:])
    #
    if command in ("del", "delete"):
        from command import delete
        return delete.run(args[1:])
    #
    if command in ("help", "--help"):
        from help import run_help
        return run_help(args[1:])
    # No Command was run
    print("Invalid Command :" + command)
    return False
