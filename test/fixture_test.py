from footgoal.fixture import Fixture, Result, FixturesOperation
import datetime


def test_result_goal_difference():
    res = Result(10, 1)
    assert res.goals_difference() == 9

    res = Result(2, 3)
    assert res.goals_difference() == -1

    res = Result(5, 5)
    assert res.goals_difference() == 0


def test_fixture_winner():
    fix = Fixture(1, datetime.datetime(2016, 5, 3), 'end',
                  10, 'ABC', 20, 'XYZ', Result(5, 1))
    assert fix.winner() == 10

    fix = Fixture(1, datetime.datetime(2016, 8, 9), 'end',
                  10, 'ABC', 20, 'XYZ', Result(0, 1))
    assert fix.winner() == 20

    fix = Fixture(1, datetime.datetime(2006, 10, 3), 'end',
                  10, 'ABC', 20, 'XYZ', Result(1, 1))
    assert fix.winner() == 0


def test_fixtures_sort():
    f1 = Fixture(1, datetime.datetime(2015, 5, 3), 'end',
                  10, 'ABC', 20, 'XYZ', Result(5, 1))

    f2 = Fixture(1, datetime.datetime(2016, 10, 20), 'end',
                 10, 'ABC', 20, 'XYZ', Result(5, 1))

    f3 = Fixture(1, datetime.datetime(2005, 8, 19), 'end',
                 10, 'ABC', 20, 'XYZ', Result(5, 1))

    fixtures = [f1, f2, f3]
    FixturesOperation.sort_fixtures_by_date(fixtures)
    assert fixtures == [f3, f1, f2]


def test_index_before_date():
    f1 = Fixture(1, datetime.datetime(2015, 5, 3), 'end',
                 10, 'ABC', 20, 'XYZ', Result(5, 1))

    f2 = Fixture(1, datetime.datetime(2016, 10, 20), 'end',
                 10, 'ABC', 20, 'XYZ', Result(5, 1))

    f3 = Fixture(1, datetime.datetime(2005, 8, 19), 'end',
                 10, 'ABC', 20, 'XYZ', Result(5, 1))

    fixtures = [f3, f1, f2]
    assert FixturesOperation.\
        index_before_date(fixtures, datetime.datetime(2016, 1, 1)) == 1

    assert FixturesOperation.\
        index_before_date(fixtures, datetime.datetime(2015, 1, 1)) == 0

    assert FixturesOperation.\
        index_before_date(fixtures, datetime.datetime(2017, 1, 1)) == 2

    assert FixturesOperation. \
        index_before_date(fixtures, datetime.datetime(2004, 1, 1)) == -1


def test_free_days():
    f1 = Fixture(1, datetime.datetime(2015, 5, 3), 'end',
                 10, 'ABC', 20, 'XYZ', Result(5, 1))

    f2 = Fixture(1, datetime.datetime(2016, 10, 20), 'end',
                 10, 'ABC', 20, 'XYZ', Result(5, 1))

    f3 = Fixture(1, datetime.datetime(2005, 8, 19), 'end',
                 10, 'ABC', 20, 'XYZ', Result(5, 1))

    fixtures = [f3, f1, f2]

    assert FixturesOperation.free_days(fixtures,
                                       datetime.datetime(2015, 5, 20)) == 17

    assert FixturesOperation.free_days(fixtures,
                                       datetime.datetime(2016, 10, 25)) == 5

    assert FixturesOperation.free_days(fixtures,
                                       datetime.datetime(2005, 8, 20)) == 1

    assert FixturesOperation.free_days(fixtures,
                                       datetime.datetime(2005, 8, 10)) == 0


def test_match_id_with():
    f1 = Fixture(1, datetime.datetime(2015, 5, 3), 'end',
                 10, 'ABC', 30, 'XYZ', Result(5, 1))

    f2 = Fixture(2, datetime.datetime(2016, 10, 20), 'end',
                 10, 'ABC', 15, 'XYZ', Result(5, 1))

    f3 = Fixture(3, datetime.datetime(2005, 8, 19), 'end',
                 10, 'ABC', 20, 'XYZ', Result(5, 1))

    fixtures = [f3, f1, f2]

    assert FixturesOperation.match_id_with(fixtures, 15) == 2
    assert FixturesOperation.match_id_with(fixtures, 5) == -1


def test_stats():
    f1 = Fixture(1, datetime.datetime(2015, 5, 3), 'end',
                 10, 'ABC', 30, 'XYZ', Result(5, 1))

    f2 = Fixture(2, datetime.datetime(2016, 10, 20), 'end',
                 10, 'ABC', 15, 'XYZ', Result(4, 3))

    f3 = Fixture(3, datetime.datetime(2005, 8, 19), 'end',
                 10, 'ABC', 20, 'XYZ', Result(0, 0))

    f4 = Fixture(3, datetime.datetime(2005, 8, 19), 'end',
                 10, 'ABC', 20, 'XYZ', Result(0, 1))

    fixtures = [f3, f1, f2, f4]
    assert FixturesOperation.stats(fixtures, 10) == (2, 1, 1, 4)