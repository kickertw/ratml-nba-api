from nba_api.stats.static import teams
import pandas
import json

all_teams = teams.get_teams()

with open('../data/json/teams.json', 'w') as f:
  json.dump(all_teams, f)

data = pandas.read_json('../data/json/teams.json')
data.to_csv('../data/csv/teams.csv')
