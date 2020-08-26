from nba_api.stats.endpoints import teamyearbyyearstats
import pandas
import json

json_file = open('../data/json/teams.json')
all_teams = json.load(json_file)

for team in all_teams:
  team_historic_data = teamyearbyyearstats.TeamYearByYearStats(team_id=team['id'])
  raw_json = team_historic_data.get_normalized_json()
  parsed_json = json.loads(raw_json)['TeamStats']
  file_name = '../data/json/team-historic-data/{0}-historic-data.json'.format(team['nickname'])
  with open(file_name, 'w') as f:
    json.dump(parsed_json, f)

  data = pandas.read_json(file_name)
  data.to_csv('../data/csv/team-historic-data/{0}-historic-data.csv'.format(team['nickname']))
