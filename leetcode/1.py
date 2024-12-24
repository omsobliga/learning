def f(nums, target):
    num_mapping_index = {}

    for i in range(len(nums)):
        n = nums[i]
        if n not in num_mapping_index:
            num_mapping_index[n] = []
        num_mapping_index[n].append(i)

    for i in range(len(nums)):
        n = target - nums[i]
        if n == nums[i]:
            if len(num_mapping_index[n]) >= 2:
                return num_mapping_index[n][:2]
        else:
            if n in num_mapping_index:
                return [i, num_mapping_index[n][0]]


print(f([2,7,11,15], 9))
print(f([3,2,4], 6))
print(f([3,3], 6))
