#!/usr/bin/env python3
# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 11.09.2023 09:24
@file: cmd-hello.py
@desc:
"""
from registrar.config.parma import read_config_parma_registrar

if __name__ == '__main__':
    import sys


    def main(argv):
        program, *args = argv
        print(f"Script {program} arguments : {args}")
        read_config_parma_registrar
        return 0


    print("Execute error") if (main(sys.argv)) else print("Complete successful")
