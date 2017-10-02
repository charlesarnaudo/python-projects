import argparse
from TwitterSearch import *

parser = argparse.ArgumentParser(description="Get username")
parser.add_argument('-u', metavar='', help='user to seach against',
                    type=str, required=True)

args = parser.parse_args()

tuo = TwitterUserOrder(args.u)

ts = TwitterSearch(
    consumer_key=config.consumer_key,
    consumer_secret=config.consumer_secret,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret
)

tf = ['title',
      'fight',
      'the last thing',
      'shed',
      'floral green',
      'spring songs'
      'hyperview',
      'symmetry',
      'like a mirror'
      'western haiku',
      'the top forever',
      'coxton',
      'train nearby',
      'your skin',
      '72',
      '27',
      'where am i',
      'stab',
      'GMT',
      'numb',
      'all away',
      'leaf',
      'like a ritual',
      'ceiling fan',
      'blush',
      'receiving line',
      'your loss',
      'get that a lot',
      'murder your memory',
      'chlorine',
      'don\'t count on me',
      'hypernight',
      'rose of sharon']

occ = 0
count = 0
for tweet in ts.search_tweets_iterable(tuo):
    count += 1
    for term in tf:
        if term in tweet['text'].lower():
            occ += 1

ans = float("{0:.2f}".format(occ / count))

print(args.u + " has tweeted about Title fight in " + str(ans) +
               "% of their tweets")
