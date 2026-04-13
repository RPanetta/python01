#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = float(height)
        self.days_old = age
        self._stats = Plant._Stats()

    class _Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self):
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

    @staticmethod
    def is_older(days):
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls(name="Unknown plant", height=0.0, age=0)

    def show(self):
        self._stats._show_count += 1
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")

    def grow(self, amount):
        self.height = self.height + float(amount)
        self._stats._grow_count = self._stats._grow_count + 1

    def age(self, days):
        self.days_old = self.days_old + days
        self._stats._age_count = self._stats._age_count + 1


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

    def bloom(self):
        self.blooming = True


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = float(trunk_diameter)
        self._stats = Tree._TreeStats()

    class _TreeStats(Plant._Stats):
        def __init__(self):
            super().__init__()
            self._shade_count = 0

        def display(self):
            super().display()
            print(f"{self._shade_count} shade")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self):
        self._stats._shade_count += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")


class Seed(Flower):
    def __init__(self, name, height, age, color, seed_count=0):
        super().__init__(name, height, age, color)
        self.seed_count = seed_count

    def show(self):
        super().show()
        print(f"Seeds: {self.seed_count}")


def display_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.seed_count = 42
    sunflower.show()
    display_stats(sunflower)

    print("\n=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_stats(anonymous)
