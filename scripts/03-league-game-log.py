from nba_api.stats.endpoints import leaguegamelog
import pandas
import json

league_game_log = leaguegamelog.LeagueGameLog()
raw_json = league_game_log.get_normalized_json()
parsed_json = json.loads(raw_json)['LeagueGameLog']
file_name = '../data/json/league-game-log.json'
with open(file_name, 'w') as f:
  json.dump(parsed_json, f)

data = pandas.read_json(file_name)
data.to_csv('../data/csv/league-game-log.csv')
