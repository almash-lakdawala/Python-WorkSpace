
def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    def is_safe(row, col):
        # Check the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1

                if solve(row + 1):
                    return True

                board[row][col] = 0

        return False

    if solve(0):
        return board

    return None


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

n = 4
solution = solve_n_queens(n)

if solution:
    print("N-Queens Solution:")
    for row in solution:
        print(*row)
else:
    print("No Solution Exists")
