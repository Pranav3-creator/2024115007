"""Registration module for managing crew members."""

class Registration:
    def __init__(self):
        self.members = {}

    def register(self, name, role):
        if name in self.members:
            raise ValueError("Member already exists")
        self.members[name] = {"role": role, "skill": 0}
        return self.members[name]