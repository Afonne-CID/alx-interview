#!/usr/bin/python3
'''N queens puzzle module
'''
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except BaseException:
        print('N must be a number')
        sys.exit(1)
    if size < 4:
        print('N must be at least 4')
        sys.exit(1)
