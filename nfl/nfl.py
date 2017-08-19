import nflgame
import argparse

parser = argparse.ArgumentParser(description="Find NFL Game information.", add_help=False)
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')


#required args
required.add_argument('--stat', help='category of stat to search for', required=True)

#optional args
optional.add_argument("-h", "--help", action="help", help="show this help message and exit")
optional.add_argument('-w', metavar='', help='week to seach for', type=int)
optional.add_argument('-y', metavar='', help='year to seach for', type=int)

args = parser.parse_args()

week = args.w
year = args.y

games = nflgame.games(year, week)
players = nflgame.combine_game_stats(games)

for p in players.passing().sort('passing_tds').limit(10):
    msg = '%s  %d completed, %d passed, for %d yards and %d TDs'
    print msg % (p, p.passing_cmp, p.passing_att, p.passing_yds, p.passing_tds)
