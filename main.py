from vs import AvgVs
from week_vs import WeekVs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("home_team", help="home team", type=str)
parser.add_argument("away_team", help="home team", type=str)

args = parser.parse_args()

print()
AvgVs().call(args.home_team, args.away_team)
WeekVs().call(args.home_team, args.away_team)