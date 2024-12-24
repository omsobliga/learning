# dp[i][j] = dp[i-1][j-1] + 1 if a[i] == b[j]
# dp[i][j] = max(dp[i][j-1], dp[i-1][j]) if a[i] != b[j]
# dp[0][j] = 1 if a[0] == b[j] else dp[0][j-1]
# dp[i][0] = 1 if a[i] == b[0] else dp[i-1][0]


def f(a, b):
    dp = [[0 for _ in range(len(b))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            if i == 0:
                if a[0] == b[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[0][j-1]
            elif j == 0:
                if a[i] == b[0]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][0]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if a[i] == b[j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
    return dp[len(a) - 1][len(b) - 1]



print(f("abcde", "ace"))
print(f("abc", "abc"))
print(f("abc", "def"))

