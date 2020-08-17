#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 18:18:55 2018

@author: mcarlebache
@project: CS109 Final Project; Twitter Bot Detector

These are essential interfacing function for the app.
"""
import twitter_credentials
import tweepy as tp
import re

def authenticate_twitter_app():
    # auth stuff
    consumer_key = twitter_credentials.CONSUMER_KEY 
    consumer_secret = twitter_credentials.CONSUMER_SECRET 
    auth = tp.OAuthHandler(consumer_key, consumer_secret)

    # token stuff
    access_token = twitter_credentials.ACCESS_TOKEN 
    access_token_secret = twitter_credentials.ACCESS_TOKEN_SECRET 
    auth.set_access_token(access_token, access_token_secret)

    return(auth)

def get_user_timeline_tweets(twitter_client, user_list, num_tweets):

    # this list will = tweeets & re-tweets (filter or tag re-tweets later)
    tweets = []

    for user in user_list:
        # This returns tweets & re-tweets, 10 at a time
        # We need to research more about getting larger volume back in time with max_id, since_id, etc.
        # I am hardcoding @realDonaldTrump...but we would put in variable from list of users
        for tweet in tp.Cursor(twitter_client.user_timeline, id=user).items(num_tweets):
            tweets.append(tweet)    

    return(tweets)
         
def produce_status_LoDs(statuses):
    
    tweet_LoD = []
    user_LoD = []
    for status in statuses:
        
        tweet_dict = {}
        user_dict = {}

        # tweet or retweet data 
        tweet_dict['user_id'] = status.author.id
        tweet_dict['created_at'] = status.created_at.isoformat()
        tweet_dict['id'] = status.id
        tweet_dict['id_str'] = status.id_str
        tweet_dict['text'] = status.text
        tweet_dict['source'] = status.source
        tweet_dict['truncated'] = status.truncated
 
        tweet_dict['retweet_count'] = status.retweet_count
        tweet_dict['favorite_count'] = status.favorite_count
        tweet_dict['lang'] = status.lang
        tweet_dict['is_tweet'] = ((re.search('RT', status.text) == None))
        ###Preimium API only?:  tweet_dict['retweeted_status'] = status.retweeted_status
        ###Preimium API only?:  tweet_dict['reply_count'] = status.reply_count
        ###Premium API only?:  tweet_dict['possibly_sensitive'] = status.possibly_sensitive
        
        tweet_LoD.append(tweet_dict)
        
        # user data
        user_dict['id'] = status.author.id
        user_dict['id_str'] = status.author.id_str
        user_dict['name'] = status.author.name
        user_dict['screen_name'] = status.author.screen_name
        user_dict['location'] = status.author.location
        user_dict['url'] = status.author.url
        user_dict['description'] = status.author.description
        user_dict['verified'] = status.author.verified
        user_dict['folowers_count'] = status.author.followers_count
        user_dict['listed_count'] = status.author.listed_count
        user_dict['favourites_count'] = status.author.favourites_count
        user_dict['statuses_count'] = status.author.statuses_count
        user_dict['created_at'] = status.author.created_at.isoformat()
        user_dict['utc_offset'] = status.author.utc_offset
        user_dict['time_zone'] = status.author.time_zone
        user_dict['lang'] = status.author.lang

        user_LoD.append(user_dict)

        
    return(tweet_LoD, user_LoD)