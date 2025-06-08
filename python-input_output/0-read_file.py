#!/usr/bin/python3
"""function that reads a text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="UTF=8") as f:
        print(f.read(), end="")
