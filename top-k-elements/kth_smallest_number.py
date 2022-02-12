import heapq as heap

arr = [1, 4, 12, 2, 11, 5]
k = 5
maxheap = []
# insert k elements to maxheap
for i in range(k):
    heap.heappush(maxheap, arr[i] * -1)

# for the rest of the values,
# if value is less than the largest value,remove largest value and insert new value
# (since we need minimum k values)

for i in range(k, len(arr)):
    if maxheap[0] * -1 > arr[i]:
        heap.heappop(maxheap)
        heap.heappush(maxheap, arr[i] * -1)

# end of loop,top value is the kth smallest value
print(maxheap[0] * -1)
