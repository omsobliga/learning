def f1(nums, k):
    """使用额外数组"""
    tmp = nums[:]
    if len(nums) <= k:
        for j in range(len(tmp)):
            i = (j + k) % len(nums)
            nums[i] = tmp[j]
        return nums

    tmp = nums[-1 * k:]

    for i in range(len(nums) - 1, k - 1, -1):
        if i - k >= 0:
            nums[i] = nums[i - k]

    for i in range(k):
        nums[i] = tmp[i]

    return nums


def f(nums, k):
    """环形替换"""
    n = len(nums) // k

    if len(nums) % k > 0:
        n += 1

    print('k, n', k, n)

    for i in range(min(k, len(nums))):
        if i >= len(nums):
            break

        tmp = nums[i]
        print('i, tmp', i, tmp, nums)
        for j in range(n):
            cur = i + (j + 1) * k
            if cur >= len(nums):
                cur = cur % len(nums)
            print(tmp, nums[cur])
            tmp, nums[cur] = nums[cur], tmp
        j
            print(tmp, nums[cur])

    return nums


# print(f([1,2], 1))
# print(f([1,2], 2))
print(f([1,2], 3))
# print(f([1,2,3,4,5,6,7], 3))
# print(f([-1], 3))
# print(f([1,2], 3))
# print(f([1,2,3], 4))
