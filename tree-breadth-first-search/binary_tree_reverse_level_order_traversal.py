from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def level_order_reverse(root):
    que = deque()
    que.append(root)

    results = deque()
    while que:
        level_length = len(que)
        level_results = []
        for _ in range(level_length):
            current_node = que.popleft()
            level_results.append(current_node.val)
            if current_node.left:
                que.append(current_node.left)
            if current_node.right:
                que.append(current_node.right)
        results.appendleft(level_results)
    return results


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Reverse level order traversal: " + str(level_order_reverse(root)))
