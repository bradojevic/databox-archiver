#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os
import time
import pytz
import datetime
import zipfile
import util
import settings
import config


def pass_gen(interval):
    while True:
        time_start = time.time()
        yield
        time_left = interval - (time.time() - time_start)
        if time_left > 0:
            time.sleep(time_left)


def main():
    sys.stderr.write('.')
    sys.stderr.flush()
    ts = datetime.datetime.utcnow().replace(tzinfo=pytz.timezone('UTC'))
    for_date = ts.strftime('%Y-%m-%d')
    zip_file = os.path.join(settings.DATABOX_OUT, '{0}.zip'.format(for_date, ))
    if not os.path.isfile(zip_file):
        print >> sys.stderr, 'create zip file'
        zipfile.ZipFile(zip_file, 'w').close()
    with zipfile.ZipFile(zip_file, 'a') as zip_handle:
        json_files = util.walk_databox(
            settings.DATABOX_IN,
            max_count=settings.FETCH_COUNT,
            file_type='.json',
            contains=for_date
        )
        for json_file in json_files:
            print >> sys.stderr, json_file
            zip_handle.write(
                json_file, os.path.basename(json_file), zipfile.ZIP_DEFLATED
            )
            os.system('rm %s' % (json_file, ))


if __name__ == "__main__":
    config.load()
    for _ in pass_gen(settings.FETCH_INTERVAL):
        config.reload()
        main()
