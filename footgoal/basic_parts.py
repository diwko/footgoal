from footgoal.download_data import FootballData
from footgoal.fixture import FixturesOperation
import datetime
from footgoal.match_info import get_data_row_with_teams
from sklearn.externals import joblib
import os


def get_season(match_date=datetime.datetime.now()):
    if match_date < datetime.datetime(match_date.year, 8, 1):
        return match_date.year - 1
    return match_date.year


class Team:
    def __init__(self, team):
        if type(team) == int:
            self.team_id = team
        elif type(team) == str:
            self.team_id = FootballData.get_team_id(team)
        else:
            raise AttributeError

        self.fixtures = self._download_fixtures()
        self.name = self.fixtures[0].home_team_name if self.team_id == \
            self.fixtures[0].home_team_id else self.fixtures[0].away_team_name

    def _download_fixtures(self, from_season=2015):
        fixtures = []
        for s in range(from_season, get_season() + 1):
            fixtures += FootballData.get_fixtures_team(self.team_id, s)
        return fixtures

    def get_fixtures(self, count=5, before=datetime.datetime.now()):
        return FixturesOperation.last_fixtures(self.fixtures, count, before)

    def get_home_fixtures(self, count=5, before=datetime.datetime.now()):
        return FixturesOperation.last_fixtures(self.fixtures, count, before,
                                               lambda x:
                                               x.home_team_id == self.team_id)

    def get_away_fixtures(self, count=5, before=datetime.datetime.now()):
        return FixturesOperation.last_fixtures(self.fixtures, count, before,
                                               lambda x:
                                               x.away_team_id == self.team_id)

    def print_fixtures(self, count=5, before=datetime.datetime.now()):
        print("FIXTURES:", self.name)
        fixtures = self.get_fixtures(count, before)
        print(FixturesOperation.to_string(fixtures))
        print(FixturesOperation.stats(fixtures, self.team_id))

    def print_home_fixtures(self, count=5, before=datetime.datetime.now()):
        print("HOME FIXTURES:", self.name)
        fixtures = self.get_home_fixtures(count, before)
        print(FixturesOperation.to_string(fixtures))
        print(FixturesOperation.stats(fixtures, self.team_id))

    def print_away_fixtures(self, count=5, before=datetime.datetime.now()):
        print("AWAY FIXTURES:", self.name)
        fixtures = self.get_away_fixtures(count, before)
        print(FixturesOperation.to_string(fixtures))
        print(FixturesOperation.stats(fixtures, self.team_id))


class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.h2h_fixtures = self._download_h2h_fixtures()

    def _download_h2h_fixtures(self):
        match_id = FixturesOperation.match_id_with(self.home_team.fixtures,
                                                   self.away_team.team_id)
        if match_id == -1:
            return []

        return FootballData.get_fixtures_h2h(match_id)

    def get_h2h_fixtures(self, count=5, before=datetime.datetime.now()):
        return FixturesOperation.last_fixtures(self.h2h_fixtures, count,
                                               before)

    def get_h2h_h_a_fixtures(self, count=5, before=datetime.datetime.now()):
        return FixturesOperation.last_fixtures(self.h2h_fixtures, count,
                                               before, lambda x:
                                               x.home_team_id ==
                                               self.home_team.team_id)

    def predict(self, count=5, match_date=datetime.datetime.now()):
        data_row = get_data_row_with_teams(self.home_team, self.away_team,
                                           self.h2h_fixtures, match_date,
                                           count)

        classifier = joblib.load(os.path.dirname(os.path.abspath(__file__)) +
                                 '/data/classifier_model')
        result = classifier.predict([data_row])
        if result == 1:
            return self.home_team.name
        elif result == 0:
            return 'DRAW'
        else:
            return self.away_team.name

    def print_h2h_fixtures(self, count=5, before=datetime.datetime.now()):
        print("H2H FIXTURES")
        last_h2h = self.get_h2h_fixtures(count, before)
        print(FixturesOperation.to_string(last_h2h))
        print(FixturesOperation.stats(last_h2h, self.home_team.team_id), '\n')
        print("H2H FIXTURES H/A")
        last_h_a_h2h = self.get_h2h_h_a_fixtures(count, before)
        print(FixturesOperation.to_string(last_h_a_h2h))
        print(FixturesOperation.stats(last_h_a_h2h, self.home_team.team_id))
