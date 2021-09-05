from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def level_by_level_traversal(root):
    if root is None:
        return root

    queue = deque()
    queue.append(root)
    results = []
    while queue:
        level_length = len(queue)
        level_results = []
        for _ in range(level_length):
            current_node = queue.popleft()
            level_results.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        results.append(level_results)
    return results


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Level order traversal: " + str(level_by_level_traversal(root)))
