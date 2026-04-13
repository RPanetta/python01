#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        if height < 0:
            print(f"{name}:  Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)
        if age < 0:
            print(f"{name}:  Error, age can't be negative")
            self._age = 0
        else:
            self._age = int(age)

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = float(height)
            print(f"Height updated: {int(self._height)}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = int(age)
            print(f"Age updated: {self._age} days")

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")


print("=== Garden Security System ===")

rose = Plant("Rose", 15, 10)
print(f"Plant created: {rose.name}: "
      f"{rose.get_height()}cm, {rose.get_age()} days old")
print()
rose.set_height(25)
rose.set_age(30)
print()
rose.set_height(-5)
rose.set_age(-3)
print()
print("Current state:", end=" ")
rose.show()
