#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 18:21:54 2018

@author: acaide

"""
# Essentials only
import pandas as pd
import tweepy as tp
import re
from twitter_interfacing import *

# Items to set
user_list = ['@realDonaldTrump', '@secupp', '@ChairmanKimNK', '@ThePSF']
num_tweets = 100




# Setup twitter client to read data from specified user
auth = ti.authenticate_twitter_app()
twitter_client = tp.API(auth)

# Get fixed number of tweets and put in results
statuses = get_user_timeline_tweets(twitter_client,user_list, num_tweets)

# Create list to write to json file like we did in HW1
tweet_LoD, user_LoD = produce_status_LoDs(statuses)

# Put in DF in case you skip the out/in via json below
tweet_df = pd.DataFrame(tweet_LoD)
user_df = pd.DataFrame(user_LoD)