# N-Queens with a pre-placed first queen (row, column are 1-based)
n = int(input("Enter N: "))
r, c = map(int, input("First queen row and column: ").split())
board = [[0] * n for _ in range(n)]
board[r-1][c-1] = 1

def safe(row, col):
    for i in range(row):
        if board[i][col]:
            return False
        if col-(row-i) >= 0 and board[i][col-(row-i)]:
            return False
        if col+(row-i) < n and board[i][col+(row-i)]:
            return False
    return True

def solve(row):
    if row == n:
        return True
    if row == r-1:              # keep the given queen fixed
        return solve(row+1)
    for col in range(n):
        if safe(row, col):
            board[row][col] = 1
            if solve(row+1):
                return True
            board[row][col] = 0
    return False

if solve(0):
    for row in board:
        print(*row)
else:
    print("No solution for this first-queen position.")
