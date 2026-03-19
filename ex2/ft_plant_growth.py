#!/usr/bin/env python3
class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        print(self.name + ": " + str(self.height) + "cm, "
              + str(self.days) + " days old")

    def simulate_week(self):
        day = 1
        while day <= 7:
            self.grow()
            self.age()
            day += 1
