from download_data import FootballData
import csv
from urllib.error import HTTPError
from json.decoder import JSONDecodeError
from match_info import get_data_row


def get_learning_row(fixture, count=5):
    in_row = get_data_row(fixture.home_team_id, fixture.away_team_id,
                          fixture.date, count, fixture.id)
    out_val = fixture.result.goals_difference()*100
    in_row.append(out_val)
    return in_row


def download_learning_data(competition_id, season, path, delimiter=';'):
    file = open(path, 'a')
    csv_writer = csv.writer(file, delimiter=delimiter)

    zero_div = 0
    http_errors = 0
    json_errors = 0

    i = 0
    fixtures = FootballData.get_fixtures_competition(competition_id, season)
    fixtures_size = len(fixtures)

    for fixture in fixtures:
        i += 1
        print(i, '/', fixtures_size)
        try:
            row = get_learning_row(fixture)
            csv_writer.writerow(row)
        except ZeroDivisionError as e:
            zero_div += 1
            print("No data", zero_div)
        except HTTPError as e:
            http_errors += 1
            print("Http error", http_errors)
        except JSONDecodeError as e:
            json_errors += 1
            print("Json error", json_errors)

    file.close()
    print('Fixtures downloaded:',
          fixtures_size - zero_div - http_errors - json_errors)
    print('HTTP errors:', http_errors)
    print('JSON errors:', json_errors)
    print('NO DATA:', zero_div)


#download_learning_data(394, 2015, 'data/all_2015.csv') #Bundesliga
#download_learning_data(396, 2015, 'data/all_2015.csv') #Ligue 1
#download_learning_data(398, 2015, 'data/all_2015.csv') #Premier League
#download_learning_data(399, 2015, 'data/all_2015.csv') #Premiera Division
#download_learning_data(401, 2015, 'data/all_2015.csv') #Serie A

#download_learning_data(430, 2016, 'data/all_2016.csv') #Bundesliga
#download_learning_data(434, 2016, 'data/all_2016.csv') #Ligue 1
#download_learning_data(426, 2016, 'data/all_2016.csv') #Premier League
#download_learning_data(436, 2016, 'data/all_2016.csv') #Premiera Division
#download_learning_data(438, 2016, 'data/all_2016.csv') #Serie A


#download_learning_data(433, 2016, 'data/test_data.csv') #Eredivisie