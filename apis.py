#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy
import twitter_config


auth = tweepy.OAuthHandler(twitter_config.consumer_key,
                           twitter_config.consumer_secret)
auth.set_access_token(twitter_config.access_token,
                      twitter_config.access_secret)
api = tweepy.API(auth)
