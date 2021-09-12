class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def has_path(root, given_sum):
    if root is None:
        return False

    if root.val == given_sum and root.left is None and root.right is None:
        return True

    #The semantics of or effectively returns the first non-false item (left to right) from between its two operands.
    return has_path(root.left, given_sum - root.val) or has_path(root.right, given_sum - root.val)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree has path: " + str(has_path(root, 23)))
print("Tree has path: " + str(has_path(root, 16)))

