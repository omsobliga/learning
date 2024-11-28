import heapq

def f(nums, k):
    if not nums or not k:
        return []

    h = []
    for i, n in enumerate(nums):
        if i < k:
            heapq.heappush(h, -1 * n)
            continue

        if h[0] < -1 * n:
            heapq.heapreplace(h, -1 * n)

    return [-1 * i for i in h]


print(f([0,0,0,2,0,5], 0))
# print(f([2, 5, 7, 4], 1))
# print(f([0, 2, 3, 6], 2))
