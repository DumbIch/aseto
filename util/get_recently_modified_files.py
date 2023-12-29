# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 24.08.2023 14:21
@file: get_recently_modified_files.py
@desc:
"""

import os
import time


def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)


if __name__ == '__main__':
    import sys

    # if len(sys.argv) != 3:
    #     print('Usage: {} dir seconds'.format(sys.argv[0]))
    #     raise SystemExit(1)
    # modified_within(sys.argv[1], float(sys.argv[2]))
