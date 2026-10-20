
def matrix_chain_multiplication(p):
    n = len(p) - 1

    if n <= 0:
        return 0

    dp = [
        [0] * n
        for _ in range(n)
    ]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float("inf")

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


# Student Details
print("Name: Almash Lakdawala")
print("Enrollment No.: 26PG030052")

# Matrix dimensions
dimensions = [10, 20, 30, 40, 30]

result = matrix_chain_multiplication(dimensions)

print("Minimum Multiplications:", result)
