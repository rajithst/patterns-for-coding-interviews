from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None


class BinaryTree:
    def __init__(self, val):
        self.root = TreeNode(val)


def right_view_of_binary_tree(root):
    if root is None:
        return root

    queue = deque()
    queue.append(root)
    right_view = []

    while queue:
        level_length = len(queue)
        for i in range(level_length):
            current_node = queue.popleft()
            if i == level_length - 1:
                right_view.append(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    return right_view


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
result = right_view_of_binary_tree(root)
print("Tree right view: ")
for node in result:
    print(str(node.val) + " ", end='')
