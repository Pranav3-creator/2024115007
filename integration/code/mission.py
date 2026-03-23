"""Mission planning module."""

class Mission:
    def assign_mission(self, crew_members, required_roles):
        roles = [m["role"] for m in crew_members]

        for role in required_roles:
            if role not in roles:
                raise ValueError("Required role missing")

        return True