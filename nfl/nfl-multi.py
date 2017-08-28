import argparse
import sys
import nflgame

class NFLFunc(object):

    def __init__(self, args):
        self.args = args

    def test(self):
        return "test"

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
        parser.add_argument('-w', metavar='', help='week to seach for', type=int)
        parser.add_argument('-y', metavar='', help='year to seach for', type=int)
        parser.add_argument('-l', metavar='', default=5, help='limit of results', type=int)
        # 2 onwards for the rest of args
        args = parser.parse_args(sys.argv[2:])
        func = NFLFunc(args)
        print func.test()


if __name__ == '__main__':
    NFLParse()
