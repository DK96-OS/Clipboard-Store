#!/usr/bin/env python3
# Clipboard Data Management
import pyperclip
import json
import sys

# The path of the Data File
file_path = "clipper_data.json"

# Valid number of Command Line Arguments
# The lowest number of arguments for a valid command is 2.
if len(sys.argv) < 2:
    raise ValueError("Argument not found")

# Get the command
command = sys.argv[1].lower()

# Obtain the Key from the command line arguments
def get_clip_key() -> str:
    # Expect 2nd Argument to be key name
    clip_key = sys.argv[2]
    # Ensure Key is valid
    if clip_key == None or len(clip_key) < 1:
        raise ValueError("Key not found for Command")
    elif len(clip_key) > 1000:
        raise ValueError("The Key is too long")
    return clip_key

# Load from the Data File
def load() -> dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except:
        return {}

# Save the Data File
def save(data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

# Process the command
# Set Command puts the clip into the stored file
if command == "set":
    # Get the Key Argument
    key = get_clip_key()
    # Get From the Clipboard
    clip_content = pyperclip.paste()
    # Validate Clipboard Content
    if len(clip_content) == 0:
        print("Nothing Found On Clipboard")
    else:
        # Load Existing Data
        data = load()
        # Save Clip using Key
        data[key] = str(clip_content)
        # Save the Data File
        save(data)
        # Task Completion Message
        print("Copied From Clipboard To Key (" + key + ")")

# Get Command searches for a clip from the stored data
elif command == "get":
    # Get the Key Argument
    key = get_clip_key()
    # Load any existing data
    data = load()
    # Check if Key is valid
    if key in data:
        # Obtain Value of Key
        value = data[key]
        try:
            pyperclip.copy(str(value))
            print("Copied To Clipboard (" + key + ")")
        except:
            print("Could Not Copy To Clipboard")
    else:
        print("Key Not Found (" + key + ")")

# Keys Command prints all keys
elif command == "keys":
    # Load from Data File
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
