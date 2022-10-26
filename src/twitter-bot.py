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

# Limit Handler
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(400)

# Like Tweets with a certain keyword
def like_tweets(search_string, numberOfTweets):
    for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numberOfTweets):
        try:
            tweet.favorite()
            print('I liked that Tweet!')
        except tweepy.errors.TweepyException as err:
            print(err)
        except StopIteration:
            break

# TODO: follow people back
def follow_back():
    pass      
    
# TODO: retweet tweets mentioned in
def retweet():
    pass

# TODO: like tweets mentioned in

if __name__ == '__main__':

    # user = api.get_user(screen_name='twitter')
    search_string = ['DataScience']
    numberOfTweets = 6

    like_tweets(search_string, numberOfTweets)

    # set these to always run:
    retweet()
    follow_back()
