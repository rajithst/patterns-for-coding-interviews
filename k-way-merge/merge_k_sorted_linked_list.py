# Definition for singly-linked list.

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# override less than fucntion to compare two ListNode objects
def __lt__(self, other):
    return self.val < other.val


ListNode.__lt__ = __lt__

import heapq as heap


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # define prioority queue and insert head nodes to heap initially
        pq = []
        for l in lists:
            if l:
                heap.heappush(pq, (l.val, l))

        # define prev node and new head of merged linked list to None
        prev = None
        newhead = None
        while pq:
            # pop smallest element
            v, node = heap.heappop(pq)
            if not prev:
                prev = node
                newhead = node
            else:
                prev.next = node
                prev = prev.next

            # push next element in current node
            if node.next:
                heap.heappush(pq, (node.next.val, node.next))
        return newhead
