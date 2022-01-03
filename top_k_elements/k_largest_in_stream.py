import heapq as heap


class KthLargestStream:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        self.pq = []
        for i in nums:
            self.add(i)

    def add(self, val):
        heap.heappush(self.pq, val)
        if len(self.pq) > self.k:
            heap.heappop(self.pq)
        return self.pq[0]


k = 3
kthLargestNumber = KthLargestStream([3, 1, 5, 12, 2, 11], k)
print(f"{k}th largest number is: " + str(kthLargestNumber.add(6)))
print(f"{k}th largest number is: " + str(kthLargestNumber.add(13)))
print(f"{k}th largest number is: " + str(kthLargestNumber.add(4)))
