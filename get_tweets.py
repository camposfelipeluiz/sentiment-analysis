import pandas as pd
import tweepy


def get_tweets(query, since, until, items):
    
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    
    
    list_= []
    public_tweets = tweepy.Cursor(api.search, tweet_mode='extended', q=query, 
                              lang='en', since=since, until=until).items(items)
    
    for tweet in public_tweets:

        dict_ = {'screen_name': tweet.user.screen_name, 
                 'tweet': tweet.full_text, 'date': tweet.created_at, 'favorite_count': tweet.favorite_count,
                 'retweet_count': tweet.retweet_count}
            
        list_.append(dict_)
            
    df = pd.DataFrame(list_)
    
    
    return df
    
    df = get_tweets()
