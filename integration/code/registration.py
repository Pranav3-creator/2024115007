"""Registration module for managing crew members."""

class Registration:
    def register(self, name, role):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name cannot be empty")

    valid_roles = ["driver", "mechanic", "strategist"]
    if role not in valid_roles:
        raise ValueError("Invalid role")

    if name in self.members:
        raise ValueError("Member already exists")

    self.members[name] = {"role": role, "skill": 0}
    return self.members[name]