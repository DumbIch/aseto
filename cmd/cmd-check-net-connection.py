#!/usr/bin/env python3
# encoding: utf-8
"""
@author: DumDumbIch
@contact: dumdumbich@mail.ru
@time: 13.09.2023 09:50
@file: cmd-check-net-connection.py
@desc:
"""

import psutil

if __name__ == '__main__':
    import sys


    def main(argv):
        program, *args = argv
        print(f"Script {program} arguments : {args}")
        net_stats = psutil.net_if_stats()
        # print(net_stats)
        for interface, stats in net_stats.items():
            print(f"{interface:<20}")
            for value in stats:
                print(f"{value:>30}")

        return 0


    main(sys.argv)
    # print("Execute error") if (main(sys.argv)) else print("Complete successful")
