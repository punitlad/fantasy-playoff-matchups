from ast import Raise
import json


class WeekVs:
    def __init__(self, home, away):
        f = open('data/week1-20-results.json')
        self.data = json.load(f)
        f.close()

        self.home = list(
            filter(lambda x: x['name'] == home, self.data['matchups']))
        self.away = list(
            filter(lambda x: x['name'] == away, self.data['matchups']))

        if len(self.home) != len(self.away):
            raise

    def output(self):
        num_matchups = len(self.home)
        for x in range(num_matchups):
            matchup = x+1
            team_1_matchup = list(
                filter(lambda x: x['matchup'] == matchup, self.home))[0]
            team_2_matchup = list(
                filter(lambda x: x['matchup'] == matchup, self.away))[0]
            print("Week\tTeam\tFG%\tFT%\t3PM\tREB\tAST\tSTL\tBLK\tPTS\tVS")

            team_matchups = (team_1_matchup, team_2_matchup)
            for team in team_matchups:
                team_name = team['name']
                team_vs = team['vs']
                team_matchup_as_string = str(matchup) + "\t" + team_name + '\t'
                for stat in team['statistics']:
                    stat_type = stat['type']
                    team_matchup_as_string = team_matchup_as_string + \
                        str(stat['value']) + '\t'

                print(team_matchup_as_string + team_vs + '\t')

            print('')
