# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
import heapq as heap
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        pq = []

        # push first element in each row to heap
        for i in range(len(matrix)):
            # store value,pushed index,and list itself,coz we need access to list to push next elements
            heap.heappush(pq, (matrix[i][0], 0, matrix[i]))

        # iterate while pq is not empty or till find the kth element
        count = 0
        val = None
        while pq:
            val, index, row = heap.heappop(pq)
            count += 1
            if count == k:
                break

            # if popped list as more elements,push next element to the heap
            if len(row) > index + 1:
                heap.heappush(pq, (row[index + 1], index + 1, row))

        return val
