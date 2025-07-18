#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
