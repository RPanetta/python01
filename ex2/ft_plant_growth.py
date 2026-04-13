#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age, growth_rate):
        self.name = name
        self.height = height
        self.days = age
        self.growth_rate = growth_rate

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.days} days old")

    def grow(self):
        self.height = self.height + self.growth_rate
        self.height = round(self.height, 1)

    def age(self):
        self.days = self.days + 1


rose = Plant("Rose", 25.0, 30, 0.8)

print("=== Garden Plant Growth ===")
rose.show()

initial_height = rose.height

for day in range(1, 8):
    rose.grow()
    rose.age()
    print(f"=== Day {day} ===")
    rose.show()

growth = round(rose.height - initial_height, 1)
print(f"Growth this week: {growth}cm")
