from footgoal.download_data import FootballData
from footgoal.fixture import FixturesOperation
import datetime


def get_season(match_date=datetime.datetime.now()):
    if match_date < datetime.datetime(match_date.year, 8, 1):
        return match_date.year - 1
    return match_date.year


def get_team_fixtures_all(team_id, date):
    season = get_season(date)
    team_fixtures = []
    for s in range(2015, season + 1):
        team_fixtures += FootballData.get_fixtures_team(team_id, s)
    return team_fixtures


def get_points_goals(fixtures, team_id):
    stats = FixturesOperation.stats(fixtures, team_id)
    matches = stats[0] + stats[1] + stats[2]
    if matches <= 0:
        return 0, 0
    return int((stats[0] - stats[1]) * 100 / matches), int(
        stats[3] * 100 / matches)


def get_last_fixtures_points_goals(team_fixtures, team_id, key=lambda x: True,
                                   match_date=datetime.datetime.now(),
                                   count=5):
    last_fixtures = FixturesOperation.last_fixtures(team_fixtures, count,
                                                    match_date, key)
    return get_points_goals(last_fixtures, team_id)


def get_h2h_match_id(home_team_id, away_team_id,
                     match_date=datetime.datetime.now()):
    home_team_fixtures = get_team_fixtures_all(home_team_id, match_date)
    return FixturesOperation.match_id_with(home_team_fixtures, away_team_id)


def get_h2h_fixtures(home_team_id, away_team_id, h2h_match_id=None,
                     match_date=datetime.datetime.now()):
    if h2h_match_id is None:
        h2h_match_id = get_h2h_match_id(home_team_id, away_team_id, match_date)

    return FootballData.get_fixtures_h2h(h2h_match_id)


def get_row_with_fixtures(fixtures, team_id, fixture_key,
                          match_date=datetime.datetime.now(), count=5):
    # 0 - POINTS
    # 1 - GOALS
    # 2 - POINTS_KEY
    # 3 - GOALS_KEY
    # 4 - FREE_DAYS
    row = [0, 0, 0, 0, 0]

    row[0], row[1] = get_last_fixtures_points_goals(fixtures, team_id,
                                                    lambda x: True, match_date,
                                                    count)
    row[2], row[3] = get_last_fixtures_points_goals(fixtures, team_id,
                                                    fixture_key, match_date,
                                                    count)
    row[4] = FixturesOperation.free_days(fixtures, match_date)
    return row


def get_data_row(home_team_id, away_team_id,
                 match_date=datetime.datetime.now(), count=5,
                 h2h_match_id=None):
    # 0 - POINTS
    # 1 - GOALS
    # 3 - POINTS_KEY
    # 3 - GOALS_KEY
    # 4 - FREE_DAYS
    # 5 - H2H_POINTS
    # 6 - H2H_GOALS
    # 7 - H2H_POINTS_KEY
    # 8 - H2H_GOALS_KEY
    row = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    home_team_fixtures = get_team_fixtures_all(home_team_id, match_date)
    home_team_row = get_row_with_fixtures(home_team_fixtures, home_team_id,
                                          lambda
                                              x: x.home_team_id == home_team_id,
                                          match_date, count)
    for i in range(5):
        row[i] += home_team_row[i]

    away_team_fixtures = get_team_fixtures_all(away_team_id, match_date)
    away_team_row = get_row_with_fixtures(away_team_fixtures, away_team_id,
                                          lambda
                                              x: x.away_team_id == away_team_id,
                                          match_date, count)
    for i in range(5):
        row[i] -= away_team_row[i]

    h2h_fixtures = get_h2h_fixtures(home_team_id, away_team_id, h2h_match_id,
                                    match_date)
    h2h_row = get_row_with_fixtures(h2h_fixtures, home_team_id,
                                    lambda x: x.home_team_id == home_team_id,
                                    match_date, count)
    for i in range(4):
        row[i + 5] += h2h_row[i]

    return row


def get_data_row_with_teams(home_team, away_team, h2h_fixtures,
                            match_date=datetime.datetime.now(), count=5):
    # 0 - POINTS
    # 1 - GOALS
    # 3 - POINTS_KEY
    # 3 - GOALS_KEY
    # 4 - FREE_DAYS
    # 5 - H2H_POINTS
    # 6 - H2H_GOALS
    # 7 - H2H_POINTS_KEY
    # 8 - H2H_GOALS_KEY
    row = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    home_team_row = get_row_with_fixtures(home_team.fixtures,
                                          home_team.team_id, lambda
                                              x: x.home_team_id ==
                                                 home_team.team_id,
                                          match_date, count)
    for i in range(5):
        row[i] += home_team_row[i]

    away_team_row = get_row_with_fixtures(away_team.fixtures,
                                          away_team.team_id, lambda
                                              x: x.away_team_id ==
                                                 away_team.team_id,
                                          match_date, count)
    for i in range(5):
        row[i] -= away_team_row[i]

    h2h_row = get_row_with_fixtures(h2h_fixtures, home_team.team_id,
                                    lambda
                                        x: x.home_team_id == home_team.team_id,
                                    match_date, count)
    for i in range(4):
        row[i + 5] += h2h_row[i]

    return row
