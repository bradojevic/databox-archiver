# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import yaml
import settings
import datetime

_last_loaded_ts = None


def _now():
    return datetime.datetime.utcnow()


def _read_yaml(path):
    with open(path, 'r') as file:
        return yaml.load(file)


def load():
    global _last_loaded_ts
    print >> sys.stderr, 'loading configuration ..'
    try:
        for key, value in _read_yaml(settings.CORE_CONFIG).items():
            setattr(settings, key.upper(), value)
            print >> sys.stderr, key.upper(), value
        _last_loaded_ts = _now()
    except yaml.YAMLError as exc:
        print >> sys.stderr, 'error loading %s' % settings.CORE_CONFIG
        print >> sys.stderr, exc


def reload():
    now = _now()
    interval = datetime.timedelta(
        seconds=settings.CORE_CONFIG_RELOAD_INTERVAL
    )
    if not _last_loaded_ts or now > (_last_loaded_ts + interval):
        load()
