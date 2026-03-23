"""Results module."""

class Results:
    def record_result(self, inventory, prize):
        inventory.update_cash(prize)