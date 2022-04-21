# Cliper
This is a little tool that copies between the clipboard and a data file, using keys to identify data.

## Usage
To use, run from command line, and pass one of the recognized __Commands__ followed by a key, or other argument depending on the __Command__.
You can add the repository directory to your Environment Path to run from any working directory.

## Commands
__Set__: Copy from Clipboard to Data File
`cliper set example-key`

__Get__: Copy from Data File to Clipboard
`cliper get example-key`

__Keys__: Print a list of the stored Keys
`cliper keys`

## Dependencies
- Python 3.8 or higher
- `pyperclip`

On Linux:
- `xsel` or `xclip`


## Additional Information
The data is stored in a __JSON__ formatted file, called `cliper_data.json`.
This file is kept in the same directory as `cliper.py`.
