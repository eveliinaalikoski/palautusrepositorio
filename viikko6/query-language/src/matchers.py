class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def test(self, *matchers):
        return True
    

class Not:
    def __init__(self, term):
        self._term = term
    
    def test(self, player):
        return not self._term.test(player)
    

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False
    

class QueryBuilder():
    def __init__(self):
        self._matcher = All()

    def plays_in(self, team):
        self._matcher = And(self._matcher, PlaysIn(team))
        return self
    
    def has_at_least(self, value, attr):
        self._matcher = And(self._matcher, HasAtLeast(value, attr))
        return self
    
    def has_fewer_than(self, value, attr):
        self._matcher = And(self._matcher, HasFewerThan(value, attr))
        return self
    
    def one_of(self, query_1, query_2):
        self._matcher = Or(query_1, query_2)
        return self

    def build(self):
        return self._matcher
