import config, argparse, twitter


def __main__():
    api = twitter.Api(consumer_key = config.consumer_key,
                      consumer_secret = config.consumer_secret,
                      access_token_key = config.access_token_key,
                      access_token_secret = config.access_token_secret)

    parser = argparse.ArgumentParser(description='tweet a lot')

    parser.add_argument('-f',
                        nargs = 1, type=str,
                        metavar='<input_file>',
                        help = 'file which containts text to tweet',
                        required = True)

    args = parser.parse_args()
