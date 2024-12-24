def backtracking(nums, path, result):
    if not nums:
        result.append(path[:])

    for i in range(len(nums)):
        path.append(nums[i])
        backtracking(nums[:i] + nums[i+1:], path, result)
        path.pop()


def f(nums):
    path = []
    result = []
    backtracking(nums, path, result)
    return result


print(f([1,2,3]))
