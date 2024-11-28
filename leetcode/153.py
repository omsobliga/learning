def f(nums):
    left = 0
    right = len(nums) - 1
    min_value = nums[0]
    while left <= right:
        mid = (left + right) // 2
        # print(left, right, mid, nums[mid])
        min_value = min(min_value, nums[mid])

        if nums[left] < nums[mid]:
            min_value = min(min_value, nums[left])
            left = mid + 1
        else:
            min_value = min(min_value, nums[right])
            right = mid - 1

    return min_value


# print(f([3,4,5,1,2]))
print(f([4,5,6,7,0,1,2]))
# print(f([11,13,15,17]))
