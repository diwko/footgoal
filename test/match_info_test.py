from footgoal.match_info import get_season
import datetime


def test_get_season():
    assert get_season(datetime.datetime(2015, 1, 1)) == 2014
    assert get_season(datetime.datetime(2015, 10, 12)) == 2015
    assert get_season(datetime.datetime(2012, 8, 5)) == 2012

