#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import models


# engine = create_engine('sqlite:///db.sqlite', echo=True)
engine = create_engine('sqlite:///db.sqlite', echo=False)
models.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
