import datetime


class Fixture:
    def __init__(self, match_id, date, status, home_team_id, home_team_name,
                 away_team_id, away_team_name, result):
        self.id = match_id
        self.date = date
        self.status = status
        self.home_team_id = home_team_id
        self.home_team_name = home_team_name
        self.away_team_id = away_team_id
        self.away_team_name = away_team_name
        self.result = result

    def winner(self):
        goals_diff = self.result.goals_difference()
        if goals_diff > 0:
            return self.home_team_id
        elif goals_diff == 0:
            return 0
        else:
            return self.away_team_id

    def to_string(self):
        return '{:<12} {:>25} {:>4} - {:<4} {:<25}'.format(
            self.date.strftime('%Y-%m-%d'),
            self.home_team_name,
            self.result.goals_home_team,
            self.result.goals_away_team,
            self.away_team_name)


class Result:
    def __init__(self, goals_home_team, goals_away_team):
        self.goals_home_team = goals_home_team
        self.goals_away_team = goals_away_team

    def goals_difference(self):
        return self.goals_home_team - self.goals_away_team


class FixturesOperation:
    @staticmethod
    def sort_fixtures_by_date(fixtures):
        fixtures.sort(key=lambda f: f.date)

    @classmethod
    def index_before_date(cls, fixtures, date=datetime.datetime.now()):
        x = len(fixtures) - 1
        while x >= 0 and date <= fixtures[x].date:
            x -= 1
        return x

    @classmethod
    def last_fixtures(cls, fixtures, count, date=datetime.datetime.now(),
                      key=lambda fix: True):

        x = cls.index_before_date(fixtures, date)
        last_fixtures = []

        while x >= 0 and count > 0:
            if key(fixtures[x]):
                last_fixtures.insert(0, fixtures[x])
                count -= 1
            x -= 1
        return last_fixtures

    @classmethod
    def free_days(cls, fixtures, date=datetime.datetime.now()):
        x = cls.index_before_date(fixtures, date)
        return (date - fixtures[x].date).days

    @staticmethod
    def match_id_with(fixtures, opponent_id):
        for fixture in fixtures:
            if fixture.home_team_id == opponent_id or \
                            fixture.away_team_id == opponent_id:
                return fixture.id
        return -1

    @staticmethod
    def stats(fixtures, team_id):
        won = 0
        draw = 0
        lost = 0
        goals_diff = 0
        for fixture in fixtures:
            winner_id = fixture.winner()
            goals_d = abs(fixture.result.goals_difference())
            if winner_id == team_id:
                won += 1
                goals_diff += goals_d
            elif winner_id == 0:
                draw += 1
            else:
                lost += 1
                goals_diff -= goals_d

        return won, draw, lost, goals_diff

    @staticmethod
    def to_string(fixtures):
        text = ''
        for i in range(len(fixtures) - 1):
            text += fixtures[i].to_string() + '\n'
        text += fixtures[-1].to_string()
        return text
