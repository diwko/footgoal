from footgoal.download_data import UnrecognizedTeamError
from urllib.error import HTTPError
from json.decoder import JSONDecodeError
from footgoal.basic_parts import Team
from footgoal.basic_parts import Match


def get_team(input_message):
    ok = False
    while not ok:
        team_name = input(input_message)
        team_name = team_name.replace(' ', '_')
        try:
            return Team(team_name)
        except UnrecognizedTeamError:
            print('Unrecognized team\n')
        except (HTTPError, JSONDecodeError):
            print('Something went wrong. Try again')


def main():
    home_team = get_team("ENTER HOME TEAM: ")
    away_team = get_team("ENTER AWAY TEAM: ")

    match = Match(home_team, away_team)

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
