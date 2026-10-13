#!/usr/bin/python3
"""N queens"""
import sys


def secured(columns, line, column):
    """Return True when queen is safe"""
    for row in range(line):
        c = columns[row]
        if c == column or abs(c - column) == line - row:
            return False
    return True


def solve(n, line, columns, solutions):
    """Place one queen per line and revert back when line is blocked"""
    if line == n:
        solutions.append([[row, columns[row]] for row in range(n)])
        return
    for column in range(n):
        if secured(columns, line, column):
            columns.append(column)
            solve(n, line + 1, columns, solutions)
            columns.pop()


def nqueens(n):
    """Return all solutions"""
    solutions = []
    solve(n, 0, [], solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    for solution in nqueens(n):
        print(solution)
