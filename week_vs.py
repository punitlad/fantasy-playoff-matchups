import json

class WeekVs: 
  def call(self, home_team, away_team): 
    f = open('data/week1-20-results.json')
    data = json.load(f)
    f.close()

    team_1 = list(filter(lambda x: x['name'] == home_team, data['matchups']))
    team_2 = list(filter(lambda x: x['name'] == away_team, data['matchups']))

    if len(team_1) != len(team_2): 
      print("team lengths are not equal!")
      print(team_1)
      print(team_2)
    else: 
      num_matchups = len(team_1)
      for x in range(num_matchups): 
        matchup = x+1
        team_1_matchup = list(filter(lambda x: x['matchup'] == matchup, team_1))[0]
        team_2_matchup = list(filter(lambda x: x['matchup'] == matchup, team_2))[0]
        print("Week\tTeam\tFG%\tFT%\t3PM\tREB\tAST\tSTL\tBLK\tPTS\tVS")

        team_matchups = (team_1_matchup, team_2_matchup)
        for team in team_matchups: 
            team_name = team['name']
            team_vs = team['vs']
            team_matchup_as_string = str(matchup) + "\t" + team_name + '\t'
            for stat in team['statistics']:
                stat_type = stat['type']
                team_matchup_as_string = team_matchup_as_string + str(stat['value']) + '\t'

            print(team_matchup_as_string + team_vs + '\t')

        print('')