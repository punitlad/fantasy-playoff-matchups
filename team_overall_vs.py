import json
from art import *


class TeamOverallVs:
    def __init__(self, home, away):
        self.home_name = home
        self.away_name = away
        f = open('data/03.14.2022-all-data.json')
        self.data = json.load(f)
        f.close()

        self.home_record = list(filter(lambda x: x['id'] == self.home_name, self.data['teams']))[0]['record']
        self.away_record = list(filter(lambda x: x['id'] == self.away_name, self.data['teams']))[0]['record']

    def output(self):
        vs_text = "\t" + self.home_name + " vs " + self.away_name
        print(text2art(vs_text,font='colossal'))
        print("\t\t\t\t" + self.home_name + "\tvs\t" + self.away_name)
        print("\t\t\t\t" + self.home_record + "\t\t" + self.away_record)
        print('')