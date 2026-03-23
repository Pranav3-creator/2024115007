"""Race management module."""

class Race:
    def create_race(self, driver, car):
        if not isinstance(driver, dict) or "role" not in driver:
            raise ValueError("Invalid driver data")

        if not isinstance(car, dict) or "name" not in car or "damaged" not in car:
            raise ValueError("Invalid car data")

        if driver["role"] != "driver":
            raise ValueError("Only drivers can race")

        if car["damaged"]:
            raise ValueError("Car is damaged")

        return True