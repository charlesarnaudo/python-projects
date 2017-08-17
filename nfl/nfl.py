import nflgame
import argparse

parser = argparse.ArgumentParser(description="Find NFL Game information.")

parser.add_argument('-w', metavar='', help='week to seach for', type=int)
parser.add_argument('-y', metavar='', help='year to seach for', type=int)
args = parser.parse_args()

week = args.w
year = args.y

games = nflgame.games(year, week)
players = nflgame.combine_game_stats(games)

for p in players.passing().sort('passing_tds').limit(10):
    msg = '%s  %d completed, %d passed, for %d yards and %d TDs'
    print msg % (p, p.passing_cmp, p.passing_att, p.passing_yds, p.passing_tds)
