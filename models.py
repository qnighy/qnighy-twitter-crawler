#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from sqlalchemy import Column, Integer, BigInteger, String, DateTime, Boolean
from sqlalchemy import Float, Text, Unicode
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    coordinates_longitude = Column(Float)
    coordinates_latitude = Column(Float)
    created_at = Column(DateTime, nullable=False)
    # Note: this is perspectival (i.e. it depends on the api user)
    current_user_retweet = Column(BigInteger)
    entities = Column(Text, nullable=False)
    extended_entities = Column(Text)
    favorite_count = Column(Integer)
    # Note: this is perspectival (i.e. it depends on the api user)
    favorited = Column(Boolean)
    filter_level = Column(String(20))
    in_reply_to_screen_name = Column(String(40))
    in_reply_to_status_id = Column(BigInteger)
    in_reply_to_user_id = Column(BigInteger)
    lang = Column(String(20))
    place = Column(Text)
    possibly_sensitive = Column(Boolean)
    quoted_status_id = Column(BigInteger)
    scopes = Column(Text)
    retweet_count = Column(Integer, nullable=False)
    # Note: this is perspectival (i.e. it depends on the api user)
    retweeted = Column(Boolean, nullable=False)
    retweeted_status_id = Column(BigInteger)
    source = Column(Unicode(1024), nullable=False)
    source_url = Column(Unicode(1024), nullable=False)
    text = Column(Unicode(1024), nullable=False)
    truncated = Column(Boolean, nullable=False)
    user_id = Column(BigInteger, nullable=False)
    withheld_copyright = Column(Boolean)
    withheld_in_countries = Column(Text)
    withheld_scope = Column(String(40))

    @property
    def media(self):
        if self.extended_entities is not None:
            extended_entities = json.loads(self.extended_entities)
            if 'media' in extended_entities:
                return extended_entities['media']
        entities = json.loads(self.entities)
        if 'media' in entities:
            return entities['media']
        return []


class User(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    contributors_enabled = Column(Boolean)
    created_at = Column(DateTime, nullable=False)
    default_profile = Column(Boolean, nullable=False)
    default_profile_image = Column(Boolean, nullable=False)
    description = Column(Unicode(1024))
    # TODO: entities
    entities = Column(Text, nullable=False)
    favourites_count = Column(Integer, nullable=False)
    # Note: this is perspectival (i.e. it depends on the api user)
    follow_request_sent = Column(Boolean)
    followers_count = Column(Integer, nullable=False)
    friends_count = Column(Integer, nullable=False)
    geo_enabled = Column(Boolean, nullable=False)
    is_translator = Column(Boolean, nullable=False)
    lang = Column(String(20), nullable=False)
    listed_count = Column(Integer, nullable=False)
    location = Column(Unicode(1024))
    name = Column(Unicode(256), nullable=False)
    profile_background_color = Column(String(20), nullable=False)
    profile_background_image_url = Column(Text)
    profile_background_image_url_https = Column(Text)
    profile_background_tile = Column(Boolean, nullable=False)
    profile_banner_url = Column(Text)
    profile_image_url = Column(Text, nullable=False)
    profile_image_url_https = Column(Text, nullable=False)
    profile_link_color = Column(String(20), nullable=False)
    profile_sidebar_border_color = Column(String(20), nullable=False)
    profile_sidebar_fill_color = Column(String(20), nullable=False)
    profile_text_color = Column(String(20), nullable=False)
    profile_use_background_image = Column(Boolean, nullable=False)
    protected = Column(Boolean, nullable=False)
    screen_name = Column(String(40), nullable=False)
    show_all_inline_media = Column(Boolean)
    status_id = Column(BigInteger)
    statuses_count = Column(Integer, nullable=False)
    time_zone = Column(String(256))
    utc_offset = Column(Integer)
    verified = Column(Boolean, nullable=False)
    withheld_in_countries = Column(Text)
    withheld_scope = Column(String(40))


class Media(Base):
    __tablename__ = 'media'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    media_url = Column(Text, nullable=False)
    media_url_https = Column(Text, nullable=False)
    url = Column(Text, nullable=False)
    display_url = Column(Text, nullable=False)
    expanded_url = Column(Text, nullable=False)
    sizes = Column(Text, nullable=False)
    type = Column(String(40), nullable=False)
    indices_begin = Column(Integer, nullable=False)
    indices_end = Column(Integer, nullable=False)
    video_info = Column(Text)

    locally_available = Column(Boolean, nullable=False, default=False,
                               index=True)
