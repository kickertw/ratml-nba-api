from flask import Flask
from flask_cors import CORS
from nba_api.stats.static import teams
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

if __name__ == '__main__':
    app.run(debug=True, port=8080)
