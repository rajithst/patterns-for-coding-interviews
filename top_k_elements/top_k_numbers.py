import heapq as heap

arr = [3, 1, 5, 12, 2, 11]
K = 3
minheap = []
for i in range(K):
    heap.heappush(minheap, arr[i])

for i in range(K, len(arr)):
    if arr[i] > minheap[0]:
        heap.heappop(minheap)
        heap.heappush(minheap, arr[i])

print(minheap)
