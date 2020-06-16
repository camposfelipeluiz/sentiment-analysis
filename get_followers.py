import tweepy
import pandas as pd

def followers_count(*users):

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    screen_names = []
    for user in users:
        user = api.get_user(str(user))._json
        screen_names.append(user)
        
        k = len(screen_names)
        for k in range(0,k):
            name = usuarios[k]['screen_name']
            followers = usuarios[k]['followers_count']
        
        print(f'{nome}: {followers}')
