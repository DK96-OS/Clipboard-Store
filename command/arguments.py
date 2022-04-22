

def getArguments() -> str:
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


def processArguments(args: list):
    """
    Process the Command Arguments provided
    """
    if args == None:
        print("Missing Command")
        return
    # Otherwise, Command is the first Argument
    command = args[0].lower()
    # Identify the Command
    if command == "set":
        from command.set import run
        run(args[1:])
    elif command == "get":
        from command.get import run
        run(args[1:])
    elif command == "keys":
        from command.keys import run
        run(args[1:])
    else:
        print("Invalid Command :" + command)
