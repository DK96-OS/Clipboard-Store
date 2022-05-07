""" Package of Help related Content """


def run_help(args: list):
    """Run the Help Command based on the arguments provided"""
    if 0 == len(args):
        # For no additional arguments, show general help
        from help.general import general_help
        general_help()
    else:
        # Show Help for the first argument, if it is a valid command
        from help.commands import command_help
        command_help(command=args[0].lower())
