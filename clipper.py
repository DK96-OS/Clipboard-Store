#!/usr/bin/env python3
# Clipboard Data Management
import pyperclip
import json
import sys

# The path of the Data File
file_path = "clipper_data.json"

# Valid number of Command Line Arguments
if len(sys.argv) < 3:
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
    # Load any existing data
    data = load()
    # Save Clip using Key
    data[key] = str(pyperclip.paste())
    # Save the data to the file
    save(data)

# Get Command searches for a clip from the stored data
elif command == "get":
    # Get the Key Argument
    key = get_clip_key()
    # Load any existing data
    data = load()
    # Get Clip using Key
    pyperclip.copy(str(data[key]))

# Keys Command prints all keys
elif command == "keys":
    # Load data
    data = load()
    # Get and print all keys
    for key in data.keys:
        print(key)

# Unknown Command
else:
    raise ValueError("Unknown Command Received" + command)
