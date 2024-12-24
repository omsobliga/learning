# DP
# d[i] 表示包含 i 的最大连续子数组和
# d[i + 1] = d[i] + nums[i] if d[i] > 0
# else d[i + 1] = nums[i]
# d[1] = nums[1]


def f(nums):
    if len(nums) == 0:
        return

    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + nums[i]
        else:
            dp[i] = nums[i]
    return max(dp)


print(f([-2,1,-3,4,-1,2,1,-5,4]))
print(f([1]))
print(f([5,4,-1,7,8]))
