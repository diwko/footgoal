from footgoal.download_data import UnrecognizedTeamError
from urllib.error import HTTPError
from json.decoder import JSONDecodeError
from footgoal.basic_parts import Team
from footgoal.basic_parts import Match
import argparse


def get_team_name(input_message):
    team_name = input(input_message)
    return team_name.replace(' ', '_')


def get_team(input_message, team_name=None):
    if team_name is None:
        team_name = get_team_name(input_message)

    while True:
        try:
            return Team(team_name)
        except UnrecognizedTeamError:
            print('Unrecognized team\n')
            team_name = get_team_name(input_message)
        except (HTTPError, JSONDecodeError):
            print('Something went wrong. Try again')
            team_name = get_team_name(input_message)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--home", help='home team name', default=None)
    parser.add_argument("--away", help='away team name', default=None)
    args = parser.parse_args()

    home_team = get_team("ENTER HOME TEAM: ", args.home)
    away_team = get_team("ENTER AWAY TEAM: ", args.away)

    for i in range(10):
        try:
            match = Match(home_team, away_team)
            break
        except (HTTPError, JSONDecodeError):
            pass

    home_team.print_fixtures()
    print('\n')
    away_team.print_fixtures()
    print('\n')
    home_team.print_home_fixtures()
    print('\n')
    away_team.print_away_fixtures()
    print('\n')
    match.print_h2h_fixtures()
    print('\n')
    print("PREDICTED RESULT:", match.predict())

if __name__ == '__main__':
    main()
