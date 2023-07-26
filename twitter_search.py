# Importing the libraries
import configparser
import tweepy

# Read the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Read the values
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Import Tweepy
import tweepy

# Authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

keyword = 'cryptocurrencies'
limit=300

tweets = tweepy.Cursor(api.search_tweets, q=keyword, tweet_mode='extended').items(limit)

hashtag = '#luna2'
limit=300

tweets = tweepy.Cursor(api.search_tweets, q=hashtag, tweet_mode='extended').items(limit)