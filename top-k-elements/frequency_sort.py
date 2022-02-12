import heapq as heap

word = "programming"
memo = {}
for char in word:
    if char not in memo:
        memo[char] = 0
    memo[char] += 1

maxheap = []
for k, v in memo.items():
    heap.heappush(maxheap, (v * -1, k))

result = ""
while len(maxheap) > 0:
    t, k = heap.heappop(maxheap)
    result += (k * (-t))
print(result)
