""" Package of Help related Content """

from help.commands import command_help
from help.general import general_help


def run_help(args: list):
    """Run the Help Command based on the arguments provided"""
    if 0 == len(args):
        # For no additional arguments, show general help
        general_help()
    else:
        # Show Help for the first argument, if it is a valid command
        command_help(command=args[0].lower())
