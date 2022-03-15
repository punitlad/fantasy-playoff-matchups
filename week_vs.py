from ast import Raise
import json


class WeekVs:
    def __init__(self, home, away):
        self.home_name = home
        self.away_name = away

        f = open('data/week1-20-results.json')
        self.data = json.load(f)
        f.close()

        self.home = list(
            filter(lambda x: x['name'] == self.home_name, self.data['matchups']))
        self.away = list(
            filter(lambda x: x['name'] == self.away_name, self.data['matchups']))

        if len(self.home) != len(self.away):
            raise

    def render_string_by_value(self, value_1, value_2): 
        if value_1 > value_2:
            return "\033[1m\033[32m" + str(value_1) + "\033[0m" + '\t'
        else: 
            return str(value_1) + '\t'

    def output(self):
        num_matchups = len(self.home)
        for x in range(num_matchups):
            matchup = x+1
            home_matchup = list(
                filter(lambda x: x['matchup'] == matchup, self.home))[0]
            away_matchup = list(
                filter(lambda x: x['matchup'] == matchup, self.away))[0]
            print("Week\tTeam\tFG%\tFT%\t3PM\tREB\tAST\tSTL\tBLK\tPTS\tVS")
            home_matchup_as_string = str(matchup) + "\t" + self.home_name + '\t'
            away_matchup_as_string = str(matchup) + "\t" + self.away_name + '\t'

            for category in ("fg%", "ft%", "3pm", "reb", "ast", "stl", "blk", "pts"):
              home_category = list(filter(lambda x: x['type'] == category, home_matchup['statistics']))[0]
              away_category = list(filter(lambda x: x['type'] == category, away_matchup['statistics']))[0]
              home_matchup_as_string = home_matchup_as_string + self.render_string_by_value(home_category['value'], away_category['value'])
              away_matchup_as_string = away_matchup_as_string + self.render_string_by_value(away_category['value'], home_category['value'])

            home_vs = home_matchup['vs']
            away_vs = away_matchup['vs']
            print(home_matchup_as_string + home_vs + '\t')
            print(away_matchup_as_string + away_vs + '\t')
            print('')
