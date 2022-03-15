from vs import AvgVs
from week_vs import WeekVs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("home_team", help="home team", type=str)
parser.add_argument("away_team", help="home team", type=str)

args = parser.parse_args()

print('')
AvgVs(args.home_team, args.away_team).output()
WeekVs(args.home_team, args.away_team).output()
