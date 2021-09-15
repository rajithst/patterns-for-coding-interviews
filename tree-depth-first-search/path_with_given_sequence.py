class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def path_with_given_sum(root, sequence):
    return traverse(root, sequence, 0)


def traverse(current_node, given_sequence, index):
    if not current_node:
        return False

    sequence_length = len(given_sequence)
    if index > sequence_length or given_sequence[index] != current_node.val:
        return False

    if current_node.left is None and current_node.right is None and given_sequence[index] == current_node.val:
        return True

    return traverse(current_node.left, given_sequence, index + 1) or traverse(current_node.right, given_sequence,index + 1)




root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print("Tree has path sequence: " + str(path_with_given_sum(root, [1, 0, 7])))
print("Tree has path sequence: " + str(path_with_given_sum(root, [1, 1, 6])))
