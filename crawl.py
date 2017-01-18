#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging_config


logging_config.configure_logging()

if __name__ == '__main__':
    import sys
    import qnighy_twitter_crawler
    sys.exit(qnighy_twitter_crawler.main())
