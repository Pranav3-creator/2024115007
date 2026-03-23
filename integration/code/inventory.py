"""Inventory module."""

class Inventory:
    def __init__(self):
        self.cars = []
        self.cash = 0

    def add_car(self, car):
        self.cars.append({"name": car, "damaged": False})

    def damage_car(self, car):
        for c in self.cars:
            if c["name"] == car:
                c["damaged"] = True

    def update_cash(self, amount):
        self.cash += amount