class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def sum_of_all_paths(root):

    return traverse(root, path_sum = 0)


def traverse(current_node, path_sum):
    if not current_node:
        return 0
    path_sum = 10*path_sum + current_node.val
    print(path_sum)
    if current_node.left is None and current_node.right is None:
        return path_sum

    return traverse(current_node.left, path_sum) + traverse(current_node.right, path_sum)


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(9)
root.right.left = TreeNode(2)
root.right.right = TreeNode(9)

print(sum_of_all_paths(root))