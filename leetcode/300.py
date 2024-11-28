# dp[i] = max(dp[k] + 1) if nums[i] > nums[k]
def f(nums):
    n = len(nums)
    dp = [1] * n
    result = 0
    for i in range(n):
        for k in range(0, i):
            if nums[i] > nums[k]:
                dp[i] = max(dp[i], dp[k] + 1)
        result = max(result, dp[i])
    return result


print(f([10,9,2,5,3,7,101,18]))
print(f([0,1,0,3,2,3]))
print(f([7,7,7,7,7,7,7]))

