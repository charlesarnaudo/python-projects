from TwitterSearch import *
import config

try:
    tuo = TwitterUserOrder('dylanilkowitz')

    ts = TwitterSearch(
        consumer_key = config.consumer_key,
        consumer_secret = config.consumer_secret,
        access_token = config.access_token,
        access_token_secret = config.access_token_secret
    )

    tf = 0
    sum = 0
    for tweet in ts.search_tweets_iterable(tuo):
        #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        sum += 1
        if "title" in tweet['text'].lower():
            tf += 1
        if "fight" in tweet['text'].lower():
            tf += 1
        if "title fight" in tweet['text'].lower():
            tf += 1
        if "27" in tweet['text'].lower():
            tf += 1
        if "numb" in tweet['text'].lower():
            tf += 1
        if "shed" in tweet['text'].lower():
            tf += 1
        if "floral" in tweet['text'].lower():
            tf += 1
        if "society" in tweet['text'].lower():
            tf += 1
        if "skin" in tweet['text'].lower():
            tf += 1
        if "hyperview" in tweet['text'].lower():
            tf += 1
        if "ceiling fan" in tweet['text'].lower():
            tf += 1
        if "all away" in tweet['text'].lower():
            tf += 1
        if "kingston" in tweet['text'].lower():
            tf += 1
        if "hopeless" in tweet['text'].lower():
            tf += 1

    #print(sum)
    #print(tf)
    avg = tf / sum
    ans = float("{0:.2f}".format(avg))

    print ("@dylanilkowitz has tweeted about Title Fight in approximately " + str(ans) + "% of their tweets")

except TwitterSearchException as e: # catch all those ugly errors
    print(e)
