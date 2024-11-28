# 1. 遍历
# 2. DP dp[i][j] = dp[i+1][j-1] if s[i] == s[j]


def f(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    max_length = 0
    result = ""
    for k in range(0, n):
        for left in range(0, n):
            right = left + k
            if right >= n:
                break

            if k == 0:
                dp[left][right] = 1
                if k + 1 > max_length:
                    max_length = k + 1
                    result = s[left: left + k + 1]
            elif k == 1:
                if s[left] == s[right]:
                    dp[left][right] = 1
                    if k + 1 > max_length:
                        max_length = k + 1
                        result = s[left: left + k + 1]
                else:
                    dp[left][right] = 0
            else:
                if s[left] == s[right] and dp[left + 1][right - 1]:
                    dp[left][right] = 1
                    if k + 1 > max_length:
                        max_length = k + 1
                        result = s[left: left + k + 1]
                else:
                    dp[left][right] = 0
    return result


print(f("aacabdkacaa"))
# print(f("a"))
# print(f("babad"))
# print(f("cbbd"))
