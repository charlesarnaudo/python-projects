import argparse
import sys
import nflgame

class NFLFunc(object):

    def __init__(self, args):
        self.year = args.y
        self.week = args.w
        self.limit = args.l


    def passer(self):
        games = nflgame.games(2012, 5)
        players = nflgame.combine_game_stats(games)

        for p in players.passing().sort('passing_tds').limit(self.limit):
            msg = '%s  %d completed, %d passed, for %d yards, %d TDs and %d INTs'
            return msg % (p, p.passing_cmp, p.passing_att, p.passing_yds, p.passing_tds, p.passing_ints)


class NFLParse(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Search NFL info from your CLI',
            usage='''nfl <command> [<args>]

Common commands:
    passer      Get information about passers
            ''')
        parser.add_argument('command', help='Subcommand to run')

        # parse_args defaults to [1:] for args
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def passer(self):
        parser = argparse.ArgumentParser(
            description='Get information about passers')
        parser.add_argument('-w', metavar='', help='week to seach for', type=int, required=True)
        parser.add_argument('-y', metavar='', help='year to seach for', type=int, required=True)
        parser.add_argument('-l', metavar='', default=5, help='limit of results', type=int, required=True)
        # 2 onwards for the rest of args
        args = parser.parse_args(sys.argv[2:])
        func = NFLFunc(args)
        print func.passer()


if __name__ == '__main__':
    NFLParse()
