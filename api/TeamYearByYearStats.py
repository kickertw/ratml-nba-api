from nba_api.stats.endpoints import teamyearbyyearstats

# Input Examples
#   team_id = 1610612752 (Knicks)
#   year = "2000-01"
def get_year_stats(team_id, year):
  team_historic_data = teamyearbyyearstats.TeamYearByYearStats(team_id)
  df = team_historic_data.get_data_frames()
  result = df[0].query('YEAR==@year').head(1)
  return result