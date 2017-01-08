#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import tweepy

try:
    with open('consumer-key.json', 'r') as f:
        consumer = json.load(f)
except FileNotFoundError as e:
    consumer_key = input('Consumer key: ')
    consumer_secret = input('Consumer secret: ')
    consumer = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret}
    with open('consumer-key.json', 'w') as f:
        json.dump(consumer, f)
    print('Successfully recorded to consumer-key.json')

auth = tweepy.OAuthHandler(consumer['consumer_key'],
                           consumer['consumer_secret'])

try:
    with open('access-token.json', 'r') as f:
        access = json.load(f)
    auth.set_access_token(access['access_token'],
                          access['access_secret'])
except FileNotFoundError as e:
    print("Please access: %s" % auth.get_authorization_url())
    verifier = input('Verifier: ')
    auth.get_access_token(verifier)
    access = {
        'access_token': auth.access_token,
        'access_secret': auth.access_token_secret}
    with open('access-token.json', 'w') as f:
        json.dump(access, f)
    print('Successfully recorded to access-token.json')

api = tweepy.API(auth)
