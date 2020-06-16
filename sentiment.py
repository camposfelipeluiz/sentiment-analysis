def sentiment(query, since, until, items):
    
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
        analysis = TextBlob(tweet.full_text)
        polarity = analysis.sentiment.polarity
        subjectivity = analysis.sentiment.subjectivity
        retweet_count = tweet.retweet_count
        if (retweet_count > 0) and (polarity != 0 or subjectivity != 0):
            dict_ = {'screen_name': tweet.user.screen_name, 
                 'tweet': tweet.full_text, 'date': tweet.created_at, 'polarity': polarity, 'subjectivity': subjectivity, 'favorite_count': tweet.favorite_count,
                 'retweet_count': tweet.retweet_count}
            list_.append(dict_)
    df = pd.DataFrame(list_)
    
    df['pos'] = df[df['polarity'] > 0]['polarity']
    df['neg'] = df[df['polarity'] < 0]['polarity']
    
    df['date'] = df['date'].apply(lambda x:x.date())
    df['rts/likes'] = df['retweet_count'] / df['favorite_count']
    
    
    return df
