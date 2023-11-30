class TennisPlayer:
    def __init__(self, name, points = 0):
        self.name = name
        self.points = points

    def increment_points(self):
        self.points += 1

    