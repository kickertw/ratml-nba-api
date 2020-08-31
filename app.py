from flask import Flask
from flask import request
from flask_cors import CORS

from api.TeamYearByYearStats import get_year_stats
from api.TeamAggregateStats import get_randomized_feature_stats
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamyearbyyearstats
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def health_check():
    return 'OK'

@app.route('/teams')
def get_teams():
    all_teams = teams.get_teams()
    return json.dumps(all_teams)

# team_id = 1610612752 (knicks)
# year = '1996-97'
@app.route('/team-stats/<team_id>/<year>')
def get_team_stats(team_id, year):
    year_data = get_year_stats(team_id, year)

    # Janky string manipulation to make JSON correct
    result = year_data.to_json(orient="table", index=False)
    ii = result.index('{"TEAM_ID"')
    result = result[ii:len(result)-2]
    return result

# team_id = 1610612752 (knicks)
# year = '1996-97'
# features = 'FGM,FG3M,FTM'
@app.route('/aggregated-stats/<team_id>/<year>')
def get_aggregated_stats(team_id, year):
    features = request.args.get('features')

    stats = get_randomized_feature_stats(int(team_id), year, features)
    return stats

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
