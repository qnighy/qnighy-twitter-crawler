#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, BigInteger, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Tweet(Base):
    __tablename__ = 'tweets'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    coordinates = Column(String(256))
    created_at = Column(DateTime, nullable=False)
    # Note: this is perspectival (i.e. it depends on the api user)
    current_user_retweet = Column(BigInteger)
    # TODO: entities
    entities = Column(String(1024), nullable=False)
    favorite_count = Column(Integer)
    # Note: this is perspectival (i.e. it depends on the api user)
    favorited = Column(Boolean)
    filter_level = Column(String(20))
    in_reply_to_screen_name = Column(String(40))
    in_reply_to_status_id = Column(BigInteger)
    in_reply_to_user_id = Column(BigInteger)
    lang = Column(String(20))
    place_id = Column(Integer)
    possibly_sensitive = Column(Boolean)
    quoted_status_id = Column(BigInteger)
    scopes = Column(String(1024))
    retweet_count = Column(Integer, nullable=False)
    # Note: this is perspectival (i.e. it depends on the api user)
    retweeted = Column(Boolean, nullable=False)
    retweeted_status_id = Column(BigInteger)
    source = Column(String(1024), nullable=False)
    source_url = Column(String(1024), nullable=False)
    text = Column(String(1024), nullable=False)
    truncated = Column(Boolean, nullable=False)
    user_id = Column(Integer, nullable=False)
    withheld_copyright = Column(Boolean, nullable=False)
    withheld_in_countries = Column(String(1024))
    withheld_scope = Column(String(40))
