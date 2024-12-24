import random


# 快排，不限内存
def quick_sort1(nums):
    if not nums:
        return []
    cur = nums[0]
    left = [n for n in nums if n < cur]
    equal = [n for n in nums if n == cur]
    right = [n for n in nums if n > cur]
    return quick_sort1(left) + equal + quick_sort1(right)


print(quick_sort1([3, 2, 1]))


# 快排，限内存
def quick_sort2(nums, left, right):
    if left < 0:
        return
    if right >= len(nums):
        return
    if right <= left:
        return

    i = random.randint(left, right)
    nums[i], nums[right] = nums[right], nums[i]
    cur = nums[right]

    if all([n == cur for n in nums[left: right + 1]]):
        return

    origin_left = left
    origin_right = right
    while left < right:
        while left < right and nums[left] <= cur:
            left += 1

        if left != right:
            nums[left], nums[right] = nums[right], nums[left]

        while left < right and nums[right] >= cur:
            right -= 1

        if left != right:
            nums[left], nums[right] = nums[right], nums[left]

    quick_sort2(nums, origin_left, left)
    quick_sort2(nums, left + 1, origin_right)


nums = [5,2,3,1]
quick_sort2(nums, 0, len(nums) - 1)
print(nums)


# 归并排序，不限内存
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_nums = nums[:mid]
    right_nums = nums[mid:]

    left_nums = merge_sort(left_nums)
    right_nums = merge_sort(right_nums)

    nums = []
    left_index = 0
    right_index = 0
    while left_index < len(left_nums) or right_index < len(right_nums):
        if left_index < len(left_nums) and (right_index >= len(right_nums) or left_nums[left_index] <= right_nums[right_index]):
            nums.append(left_nums[left_index])
            left_index += 1
        else:
            nums.append(right_nums[right_index])
            right_index += 1
    return nums


print(merge_sort([3,2,1]))

