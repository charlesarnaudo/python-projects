import nflgame
import argparse


def topPasser(week, year, limit):
    games = nflgame.games(year, week)
    players = nflgame.combine_game_stats(games)

    for p in players.passing().sort('passing_tds').limit(limit):
        msg = '%s  %d completed, %d passed, for %d yards, %d TDs and %d INTs'
        print msg % (p, p.passing_cmp, p.passing_att, p.passing_yds,
                     p.passing_tds, p.passing_ints)
    print " "

parser = argparse.ArgumentParser(description="Find NFL Game information.", add_help=False)

#required args

#optional args
parser.add_argument("-h", "--help", action="help")
parser.add_argument("-tp", action='store_true',
                    help='get top passers for a given week')
parser.add_argument('-w', metavar='', help='week to seach for', type=int)
parser.add_argument('-y', metavar='', help='year to seach for', type=int)
parser.add_argument('-l', metavar='', default=5, help='limit of results', type=int)

args = parser.parse_args()

week    = args.w
year    = args.y
limit   = args.l
tp = args.tp

print ""

if tp:
    topPasser(week, year, limit)
