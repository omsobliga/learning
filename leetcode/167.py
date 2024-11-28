def f(nums, target):
    for i in range(len(nums)):
        find_n = target - nums[i]
        left = i + 1
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid, nums[mid], find_n)
            if nums[mid] > find_n:
                right = mid - 1
            elif nums[mid] < find_n:
                left = mid + 1
            else:
                return [nums[i], nums[mid]]


print(f([-1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], -2))
# print(f([2,7,11,15], 9))
# print(f([2,3,4], 6))
# print(f([-1,0], -1))
