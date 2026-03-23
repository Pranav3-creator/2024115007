"""Leaderboard module."""

class Leaderboard:
    def rank(self, members):
        return sorted(members.items(), key=lambda x: x[1]["skill"], reverse=True)