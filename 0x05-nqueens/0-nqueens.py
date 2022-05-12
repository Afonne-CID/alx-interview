#!/usr/bin/python3
'''N queens puzzle module
'''
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except BaseException:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    col = set()
    posDiag = set()
    negDiag = set()
    board = [[0 for _ in range(n)] for _ in range(n)]

    def solveNQueens(r):
        if r == n:
            bCopy = [row for row in board]
            printNQueens(bCopy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = 1

            solveNQueens(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = 0

    def printNQueens(res):
        output = []
        for i in range(n):
            for j in range(n):
                if res[i][j] == 1:
                    output.append([i, j])
        print(output)
        output.clear()
    solveNQueens(0)
