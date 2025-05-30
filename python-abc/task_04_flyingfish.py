#!/usr/bin/python3

class Fish:
    """class representing a fish"""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """class representing a bird"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """class representing a flying fish
    inheriting from Fish and Bird"""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print ("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
    print(FlyingFish.mrol())
