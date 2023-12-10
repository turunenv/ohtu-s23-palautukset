from matchers import And, All, Or, Not, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self):
        self.matcher = All()

    def playsIn(self, team):
        pass

    def build(self):
        return self.matcher