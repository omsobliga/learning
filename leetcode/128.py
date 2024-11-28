# dp[i] = dp[i-1] + 1 if s[i] = s[i-1] + 1

def f(nums):
    nums = sorted(nums)
    # print(nums)
    dp = [0] * len(nums)
    result = 0
    for i in range(len(nums)):
        if i == 0:
            dp[i] = 1
        else:
            if nums[i] == nums[i-1] + 1:
                dp[i] = dp[i-1] + 1
            elif nums[i] == nums[i-1]:
                dp[i] = dp[i-1]
            else:
                dp[i] = 1
        # print(dp[i])
        result = max(result, dp[i])
    return result


print(f([1,2,0,1]))
# print(f([100,4,200,1,3,2]))
# print(f([0,3,7,2,5,8,4,6,0,1]))
