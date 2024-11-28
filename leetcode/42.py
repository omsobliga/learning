# 方法一：DP
# left_max = []
# right_max = []
# s[i] = min(left_max[i], right_max[i])

# 方法二：stack


def f(nums):
    # print(nums)
    left_max = [0] * len(nums)
    left_max_value = 0
    for i in range(0, len(nums)):
        left_max[i] = left_max_value
        left_max_value = max(nums[i], left_max_value)
    # print(left_max)

    right_max = [0] * len(nums)
    right_max_value = 0
    for i in range(len(nums) - 1, -1, -1):
        right_max[i] = right_max_value
        right_max_value = max(nums[i], right_max_value)
    # print(right_max)

    result = 0
    for i in range(len(nums)):
        s = max(min(left_max[i], right_max[i]) - nums[i], 0)
        # print(i, s)
        result += s

    return result


def f2(nums):
    stack = []
    result = 0
    for i in range(len(nums)):
        print(result, stack)
        if not stack:
            stack.append(i)
            continue

        k = stack[-1]
        if nums[i] < nums[k]:
            stack.append(i)
            continue
        elif nums[i] == nums[k]:
            continue
        else:
            while nums[stack[-1]] < nums[i]:
                print("+", result, stack, i)
                stack.pop()
                if not stack:
                    break

                j = stack[-1]
                min_h = min(nums[i], nums[j])
                result += (min_h - nums[k]) * (i - j - 1)
                k = j

            stack.append(i)
    return result


# print(f2([1,0,2,0,2]))
# print(f2([0,1,0,2,1,0,1,3,2,1,2,1]))
# print(f2([4,2,0,3,2,5]))
