import heapq

def f(nums, k):
    count_dict = {}
    for n in nums:
        count_dict[n] = count_dict.get(n, 0) + 1

    h = []
    for i, (key, value) in enumerate(count_dict.items()):
        # print(key, value)
        if i < k:
            heapq.heappush(h, (value, key))
            # print(h, value)
            continue

        if h[0][0] < value:
            heapq.heapreplace(h, (value, key))
        # print(h, value)

    return [i[1] for i in h]


print(f([1,1,1,2,2,3], 2))

print(f([1], 1))
