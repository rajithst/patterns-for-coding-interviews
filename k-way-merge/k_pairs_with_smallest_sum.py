#https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
import heapq as heap
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        pq = []

        for i in range(0, min(k, len(nums1))):
            for j in range(0, min(k, len(nums2))):
                v1 = nums1[i]
                v2 = nums2[j]
                if len(pq) < k:
                    heap.heappush(pq, ((v1 + v2) * -1, [v1, v2]))
                else:
                    # pair is greater than largest value,we can't find another smallest pair(since lists are sorted)
                    #so we can break the loop
                    if v1 + v2 >= (pq[0][0]) * -1:
                        break
                    else:
                        heap.heappop(pq)
                        heap.heappush(pq, ((v1 + v2) * -1, [v1, v2]))

        res = []
        while k > 0 and len(pq) > 0:
            v, p = heap.heappop(pq)
            res.append(p)
            k -= 1
        return res