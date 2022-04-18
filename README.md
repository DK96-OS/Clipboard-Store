# Clipboard-Store
This is a little tool that copies between the clipboard and a data file, using keys to identify data.

## Usage
To use, run the script from command line, and pass arguments after script name.

__Set__:
Clipboard -> Data File

Use the __Set__ command:
`python3 clipper.py set key`

__Get__:
Data File -> Clipboard

Use the __Get__ command:
`python3 clipper.py get key`


## Dependencies
- Python 3.8 or higher
- `pyperclip`

On Linux:
- `xsel` or `xclip`


## Additional Information
The data is stored in a __JSON__ formatted file, called `clipper_data.json`.
This file is kept in the same directory as `clipper.py`.
