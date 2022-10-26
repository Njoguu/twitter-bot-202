import tweepy
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Authentication
auth = tweepy.OAuth1UserHandler(
    os.getenv('API_KEY'),
    os.getenv('API_KEY_SECRET'),
    os.getenv('ACCESS_TOKEN'),
    os.getenv('ACCESS_TOKEN_SECRET')
)
api = tweepy.API(auth)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'Data Science'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that Tweet!')
    except tweepy.errors.TweepyException as err:
        print(err)
    except StopIteration:
        break











# TODO Generous Bot
