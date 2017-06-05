import json
import urllib.request as urlreq
import datetime
from footgoal.fixture import Fixture, Result
import time


class UnrecognizedTeamError(Exception):
    pass


class FootballDataOrgDownloader:
    base_url = "http://www.football-data.org/v1"
    requests = 0

    competitions = {}  # season: id
    teams = {}  # name: id
    fixtures_team = {}  # team_id: {season: fixtures}
    fixtures_competition = {}  # competition_id: {season: fixtures}
    matches = {}  # match_id: info

    @classmethod
    def url_download(cls, url, encoding='utf-8'):
        cls.requests += 1
        if cls.requests % 49 == 0:
            time.sleep(60)
        req = urlreq.Request(url, headers={
            'X-Auth-Token': 'c3d4466e2296496ab076955528543e55'})
        return urlreq.urlopen(req).read().decode(encoding)

    @classmethod
    def get_competitions(cls, season):
        if season not in cls.competitions:
            url = cls.base_url + '/competitions?season={}'.format(season)
            cls.competitions[season] = cls.url_download(url)
        return cls.competitions[season]

    @classmethod
    def get_team(cls, name):
        if name not in cls.teams:
            url = cls.base_url + '/teams?name={}'.format(name)
            cls.teams[id] = cls.url_download(url)
        return cls.teams[id]

    @classmethod
    def get_fixtures_team(cls, team_id, season):
        if team_id not in cls.fixtures_team:
            cls.fixtures_team[team_id] = {}
        if season not in cls.fixtures_team[team_id]:
            url = cls.base_url + '/teams/{}/fixtures?season={}'.\
                format(team_id, season)

            cls.fixtures_team[team_id][season] = cls.url_download(url)

        return cls.fixtures_team[team_id][season]

    @classmethod
    def get_fixtures_competition(cls, competition_id, season):
        if competition_id not in cls.fixtures_competition:
            cls.fixtures_competition[competition_id] = {}
        if season not in cls.fixtures_competition[competition_id]:
            url = cls.base_url + '/competitions/{}/fixtures?season={}'.\
                format(competition_id, season)

            cls.fixtures_competition[competition_id][season] = \
                cls.url_download(url)

        return cls.fixtures_competition[competition_id][season]

    @classmethod
    def get_match(cls, match_id):
        if match_id not in cls.matches:
            url = cls.base_url + '/fixtures/{}?head2head=20'.format(match_id)
            cls.matches[match_id] = cls.url_download(url)
        return cls.matches[match_id]


class DataExtractor:
    @classmethod
    def get_fixtures(cls, data):
        fixtures = []
        for fixture in data['fixtures']:
            fixtures.append(cls.get_fixture(fixture))
        return fixtures

    @classmethod
    def get_fixture(cls, data):
        if 'fixture' in data:
            data = data['fixture']

        if '_links' in data:
            match_id = cls.get_id_from_href(data['_links']['self']['href'])

            home_team_id = cls.get_id_from_href(
                data['_links']['homeTeam']['href'])

            away_team_id = cls.get_id_from_href(
                data['_links']['awayTeam']['href'])
        else:
            match_id = data['id']
            home_team_id = data['homeTeamId']
            away_team_id = data['awayTeamId']

        date = cls.parse_date(data['date'])
        status = data['status']
        home_team_name = data['homeTeamName']
        away_team_name = data['awayTeamName']
        result = Result(
            goals_home_team=data['result']['goalsHomeTeam'],
            goals_away_team=data['result']['goalsAwayTeam'])

        return Fixture(match_id, date, status, home_team_id, home_team_name,
                       away_team_id, away_team_name, result)

    @staticmethod
    def get_team_id(data):
        if data['count'] > 0:
            return data['teams'][0]['id']

        raise UnrecognizedTeamError()

    @classmethod
    def get_h2h_fixtures(cls, data):
        fixtures = cls.get_fixtures(data['head2head'])
        fixtures.sort(key=lambda x: x.date)
        return fixtures

    @staticmethod
    def get_id_from_href(href, position=-1):
        return int(href.split('/')[position])

    @staticmethod
    def parse_date(date):
        return datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')


class FootballData:
    competitions = {}  # season: id
    teams = {}  # name: id
    fixtures_team = {}  # team_id: {season: fixtures}
    fixtures_competition = {}  # competition_id: {season: fixtures}
    fixtures_match = {}  # match_id: match
    fixtures_h2h = {} # match_id: h2h_fixtures

    @classmethod
    def get_team_id(cls, team_name):
        if team_name not in cls.teams:
            teams_json = FootballDataOrgDownloader.get_team(team_name)
            teams_data = json.loads(teams_json)
            cls.teams[team_name] = DataExtractor.get_team_id(teams_data)
        return cls.teams[team_name]

    @classmethod
    def get_fixtures_team(cls, team_id, season):
        if team_id not in cls.fixtures_team:
            cls.fixtures_team[team_id] = {}
        if season not in cls.fixtures_team[team_id]:
            fixtures_json = FootballDataOrgDownloader.\
                get_fixtures_team(team_id, season)

            fixtures_data = json.loads(fixtures_json)

            cls.fixtures_team[team_id][season] = \
                DataExtractor.get_fixtures(fixtures_data)

        return cls.fixtures_team[team_id][season]

    @classmethod
    def get_fixtures_competition(cls, competition_id, season):
        if competition_id not in cls.fixtures_competition:
            cls.fixtures_competition[competition_id] = {}
        if season not in cls.fixtures_competition[competition_id]:
            fixtures_json = FootballDataOrgDownloader.\
                get_fixtures_competition(competition_id, season)

            fixtures_data = json.loads(fixtures_json)

            cls.fixtures_competition[competition_id][season] = \
                DataExtractor.get_fixtures(fixtures_data)

        return cls.fixtures_competition[competition_id][season]

    @classmethod
    def download_match_details(cls, match_id):
        match_json = FootballDataOrgDownloader.get_match(match_id)
        match_data = json.loads(match_json)
        cls.fixtures_match[match_id] = DataExtractor.get_fixture(match_data)
        cls.fixtures_h2h[match_id] = DataExtractor.get_h2h_fixtures(match_data)

    @classmethod
    def get_fixture(cls, match_id):
        if match_id not in cls.fixtures_match:
            cls.download_match_details(match_id)
        return cls.fixtures_match[match_id]

    @classmethod
    def get_fixtures_h2h(cls, match_id):
        if match_id not in cls.fixtures_h2h:
            cls.download_match_details(match_id)
        return cls.fixtures_h2h[match_id]
