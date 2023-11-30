class TennisPlayer:
    def __init__(self, name, points = 0):
        self.name = name
        self.points = points

    def increment_points(self):
        self.points += 1

    def calculate_points_diff(self, player2):
        return abs(self.points, player2.points)
    