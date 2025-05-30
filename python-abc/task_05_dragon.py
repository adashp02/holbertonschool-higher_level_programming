#!/usr/bin/python3

class SwimMixin:
    """mixin to add ability to swim"""

    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """mixin to add flying ability"""

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon with mixins"""

    def roar(self):
        print("The dragon roars!")
