#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 22:45:11 2018

@author: andrewcaide

bot list pulled from:
    https://www.nbcnews.com/tech/social-media/now-available-more-200-000-deleted-russian-troll-tweets-n844731
"""
import pandas as pd

# Find these locally! 
bots = pd.read_csv('Input Files/users.csv')
tweets = pd.read_csv('Input Files/tweets.csv')


def produce_bot_LoDs(bots, tweets):
    '''
    Read in dataframe of bots and their tweets. Organize them according to Mark's format. 
    
    Args: 
        dataframes - Bots, Tweets
    
    Returns: 
        Cleaned dataframe, with an extra column: 'Bot_Status' = True
    '''
    # Fix tweets:
    tweet_colnames = ['created_at','favorite_count','id','id_str','is_tweet','lang','retweet_count',
                 'source','text','truncated','user_id', 'hashtags']
    
    # Ask mark to see if he can pull out hashtags from his tweets!!
    tweets['truncated'] = False
    tweets['is_tweet'] = tweets['text'].apply(lambda x: False if str(x).find('RT') == -1 else True)
    tweets = tweets.rename(columns={'tweet_id': 'id'}) 
    tweets['id_str'] = str(tweets['id'])
    tweets['lang'] = 'en'
    
    tweet_output = tweets[tweet_colnames]
    
    # Fix users:
    user_colnames = ['created_at','description','favourites_count','followers_count','friends_count','id',
                      'lang','listed_count','location','name','screen_name','statuses_count',
                      'time_zone','verified']
    
    bots_output = bots[user_colnames]
    return(bots_output, tweet_output)


bots_Clean, tweets_Clean = produce_bot_LoDs(bots, tweets)

bots_Clean.to_csv('Input Files/bot_handles.csv')
tweets_Clean.to_csv('Input Files/bot_tweets.csv')
