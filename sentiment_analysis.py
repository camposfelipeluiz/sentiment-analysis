import tweepy
from textblob import TextBlob
import pandas as pd
import numpy as np

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

list_= []
public_tweets = tweepy.Cursor(api.search, tweet_mode='extended', q='trump -filter:retweets', 
                              lang='en', since = '2020-01-01').items(1000)
for tweet in public_tweets:
    analysis = TextBlob(tweet.full_text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    retweet_count = tweet.retweet_count
    if (retweet_count > 0) and (polarity != 0 or subjectivity != 0):
        dict_ = {'user_name': tweet.user.name, 'screen_name': tweet.user.screen_name, 
                 'tweet': tweet.full_text, 'date': tweet.created_at, 'polarity': polarity, 'subjectivity': subjectivity, 'favorite_count': tweet.favorite_count,
                 'retweet_count': str(tweet.retweet_count)}
        list_.append(dict_)
df = pd.DataFrame(list_)

df['date'] = df['date'].apply(lambda x:x.date())
df['favorite_count'] = df['favorite_count'].astype(int)
df['retweet_count'] = df['retweet_count'].astype(int)

df['rts/likes'] = df['retweet_count'] / df['favorite_count']
df['impact'] = df['polarity'] * df['retweet_count']

df['impact'] = df['impact'].round(2)
df['polarity'] = df['polarity'].round(2)
df['subjectivity'] = df['subjectivity'].round(2)
df['rts/likes'] = df['rts/likes'].round(2)

bins = np.linspace(min(df['polarity']), max(df['polarity']), 5)
group_names = ['very negative', 'negative', 'positive', 'very positive']
df['polarity_group'] = pd.cut(df['polarity'], bins, labels=group_names, include_lowest=True)
bins1 = np.linspace(min(df['subjectivity']), max(df['subjectivity']), 4)
group_names1 = ['descriptive', 'subjective', 'very subjective']
df['subjectivity_group'] = pd.cut(df['subjectivity'], bins1, labels=group_names1, include_lowest=True)

