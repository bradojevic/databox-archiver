# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os


def walk_databox(directory, max_count=0, file_type=None, contains=None):
    count = 0
    for root, directories, filenames in os.walk(directory):
        for filename in filenames:
            if max_count > 0 and count >= max_count:
                raise StopIteration()
            if file_type is not None:
                basename, extension = os.path.splitext(filename)
                if extension != file_type:
                    continue
            if contains and os.path.basename(filename).find(contains) == -1:
                continue
            yield os.path.join(directory, filename)
            count += 1
        raise StopIteration()
