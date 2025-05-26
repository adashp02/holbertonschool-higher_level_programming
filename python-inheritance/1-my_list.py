#!/usr/bin/python3
"""creates a class MyList with inheritance
of class list and prints contents of a list of ints sorted"""


class MyList(list):

    def print_sorted(self):
        """this function will print a sorted list of ints"""

        print(sorted(self))
