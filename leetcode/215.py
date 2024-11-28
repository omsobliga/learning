import heapq


def f(nums, k):
    h = nums[:k]
    heapq.heapify(h)
    for n in nums[k:]:
        if h[0] < n:
            heapq.heapreplace(h, n)
    return h[0]


print(f([3,2,1,5,6,4], 2))
print(f([3,2,3,1,2,4,5,5,6], 4))
