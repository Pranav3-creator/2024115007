"""Race management module."""

class Race:
    def create_race(self, driver, car):
        if driver["role"] != "driver":
            raise ValueError("Only drivers can race")

        if car["damaged"]:
            raise ValueError("Car is damaged")

        return True