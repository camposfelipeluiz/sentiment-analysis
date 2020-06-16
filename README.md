# twitter_monitor

This is a repository developed to make it easier to extract and analyze twitter data. All the codes use tweepy and pandas. 

File sentiment.py uses TextBlob to analyze sentiment -- polarity and subjectivity. It gets some inputs (query, since, until, items) and returns tweets and stats in a pandas dataframe.

File get_user_tweets.py get inputs (user, items) and returns a pandas dataframe with tweets by that user, and also twitter stats. 

File followers_count.py gets as an input one or several usernames and return their number of followers. Just a little and simple code for something i had to manually every couple of days at work.

File get_ids.py does pretty much the same the one above, but it returns user'd ID. 
