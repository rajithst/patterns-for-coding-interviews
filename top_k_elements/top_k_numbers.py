import heapq as heap

arr = [3, 1, 5, 12, 2, 11]
K = 3
minheap = []
#insert k elements to minheap
for i in range(K):
    heap.heappush(minheap, arr[i])

#for rest of the numbers,check if number is larger than minimum value and replace
for i in range(K, len(arr)):
    if arr[i] > minheap[0]:
        heap.heappop(minheap)
        heap.heappush(minheap, arr[i])

print(minheap)
