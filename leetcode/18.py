def f(nums, target):
    nums = sorted(nums)

    result = []
    result_set = set()

    for j in range(len(nums) - 3):
        if j > 0 and nums[j] == nums[j-1]:
            continue

        for i in range(j + 1, len(nums) - 2):
            if i > j + 1 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum_ = nums[j] + nums[i] + nums[left] + nums[right]
                if sum_ == target:
                    s = f"{nums[j]}_{nums[i]}_{nums[left]}_{nums[right]}"
                    if s not in result_set:
                        result.append([nums[j], nums[i], nums[left], nums[right]])
                        result_set.add(s)
                    left += 1
                    right -= 1
                elif sum_ > target:
                    right -= 1
                else:
                    left += 1

    return result


print(f([1,0,-1,0,-2,2], 0))
print(f([2,2,2,2,2], 8))
