#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)

plants = [rose, sunflower, cactus]

print("=== Garden Plant Registry ===")
for plant in plants:
    print(f"{plant.name}: {plant.height}cm, {plant.days} days old")
