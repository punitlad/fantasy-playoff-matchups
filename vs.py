import json


class AvgVs:
    def __init__(self, home, away):
        f = open('data/03.13.2022-all-data.json')
        self.data = json.load(f)
        f.close()

        self.home = list(filter(lambda x: x['id'] == home, self.data['teams']))[0]
        self.away = list(filter(lambda x: x['id'] == away, self.data['teams']))[0]

    def output(self):
        total_matchups = 20

        print("\tTeam\tFG%\tFT%\t3PM\tREB\tAST\tSTL\tBLK\tPTS")

        for team in (self.home, self.away):
            team_name = team['id']
            team_averages_as_string = '\t' + team_name + '\t'
            team_avg_stats = []
            for stat in team['statistics']:
                stat_type = stat['type']
                if stat_type == 'fg%' or stat_type == 'ft%':
                    team_avg_stats.append(stat)
                    team_averages_as_string = team_averages_as_string + \
                        str(stat['value']) + '\t'
                else:
                    average = stat['value'] / total_matchups
                    team_averages_as_string = team_averages_as_string + \
                        str(average) + '\t'
                    team_avg_stats.append(
                        {'type': stat_type, 'value': average})

            print(team_averages_as_string)
        print('')
