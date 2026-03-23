"""Crew management module."""

class Crew:
    def assign_role(self, member, role):
        member["role"] = role

    def assign_skill(self, member, skill):
        if skill < 0:
            raise ValueError("Skill must be positive")
        member["skill"] = skill