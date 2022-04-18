# Clipboard Data Management
import pyperclip
import json
import sys

# The path of the file where data is stored
file_path = "clipper_data.json"

# Load the data from the saved file
def load():
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except:
        return {}

# Save the data to the file
def save(data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

# Validate Command Line Args
if len(sys.argv) < 3:
    raise ValueError("Argument not found")

# Get the command
command = sys.argv[1].lower()

# Obtain the Key from the command line arguments
def get_clip_key():
    # Expect 2nd Argument to be key name
    clip_key = sys.argv[2]
    # Ensure Key is valid
    if clip_key == None or len(clip_key) < 1:
        raise ValueError("Invalid Key for Save Command")
    return clip_key

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

# Get Command gets a clip from the stored data
elif command == "get":
    # Get the Key Argument
    key = get_clip_key()
    # Load any existing data
    data = load()
    # Get Clip using Key
    pyperclip.copy(str(data[key]))

# Unknown Command
else:
    raise ValueError("Unknown Command Received" + command)
