#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.age = int(age)

    def show(self):
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


rose = Plant("Rose", 25, 30)
oak = Plant("Oak", 200, 365)
cactus = Plant("Cactus", 5, 90)
sunflower = Plant("Sunflower", 80, 45)
fern = Plant("Fern", 15, 120)

print("=== Plant Factory Output ===")
rose.show()
oak.show()
cactus.show()
sunflower.show()
fern.show()
