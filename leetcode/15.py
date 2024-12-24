# 排序 + 双指针

def f(nums):
    nums = sorted(nums)
    target = 0

    result = []
    result_set = set()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]
            if sum_ == target:
                s = f"{nums[i]}_{nums[left]}_{nums[right]}"
                if s not in result_set:
                    result.append([nums[i], nums[left], nums[right]])
                    result_set.add(s)
                left += 1
                right -= 1
            elif sum_ > target:
                right -= 1
            else:
                left += 1

    return result


# print(f([-1,0,1,2,-1,-4]))
# print(f([0,1,1]))
# print(f([0,0,0,0]))
# print(f([-1,0,1,2,-1,-4]))
print(f([-2,0,0,2,2]))
