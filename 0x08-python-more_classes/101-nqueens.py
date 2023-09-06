#!/usr/bin/python3
import sys


def nqueens(n):
    solutions = []

    def backtrack(r):
        if r == n:
            solutions.append(list(solution))
            return

        for c in range(n):
            if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            cols.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            solution.append([r, c])

            backtrack(r + 1)

            cols.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            solution.pop()

    cols = set()
    pos_diag = set()
    neg_diag = set()

    solution = []
    backtrack(0)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    n = 0
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solutions = nqueens(n)
    for sol in solutions:
        print(sol)
