"""Help with a specific command"""


def command_help(command: str):
    """Help with using a specific command"""
    if command == 'get':
        print("Help with the Get Command")
    elif command == 'set':
        print("Help with the Set Command")
    elif command == 'keys':
        print("Help with the Keys Command")
    elif command in ('del', 'delete'):
        print("Help with the Delete Command")
    else:
        print("Unknown Command: " + command)
