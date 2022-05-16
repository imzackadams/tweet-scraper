import csv
import tweepy
import keys
import pandas as pd
import sys



# authenticate


auth = tweepy.OAuthHandler(keys.api_key, keys.api_key_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('tweets.csv', 'a')
csvWriter = csv.writer(csvFile)

search_words = input("What is the tweet keyword do you want to search?: ")  # enter your words
new_search = search_words + " -filter:retweets"

for tweet in tweepy.Cursor(api.search_tweets, q=new_search, count=100,
                           lang="en",
                           since_id=0).items(200):
    csvWriter.writerow([tweet.text.encode()
                        ])

df = pd.read_csv("tweets.csv")



