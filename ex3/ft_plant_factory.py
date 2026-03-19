#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

plant_data = [
    ("Rose", 25, 30)
    ("Oak", 200, 365)
    ("Cactus", 5, 90)
    ("Sunflower", 80, 45)
    ("Fern", 15, 120)
    ]

plants = []

print("=== Plant Factory Output ===")