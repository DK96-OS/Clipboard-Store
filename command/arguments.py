""" Process Command Line Arguments """


def getArguments() -> list:
    """
    Get the Arguments for this run
    If there are no arguments, returns None
    """
    import sys
    arguments = sys.argv[1:]
    # Must have at least one Argument
    if len(arguments) < 1: return None
    # The Command is the first argument
    return arguments


def processArguments(args: list) -> bool:
    """
    Process the Command Arguments provided
    """
    if args == None:
        print("Missing Command")
        return False
    # Command is the first Argument
    command = args[0].lower()

    # Identify the Command
    if command == "set":
        from command import set
        return set.run(args[1:])
    
    elif command == "get":
        from command import get
        return get.run(args[1:])
    
    elif command == "keys":
        from command import keys
        return keys.run(args[1:])
    
    elif command in ("del", "delete"):
        from command import delete
        return delete.run(args[1:])
    
    # No Command was run
    print("Invalid Command :" + command)
    return False
