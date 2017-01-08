#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models


engine = create_engine('sqlite:///db.sqlite', echo=True)
models.Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
