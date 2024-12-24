import heapq


def f(nums, k):
    if k <= 0:
        return

    hq = []
    for i in range(k):
        heapq.heappush(hq, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > hq[0]:
            heapq.heappop(hq)
            heapq.heappush(hq, nums[i])

    return hq[0]


print(f([3,2,1,5,6,4], 2))
print(f([3,2,3,1,2,4,5,5,6], 4))
