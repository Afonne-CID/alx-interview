#!/usr/bin/python3
""" A script that reads stdin line by line and computes metrics
"""
import sys


if __name__ == '__main__':
    filesize, cnt = 0, 0
    stats = {k: 0 for k in [
        "200", "301", "400", "401", "403", "404", "405", "500"
    ]}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            cnt += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if cnt % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
