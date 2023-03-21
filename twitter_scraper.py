# pip install pandas
# pip install tweepy


from datetime import time
import pandas as pd
import tweepy
from tweepy import OAuthHandler

consumer_key = "uJUfRK2GdxfdqOyo43RWmkCbd"

consumer_secret = "sK6WNrfYZKBhFKXyneWv6URESMwq7GwcLbKQER1D7B50WSkwdj"
access_key = "2551921020-ZkWwPqeqRgtJtESKnd5nnAWbVa12oK56WT1zBEB"
access_secret = "PIKiOs0eewDKqsaKiPqQ99L7lrYCqa9clrqm5QMrqrX0m"

#Pass in our twitter API authentication key
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

username=input("Enter the Username :")
# username= "imVkohli"
no_of_tweets =5


try:
    #The number of tweets we want to retrieved from the user
    tweets = api.user_timeline(screen_name=username, count=no_of_tweets)
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.created_at, tweet.favorite_count,tweet.source,  tweet.text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))
    time.sleep(3)

tweets_df.head(5)