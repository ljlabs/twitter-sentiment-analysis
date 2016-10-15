import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
query = 'trump'
max_tweets = 100
public_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    print('"' + str(tweet.text) + '", ' + str(analysis.sentiment.polarity) + ', ' + str(analysis.sentiment.subjectivity))