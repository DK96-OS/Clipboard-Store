#!/usr/bin/env python3
# Clipboard Data Management

# Get the Arguments for this run
def getArguments() -> str:
    import sys
    arguments = sys.argv[1:]
    # Must have at least one Argument
    if len(arguments) < 1: return None
    # The Command is the first argument
    return arguments

arguments = getArguments()
# Command is the first Argument
command = arguments[0].lower()

# When Command has a Key, it is 2nd argument
def getKey() -> str:
    # Expect 2nd Argument to be key name
    clip_key = arguments[1]
    # Ensure Key is valid
    if clip_key == None or len(clip_key) < 1:
        raise ValueError("Key not found for Command")
    elif len(clip_key) > 1000:
        raise ValueError("The Key is too long")
    return clip_key

# Process the command
if command is None:
    print("Invalid Command")

# Set Command inserts clip into Data File
elif command == "set":
    # Get the Key Argument
    key = getKey()
    # Get From the Clipboard
    import pyperclip
    clip_content = pyperclip.paste()
    # Validate Clipboard Content
    if len(clip_content) == 0:
        print("Nothing Found On Clipboard")
    else:
        # Load Existing Data
        from fileio import load, save
        data = load()
        # Save Clip using Key
        data[key] = str(clip_content)
        # Save the Data File
        save(data)
        # Task Completion Message
        print("Copied From Clipboard To Key (" + key + ")")

# Get Command returns clipped value from the Data File
elif command == "get":
    # Get the Key Argument
    key = getKey()
    # Load any existing data
    from fileio import load
    data = load()
    # Check if Key is valid
    if key in data:
        # Obtain Value of Key
        value = data[key]
        try:
            import pyperclip
            pyperclip.copy(str(value))
            print("Copied To Clipboard (" + key + ")")
        except:
            print("Could Not Copy To Clipboard")
    else:
        print("Key Not Found (" + key + ")")

# Keys Command prints all keys
elif command == "keys":
    # Load from Data File
    from fileio import load
    data = load()
    # Get all Keys
    data_keys = data.keys()
    # Count the Number of Keys
    key_count = len(data_keys)
    # Check if there are no Keys
    if key_count == 0:
        print("There are no Keys stored")
    else:
        # New Line First
        print()
        for key in data_keys:
            # Do not show keys starting with underscore
            if not str.startswith(key, '_'):
                print(key)
        # Print the key count at the end
        print("\n\tTotal Key Count : " + str(key_count) + "\n")

# Unknown Command
else:
    raise ValueError("Unknown Command Received :" + command)
