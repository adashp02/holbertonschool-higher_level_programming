#!/usr/bin/python3
"""function that appends a string at the end of a text file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """Append a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.
    Returns:
        The number of characters appended."""
    with open(filename, 'a', encoding='utf-8') as f:
        f.append(filename)
        return len(text)
