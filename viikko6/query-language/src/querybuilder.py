from matchers import And, All, Or, Not, HasAtLeast, HasFewerThan, PlaysIn

class QueryBuilder:
    def __init__(self, matcher = All()):
        self.matcher = matcher

    def playsIn(self, team):
        return QueryBuilder(And(self.matcher, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self.matcher, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self.matcher, HasFewerThan(value, attr)))
    
    def oneOf(self, matcher1, matcher2):
        return QueryBuilder(Or(matcher1, matcher2))

    def build(self):
        return self.matcher