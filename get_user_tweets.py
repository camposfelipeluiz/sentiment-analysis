import tweepy
import pandas as pd

def get_user_tweets(user1, user2,  user1_items=100, user2_items=100):
    
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    list1= []
    public_tweets1 = tweepy.Cursor(api.user_timeline, tweet_mode='extended', screen_name=user1).items(user1_items)
    for tweet in public_tweets1:
        if 'RT @' not in tweet.full_text:
            dict1 = {'screen_name': tweet.user.screen_name, 'tweet': tweet.full_text, 'created_at': tweet.created_at, 'favorite_count': tweet.favorite_count,  'retweet_count': tweet.retweet_count}
            list1.append(dict1)
    df1 = pd.DataFrame(list1)
    df1['date'] = df1['created_at'].apply(lambda x:x.date())
    df1['time'] = df1['created_at'].apply(lambda x:x.time())
    df1['created_at'] = df1['created_at'].apply(lambda x:x.strftime('%Y-%m-%d %H:%M'))
    df1['rts/likes'] = df1['retweet_count']/df1['favorite_count']
    df1['rts/likes'] = df1['rts/likes'].round(2)
    
    list2 = []
    public_tweets2 = tweepy.Cursor(api.user_timeline, tweet_mode='extended', screen_name=user2).items(user2_items)
    for tweet in public_tweets2:
        if 'RT @' not in tweet.full_text:
            dict2 = {'screen_name': tweet.user.screen_name, 'tweet': tweet.full_text, 'created_at': tweet.created_at, 'favorite_count': tweet.favorite_count,  'retweet_count': tweet.retweet_count}
            list2.append(dict2)
    df2 = pd.DataFrame(list2)
    df2['date'] = df2['created_at'].apply(lambda x:x.date())
    df2['time'] = df2['created_at'].apply(lambda x:x.time())
    df2['created_at'] = df2['created_at'].apply(lambda x:x.strftime('%Y-%m-%d %H:%M'))
    df2['rts/likes'] = df2['retweet_count']/df2['favorite_count']
    df2['rts/likes'] = df2['rts/likes'].round(2)
    
    df = pd.concat([df1, df2])
    
    return df

df = get_user_tweets()
