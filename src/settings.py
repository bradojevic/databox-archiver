# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CORE_CONFIG = os.path.join(BASE_DIR, 'config', 'core.yaml')
CORE_CONFIG_RELOAD_INTERVAL = 120  # s

FETCH_COUNT = 400
FETCH_INTERVAL = 10  # s

DATABOX_IN = os.path.join(BASE_DIR, 'data')
DATABOX_OUT = os.path.join(BASE_DIR, 'data')
