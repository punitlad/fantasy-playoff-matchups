import json


class AvgVs:
    def __init__(self, home, away):
        self.home_name = home
        self.away_name = away
        f = open('data/03.13.2022-all-data.json')
        self.data = json.load(f)
        f.close()

        self.home_data = list(filter(lambda x: x['id'] == self.home_name, self.data['teams']))[0]
        self.away_data = list(filter(lambda x: x['id'] == self.away_name, self.data['teams']))[0]

    def render_string_by_value(self, value_1, value_2): 
        if value_1 > value_2:
            return "\033[92m" + str(value_1) + "\033[0m" + '\t'
        else: 
            return str(value_1) + '\t'

    def output(self):
        total_matchups = 20

        print("\tAvg\tFG%\tFT%\t3PM\tREB\tAST\tSTL\tBLK\tPTS")
        home_averages_as_string = '\t' + self.home_name + '\t'
        away_averages_as_string = '\t' + self.away_name + '\t'

        for category in ("fg%", "ft%", "3pm", "reb", "ast", "stl", "blk", "pts"):
            home_category = list(filter(lambda x: x['type'] == category, self.home_data['statistics']))[0]
            away_category = list(filter(lambda x: x['type'] == category, self.away_data['statistics']))[0]

            if category == 'fg%' or category == 'ft%':
                home_averages_as_string = home_averages_as_string + self.render_string_by_value(home_category['value'], away_category['value'])
                away_averages_as_string = away_averages_as_string + self.render_string_by_value(away_category['value'], home_category['value'])
            else: 
                home_averages_as_string = home_averages_as_string + self.render_string_by_value(home_category['value'] / total_matchups, away_category['value'] / total_matchups)
                away_averages_as_string = away_averages_as_string + self.render_string_by_value(away_category['value'] / total_matchups, home_category['value'] / total_matchups)
        
        print(home_averages_as_string)
        print(away_averages_as_string)
        print('')