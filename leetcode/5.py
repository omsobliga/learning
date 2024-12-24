# dp[i][j] = dp[i+1][j-1] + 2 if s[i]==s[j] and dp[i+1][j-1] > 0 else 0
# dp[i][j] = 1 if i == j
# dp[i][j] = 2 if s[i]=s[j] else 0


def f(s):
    length = len(s)
    dp = [[0 for _ in range(length)] for _ in range(length)]
    result = ""
    for k in range(length):
        for i in range(length - k):
            j = i + k
            if k == 0:
                dp[i][j] = 1
            elif k == 1:
                if s[i] == s[j]:
                    dp[i][j] = 2
            else:
                if s[i] == s[j] and dp[i+1][j-1] > 0:
                    dp[i][j] = dp[i+1][j-1] + 2
            print(k, i, j, dp[i][j])
            if dp[i][j] > len(result):
                result = s[i:j+1]
    return result


