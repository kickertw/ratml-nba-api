import json
import os
from random import randint

z_score_dict = {
  1:-2.326,
  2:-2.054,
  3:-1.881,
  4:-1.751,
  5:-1.645,
  6:-1.555,
  7:-1.476,
  8:-1.405,
  9:-1.341,
  10:-1.282,
  11:-1.227,
  12:-1.175,
  13:-1.126,
  14:-1.08,
  15:-1.036,
  16:-0.994,
  17:-0.954,
  18:-0.915,
  19:-0.878,
  20:-0.842,
  21:-0.806,
  22:-0.772,
  23:-0.739,
  24:-0.706,
  25:-0.674,
  26:-0.643,
  27:-0.613,
  28:-0.583,
  29:-0.553,
  30:-0.524,
  31:-0.496,
  32:-0.468,
  33:-0.44,
  34:-0.412,
  35:-0.385,
  36:-0.358,
  37:-0.332,
  38:-0.305,
  39:-0.279,
  40:-0.253,
  41:-0.228,
  42:-0.202,
  43:-0.176,
  44:-0.151,
  45:-0.126,
  46:-0.1,
  47:-0.075,
  48:-0.05,
  49:-0.025,
  50:0,
  51:0.025,
  52:0.05,
  53:0.075,
  54:0.1,
  55:0.126,
  56:0.151,
  57:0.176,
  58:0.202,
  59:0.228,
  60:0.253,
  61:0.279,
  62:0.305,
  63:0.332,
  64:0.358,
  65:0.385,
  66:0.412,
  67:0.44,
  68:0.468,
  69:0.496,
  70:0.524,
  71:0.553,
  72:0.583,
  73:0.613,
  74:0.643,
  75:0.674,
  76:0.706,
  77:0.739,
  78:0.772,
  79:0.806,
  80:0.842,
  81:0.878,
  82:0.915,
  83:0.954,
  84:0.994,
  85:1.036,
  86:1.08,
  87:1.126,
  88:0.1175,
  89:0.1227,
  90:1.282,
  91:1.341,
  92:1.405,
  93:1.476,
  94:1.555,
  95:1.645,
  96:1.751,
  97:1.881,
  98:2.054,
  99:2.326
}

# Input Examples
#   team_id = 1610612752 (Knicks)
#   year = "2000-01"
#   features = ['FGM', 'FG3M', 'FTM']
def get_randomized_feature_stats(team_id, year, features):
  teams_json = open('data/json/teams.json')
  all_teams = json.load(teams_json)
  team = [x for x in all_teams if x['id'] == team_id][0]

  aggregate_data_json = open('data/json/team-aggregate-stats/{0}/{1}-stats.json'.format(year, team['nickname']))
  aggregated_data = json.load(aggregate_data_json)

  feature_list = features.split(sep=',')

  stats = {}
  for feature in feature_list:
    # Because different calls to the NBA API aren't consistent in terminology :(
    feature = feature.replace('_PCT', 'P')
    feature_avg = aggregated_data[feature]['AVG']
    feature_stdev = aggregated_data[feature]['STDEV']
    random = randint(1,99)
    random_stat = feature_avg + z_score_dict[random] * feature_stdev

    if random_stat < 0:
      stats[feature]=0
    else:
      stats[feature]=random_stat

  return stats
