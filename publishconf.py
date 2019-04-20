#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://outde.xyz'
SITELOGO = SITEURL + '/img/logo.svg'
FAVICON = SITEURL + '/img/favicon.ico'
ABS_SITEURL = SITEURL
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
USE_UTTERANCES = False
USE_TALKYARD = True
