import json

class AvgVs: 
  def call(self, home_team, away_team): 
    total_matchups = 20

    f = open('data/03.13.2022-all-data.json')
    data = json.load(f)
    f.close()

    vs_teams = list(filter(lambda x: x['id'] == home_team or x['id'] == away_team, data['teams']))

    print("\tTeam\tFG%\tFT%\t3PM\tREB\tAST\tSTL\tBLK\tPTS")

    for team in vs_teams: 
        team_name = team['id']
        team_averages_as_string = '\t' + team_name + '\t'
        team_avg_stats = []
        for stat in team['statistics']:
            stat_type = stat['type']
            if stat_type == 'fg%' or stat_type == 'ft%':
                team_avg_stats.append(stat)
                team_averages_as_string = team_averages_as_string + str(stat['value']) + '\t'
            else:
                average = stat['value'] / total_matchups
                team_averages_as_string = team_averages_as_string + str(average) + '\t'
                team_avg_stats.append({ 'type': stat_type, 'value': average})

        print(team_averages_as_string)
    print()