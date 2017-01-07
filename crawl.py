#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tweepy
from sqlalchemy import create_engine
from sqlalchemy.orm import load_only, sessionmaker
import models
import twitter_config


auth = tweepy.OAuthHandler(twitter_config.consumer_key,
                           twitter_config.consumer_secret)
auth.set_access_token(twitter_config.access_token,
                      twitter_config.access_secret)
api = tweepy.API(auth)

engine = create_engine('sqlite:///db.sqlite', echo=True)
models.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def update_tweet_info(session, tw):
    tw_db = session.query(models.Tweet)\
        .options(load_only("id"))\
        .filter_by(id=tw.id)\
        .one_or_none()
    if tw_db is None:
        tw_db = models.Tweet(id=tw.id)
        session.add(tw_db)
    # TODO: tw.coordinates
    # # coordinates = Column(String(256))
    # tw_db.coordinates = tw.coordinates
    tw_db.created_at = tw.created_at
    if hasattr(tw, 'current_user_retweet'):
        tw_db.current_user_retweet = tw.current_user_retweet['id']
    else:
        tw_db.current_user_retweet = None
    # TODO: tw.entities
    # # entities = Column(String(1024))
    tw_db.entities = "{}"
    # tw_db.entities = tw.entities
    tw_db.favorite_count = tw.favorite_count
    tw_db.favorited = tw.favorited
    tw_db.filter_level = getattr(tw, 'filter_level', None)
    tw_db.in_reply_to_screen_name = tw.in_reply_to_screen_name
    tw_db.in_reply_to_status_id = tw.in_reply_to_status_id
    tw_db.in_reply_to_user_id = tw.in_reply_to_user_id
    tw_db.lang = tw.lang
    # TODO: tw.place
    # tw_db.place_id = tw.place['id']
    tw_db.possibly_sensitive = getattr(tw, 'possibly_sensitive', None)
    # TODO: tw.quoted_status
    tw_db.quoted_status_id = getattr(tw, 'quoted_status_id', None)
    # # scopes = Column(String(1024))
    # tw_db.scopes = getattr(tw, 'scopes', None)
    tw_db.retweet_count = tw.retweet_count
    tw_db.retweeted = tw.retweeted
    # TODO: tw.retweeted_status_id
    if hasattr(tw, 'retweeted_status'):
        tw_db.retweeted_status_id = tw.retweeted_status.id
    else:
        tw_db.retweeted_status_id = None
    tw_db.source = tw.source
    tw_db.source_url = tw.source_url
    tw_db.text = tw.text
    tw_db.truncated = tw.truncated
    tw_db.user_id = tw.user.id
    if hasattr(tw, 'withheld_copyright'):
        tw_db.withheld_copyright = tw.withheld_copyright
    else:
        tw_db.withheld_copyright = False
    if hasattr(tw, 'withheld_in_countries'):
        tw_db.withheld_in_countries = tw.withheld_in_countries
    else:
        tw_db.withheld_in_countries = None
    if hasattr(tw, 'withheld_scope'):
        tw_db.withheld_scope = tw.withheld_scope
    else:
        tw_db.withheld_scope = None


def main():
    session = Session()
    tw = api.get_status(817645036309356544)
    update_tweet_info(session, tw)
    session.commit()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
