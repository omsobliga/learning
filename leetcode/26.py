def delete_repeated_items(nums):
    if len(nums) <= 1:
        return nums

    left = right = 1
    cur = nums[0]
    repeated_count = 0
    while right < len(nums):
        while right < len(nums) and nums[right] == cur:
            repeated_count += 1
            right += 1

        if right >= len(nums):
            break

        nums[left] = nums[right]
        cur = nums[left]
        left += 1
        right += 1
        repeated_count = 0

    return nums[:left]


print(delete_repeated_items([1,1]))
