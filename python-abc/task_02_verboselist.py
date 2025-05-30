#!/usr/bin/python3

class VerboseList(list):
    """A list printing notifications and modifications"""

    def append(self, item):
        """Add an item to the end of the list
        and print notitfications"""

        super().append(item)#calling original method from class list with super
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from
        the iterable and print notification"""

        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove the first occurence of the item
        and print a notification"""

        super().remove(item)
        print(f"Removed [{item}] fromthe list.")

    def pop(self, index=-1):
        """Remove and return item at index (default last)
        and print a notitfication"""

        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
