# dp1[i] 表示最大正整数，要么 0，要么正整数
# dp2[i] 表示最小负整数，要么 0，要么负整数
# if nums[i] == 0:
# dp1[i] = 0
# dp2[i] == 0
# if nums[i] > 0:
#   dp1[i] = max(dp1[i-1] * nums[i], nums[i])
#   dp2[i] = dp2[i-1] * nums[i]
# else:
#   dp1[i] = dp2[i-1] * nums[i]
#   dp2[i] = min(dp1[i-1] * nums[i], nums[i])


def f(nums):
    if len(nums) == 0:
        return

    dp1 = [0] * len(nums)
    dp2 = [0] * len(nums)

    dp1[0] = nums[0]
    dp2[0] = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == 0:
            continue
        elif nums[i] > 0:
            dp1[i] = max(dp1[i-1] * nums[i], nums[i])
            dp2[i] = dp2[i-1] * nums[i]
        else:
            dp1[i] = dp2[i-1] * nums[i]
            dp2[i] = min(dp1[i-1] * nums[i], nums[i])

    return max(dp1)


print(f([2,3,-2,4]))
print(f([-2,0,-1]))
print(f([-2]))
