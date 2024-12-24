# heapq 是最小堆
# heapq.heappush
# heapq.heappop
# pq[0]
import heapq


def f(arr, k):
    if k <= 0:
        return []

    pq = []
    for i in range(k):
        heapq.heappush(pq, arr[i] * -1)

    for i in range(k, len(arr)):
        if arr[i] < pq[0] * -1:
            heapq.heappop(pq)
            heapq.heappush(pq, arr[i] * -1)

    return [i * -1 for i in pq]


print(f([1,3,5,7,2,4,6,8], 4))
