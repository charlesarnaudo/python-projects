import config, argparse

parser = argparse.ArgumentParser(description="Tweet a lot")
parser.add_argument('-f', metavar='', help="file which contains text to tweet", type=file, required=True)

args = parser.parse_args()
