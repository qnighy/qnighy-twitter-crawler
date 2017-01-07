#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
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
    update_user_info(session, tw.user)
    if hasattr(tw, 'quoted_status'):
        quoted_status = tw.quoted_status
        if type(quoted_status) == dict:
            quoted_status = tweepy.Status.parse(api, quoted_status)
        update_tweet_info(session, quoted_status)
    if hasattr(tw, 'retweeted_status'):
        update_tweet_info(session, tw.retweeted_status)

    tw_db = session.query(models.Tweet)\
        .options(load_only("id"))\
        .filter_by(id=tw.id)\
        .one_or_none()
    if tw_db is None:
        tw_db = models.Tweet(id=tw.id)
        session.add(tw_db)
    if tw.coordinates is not None:
        tw_db.coordinates_longitude = tw.coordinates['coordinates'][0]
        tw_db.coordinates_latitude = tw.coordinates['coordinates'][1]
    else:
        tw_db.coordinates_longitude = None
        tw_db.coordinates_latitude = None
    tw_db.created_at = tw.created_at
    if hasattr(tw, 'current_user_retweet'):
        tw_db.current_user_retweet = tw.current_user_retweet['id']
    else:
        tw_db.current_user_retweet = None
    tw_db.entities = json.dumps(tw.entities)
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
    tw_db.quoted_status_id = getattr(tw, 'quoted_status_id', None)
    if hasattr(tw, 'scopes'):
        tw_db.scopes = json.dumps(tw.scopes)
    else:
        tw_db.scopes = None
    tw_db.retweet_count = tw.retweet_count
    tw_db.retweeted = tw.retweeted
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
        tw_db.withheld_copyright = None
    if hasattr(tw, 'withheld_in_countries'):
        tw_db.withheld_in_countries = tw.withheld_in_countries
    else:
        tw_db.withheld_in_countries = None
    if hasattr(tw, 'withheld_scope'):
        tw_db.withheld_scope = tw.withheld_scope
    else:
        tw_db.withheld_scope = None
    session.commit()


def update_user_info(session, u):
    if hasattr(u, 'status') and u.status is not None:
        update_tweet_info(session, u.status)

    u_db = session.query(models.User)\
        .options(load_only("id"))\
        .filter_by(id=u.id)\
        .one_or_none()
    if u_db is None:
        u_db = models.User(id=u.id)
        session.add(u_db)
    u_db.created_at = u.created_at
    u_db.default_profile = u.default_profile
    u_db.default_profile_image = u.default_profile_image
    u_db.description = u.description
    u_db.entities = json.dumps(u.entities)
    u_db.favourites_count = u.favourites_count
    u_db.follow_request_sent = u.follow_request_sent
    u_db.followers_count = u.followers_count
    u_db.friends_count = u.friends_count
    u_db.geo_enabled = u.geo_enabled
    u_db.is_translator = u.is_translator
    u_db.lang = u.lang
    u_db.listed_count = u.listed_count
    u_db.location = u.location
    u_db.name = u.name
    u_db.profile_background_color = u.profile_background_color
    u_db.profile_background_image_url = u.profile_background_image_url
    u_db.profile_background_image_url_https = \
        u.profile_background_image_url_https
    u_db.profile_background_tile = u.profile_background_tile
    u_db.profile_banner_url = getattr(u, 'profile_banner_url', None)
    u_db.profile_image_url = u.profile_image_url
    u_db.profile_image_url_https = u.profile_image_url_https
    u_db.profile_link_color = u.profile_link_color
    u_db.profile_sidebar_border_color = u.profile_sidebar_border_color
    u_db.profile_sidebar_fill_color = u.profile_sidebar_fill_color
    u_db.profile_text_color = u.profile_text_color
    u_db.profile_use_background_image = u.profile_use_background_image
    u_db.protected = u.protected
    u_db.screen_name = u.screen_name
    u_db.show_all_inline_media = getattr(u, 'show_all_inline_media', None)
    if hasattr(u, 'status') and u.status is not None:
        u_db.status_id = u.status.id
    else:
        u_db.status_id = None
    u_db.statuses_count = u.statuses_count
    u_db.time_zone = u.time_zone
    u_db.url = u.url
    u_db.utc_offset = u.utc_offset
    u_db.verified = u.verified
    u_db.withheld_in_countries = getattr(u, 'withheld_in_countries', None)
    u_db.withheld_scope = getattr(u, 'withheld_scope', None)
    session.commit()


def main():
    session = Session()
    for status_id in [
            817645036309356544,
            817666240042803201,
            817667861032243200,
            817673828721565696,
            817369529974079488,
            817674606555242496,
            817664008584990720,
            817524535960313856,
            817524185597550593,
            817523673665941505,
            817551496266977280,
            817560519003357184,
            817671363578056704,
            815572784747159552,
            817467641128361985,
            786533768840433664,
            ]:
        tw = api.get_status(status_id)
        update_tweet_info(session, tw)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
