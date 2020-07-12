import tweepy
import pandas as pd

def get_user_tweets(user, items=100):
    
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    list_= []
    public_tweets = tweepy.Cursor(api.user_timeline, tweet_mode='extended', screen_name=user).items(items)
    for tweet in public_tweets:
        if 'RT @' not in tweet.full_text:
            dict_ = {'screen_name': tweet.user.screen_name, 'tweet': tweet.full_text, 'created_at': tweet.created_at, 'favorite_count': tweet.favorite_count,  'retweet_count': tweet.retweet_count}
            list_.append(dict_)
    df = pd.DataFrame(list_)
    df['date'] = df['created_at'].apply(lambda x:x.date())
    df['time'] = df['created_at'].apply(lambda x:x.time())
    df['created_at'] = df['created_at'].apply(lambda x:x.strftime('%Y-%m-%d %H:%M'))
    df['rts/likes'] = df['retweet_count']/df['favorite_count']
    df['rts/likes'] = df['rts/likes'].round(2)
    
    return df
    
