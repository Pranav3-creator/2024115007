"""Vehicle maintenance module."""

class Maintenance:
    def repair_car(self, car):
        if car["damaged"]:
            car["damaged"] = False