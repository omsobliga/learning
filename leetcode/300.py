# dp[i] = max(dp[i], dp[k] + 1) if nums[i] > nums[k]
# dp[i] = max(dp[i], dp[k]) if nums[i] == nums[k]
# else continue
# dp[i] = max(dp[i], 1)
# dp[0] = 1


def f(nums):
    dp = [0 for _ in range(len(nums))]
    result = 0
    for i in range(len(nums)):
        if i == 0:
            dp[i] = 1
        else:
            for k in range(i):
                if nums[i] > nums[k]:
                    dp[i] = max(dp[k] + 1, dp[i])
                elif nums[i] == nums[k]:
                    dp[i] = max(dp[k], dp[i])
                else:
                    continue
            dp[i] = max(dp[i], 1)
        if dp[i] > result:
            result = dp[i]
    return result


print(f([10,9,2,5,3,7,101,18]))
print(f([0,1,0,3,2,3]))
print(f([7,7,7,7,7,7,7]))
