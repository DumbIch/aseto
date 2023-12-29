# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 23.08.2023 10:07
@file: search-startup-event.py
@desc:
"""


def main(argv):
    program, *args = argv
    print(f"Script {program} arguments : {args}")
    return 0


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
