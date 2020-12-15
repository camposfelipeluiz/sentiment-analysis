import tweepy
import pandas as pd

def get_id(*users):

    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    usuarios = []
    for user in users:
        user = api.get_user(str(user))._json
        usuarios.append(user)
        k = len(usuarios)
        
        for k in range(0,k):
            nome = usuarios[k]['screen_name']
            ID = usuarios[k]['id']
            
        print(f'{nome}: {ID}')
