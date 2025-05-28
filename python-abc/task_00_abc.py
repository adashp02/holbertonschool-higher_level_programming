#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal"""


    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses
        
        Returns:
            str: a sound made by a specific animal
        """
        pass

    class Dog(Animal):
        """class representing a Dog, subclass of Animal"""

        def sound(self):
            """returns sound made by a dog
            
            Returns:
                str: 'Bark'
            """
            return "Bark"
        
    class Cat(Animal):
        """class representing a cat, subclass of Animal"""

        def sound(self):
            """returns sound made by a cat
            
            Returns
                str: 'Meow'
            """

            return "Meow"
 
