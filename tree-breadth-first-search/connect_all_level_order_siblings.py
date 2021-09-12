from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None


def connect_all_siblings(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)
    currentNode, previousNode = None, None
    while queue:
        currentNode = queue.popleft()
        if previousNode:
            previousNode.next = currentNode
        previousNode = currentNode

        # insert the children of current node in the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

