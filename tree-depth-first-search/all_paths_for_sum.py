class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def all_paths_sum(root, given_sum):
    all_paths = []
    traverse(root, given_sum, all_paths, current_list=[])
    return all_paths


def traverse(node, given_sum, all_paths, current_list):
    if node is None:
        return
    current_list.append(node.val)

    if node.val == given_sum and node.left is None and node.right is None:
        all_paths.append(list(current_list))
    else:
        traverse(node.left, given_sum - node.val, all_paths, current_list)
        traverse(node.right, given_sum - node.val, all_paths, current_list)
    del current_list[-1]

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
required_sum = 23
print("Tree paths with required_sum " + str(required_sum) +
    ": " + str(all_paths_sum(root, required_sum)))