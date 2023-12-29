#!/usr/bin/env python3
# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 11.09.2023 10:53
@file: read_config_parma_registrar.py
@desc:
"""

if __name__ == '__main__':
    import sys


    def main(argv):
        program, *args = argv
        print(f"Script {program} arguments : {args}")
        return 0


    print("Execute error") if (main(sys.argv)) else print("Complete successful")