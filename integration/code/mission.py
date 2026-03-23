"""Mission planning module."""

class Mission:
    def assign_mission(self, crew_members, required_roles):
        if not crew_members:
            raise ValueError("Crew cannot be empty")

        if not required_roles:
            raise ValueError("Required roles cannot be empty")

        for member in crew_members:
            if not isinstance(member, dict) or "role" not in member:
                raise ValueError("Invalid crew member data")

        roles = [m["role"] for m in crew_members]

        for role in required_roles:
            if role not in roles:
                raise ValueError("Required role missing")

        return True