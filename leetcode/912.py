import random

def quick_sort(nums, left, right):
    if left >= right:
        return
    start, end = left, right

    # 进行二叉树平衡
    point = random.randint(left, right)
    target = nums[point]
    nums[point], nums[right] = nums[right], nums[point]

    # 优化相等情况
    left_equal = True
    right_equal = True

    while left < right:
        while left < right and nums[left] <= target:
            if nums[left] != target and left_equal:
                left_equal = False
            left += 1

        nums[right] = nums[left]

        while left < right and nums[right] >= target:
            if nums[right] != target and right_equal:
                right_equal = False
            right -= 1

        nums[left] = nums[right]

    nums[left] = target
    if not left_equal:
        quick_sort(nums, start, left - 1)
    if not right_equal:
        quick_sort(nums, left + 1, end)


def quick_sort2(nums):
    """ 内存会超 """
    if not nums:
        return []
    target = nums[-1]
    left = [n for n in nums if n < target]
    right = [n for n in nums if n > target]
    mid = [n for n in nums if n == target]
    return quick_sort2(left) + mid + quick_sort2(right)


def f(nums):
    quick_sort(nums, 0, len(nums) - 1)
    return nums


print(f([-4,0,7,4,9,-5,-1,0,-7,-1]))
print(f([5,2,3,1]))
print(f([5, 2, 3, 1]))
print(f([5,1,1,2,0,0]))
print(f([-1,2,-8,-10]))
