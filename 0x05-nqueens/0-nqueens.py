#!/usr/bin/python3
import sys

def issafe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solvenqueens(n):
    def solve(board, row):
        if row == n:
            solutions.append(list(enumerate(board)))
            return

        for col in range(n):
            if issafe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1

    solutions = []
    board = [-1] * n
    solve(board, 0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

def main():
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

    solutions = solve_n_queens(n)
    print_solutions(solutions)

if __name == "__main":
    main()
