# dp[i][j] 指 a1[:i] 和 a2[:j] 最长公共子序列
# dp[i][j] = dp[i-1][j-1] if a1[i] == a2[j]
# else
# dp[i][j] = max(dp[i][j-1], dp[i-1][j])
# dp[0][j] = 1 if a1[0] = a2[j]
# dp[i][0] = 1 if a1[i] = a2[0]


def f(text1, text2):
    n1 = len(text1)
    n2 = len(text2)
    dp = [[0] * n2 for _ in range(n1)]
    max_length = 0
    for i in range(n1):
        for j in range(n2):
            if i == 0:
                if text1[0] == text2[j]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] if j > 0 else 0
            if j == 0:
                if text2[0] == text1[i]:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] if i > 0 else 0
            if i > 0 and j > 0:
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

            if dp[i][j] > max_length:
                max_length = dp[i][j]
                print(max_length, i, j)
    return max_length


print(f("oxcpqrsvwf", "shmtulqrypy"))
# print(f("abcde", "ace"))
# print(f("abc", "abc"))
# print(f("abc", "def"))
