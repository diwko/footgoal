from footgoal.download_data import DataExtractor
import json
import datetime


def test_get_id_from_href():
    assert DataExtractor.get_id_from_href("http://api.football-data.org"
                                          "/v1/competitions/426") == 426

    assert DataExtractor.get_id_from_href("http://api.football-data.org"
                                          "/v1/fixtures/150575") == 150575


def test_get_fixture():
    with open('test_fixture.json') as file:
        text = file.read()

    fixture = DataExtractor.get_fixture(json.loads(text))
    assert fixture.id == 150841
    assert fixture.date == datetime.datetime(2016, 8, 13, 11, 30)
    assert fixture.status == "FINISHED"
    assert fixture.home_team_id == 322
    assert fixture.home_team_name == "Hull City FC"
    assert fixture.away_team_id == 338
    assert fixture.away_team_name == "Leicester City FC"
    assert fixture.result.goals_home_team == 2
    assert fixture.result.goals_away_team == 1
