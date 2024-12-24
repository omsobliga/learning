def backtracking(nums, path, result):
    result.append(path[:])

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        path.append(nums[i])
        backtracking(nums[i+1:], path, result)
        path.pop()


def f(nums):
    path = []
    result = []
    nums = sorted(nums)
    backtracking(nums, path, result)
    return result


print(f([1,2,2]))
