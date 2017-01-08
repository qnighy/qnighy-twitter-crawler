#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler


def configure_logging():
    logFormatter = logging.Formatter(
        "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger('')
    rootLogger.setLevel(logging.DEBUG)

    fileHandler = RotatingFileHandler("crawl.log", maxBytes=(1048576*5))
    fileHandler.setFormatter(logFormatter)
    fileHandler.setLevel(logging.WARNING)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(logging.INFO)
    rootLogger.addHandler(consoleHandler)
