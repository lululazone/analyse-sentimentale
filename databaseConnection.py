# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:11:36 2022

@author: Lucas Girard
"""


import os
import tweepy
from dotenv import load_dotenv

API_KEY="i0KW06q2EaI0BrF0kIhnav7p9"
API_KEY_SECRET="r3fLg1MCR3FnZRtQy1dkbzzLhg9nLL4YQGs3K9I9qHy2lZ4v1X"
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAMJOjgEAAAAAkNjeqmkvNxVSfNZlh75tfi35864%3D2d7PR9fkmxGcngfNr8KFN46fUMaAiuI3xUI0KkYfiPspuo2p11"
ACCESS_TOKEN="1589912574698594304-ZTfXvKQkmlrj1Gts0YkAVTMbzJkYRl"
ACCESS_TOKEN_SECRET="ReJBMhKQjAC3CbXOt3JDwSrauptvxwdMXYhkInVdfMLZS"

#Fetch twitter api using tweepy
consumer_key = API_KEY
consumer_secret = API_KEY_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET




auth = tweepy.OAuth1UserHandler(
  consumer_key, 
  consumer_secret, 
  access_token, 
  access_token_secret
)

api = tweepy.API(auth)

extracted_tweets = []

for status in tweepy.Cursor(api.search_tweets, 
                            "Ukraine", 
                            lang="en",
                            count=100).items(250):
    extracted_tweets.append(status)
    
print(status)