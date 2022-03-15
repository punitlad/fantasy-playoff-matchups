import json


class TeamOverallVs:
    def __init__(self, home, away):
        self.home_name = home
        self.away_name = away
        f = open('data/03.13.2022-all-data.json')
        self.data = json.load(f)
        f.close()

        self.home_record = list(filter(lambda x: x['id'] == self.home_name, self.data['teams']))[0]['record']
        self.away_record = list(filter(lambda x: x['id'] == self.away_name, self.data['teams']))[0]['record']

    def output(self):
        print("\t\t\t\t" + self.home_name + "\tVS\t" + self.away_name + "\t\t")
        print("\t\t\t\t" + self.home_record + "\t" + self.away_record + "\t\t")
        print('')