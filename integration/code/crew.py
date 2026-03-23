"""Crew management module."""

class Crew:
    def assign_role(self, member, role):
        if not isinstance(member, dict):
            raise ValueError("Invalid member data")

        valid_roles = ["driver", "mechanic", "strategist"]
        if role not in valid_roles:
            raise ValueError("Invalid role")

        member["role"] = role


    def assign_skill(self, member, skill):
        if not isinstance(member, dict):
            raise ValueError("Invalid member data")

        if not isinstance(skill, int):
            raise ValueError("Skill must be an integer")

        if skill < 0 or skill > 100:
            raise ValueError("Skill must be between 0 and 100")

        member["skill"] = skill